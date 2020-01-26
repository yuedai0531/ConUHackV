import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
from acs import send
import os
from emotions import detect_faces

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:  # Infinite loop to get video, create bounding box,
    if not video_capture.isOpened():  # If webcam is not working
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()  # Take frame from webcam

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts to grayscale

    faces = faceCascade.detectMultiScale(  # Detects faces, stores the coordinates of the faces for boxes
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # If faces are detected, send the api call
    if len(faces) != 0:
        # print(len(faces))
        cv2.imwrite("image.jpg", frame)  # Save the image if there are faces

        if anterior != len(faces):
            anterior = len(faces)
            log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        sum_dict = {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 0.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
        # Send jpg to azure cognitive services and get the faceattributes
        image_directory = os.path.dirname(__file__) + '/image.jpg'
        response = send(image_directory)
        if response:
            faces = response
            for face in faces:
                face_attributes = face['faceAttributes']
                emotion_dict = face_attributes['emotion']
                # print(emotion_dict)
                for emotion in emotion_dict.keys():
                    sum_dict[emotion] += emotion_dict[emotion]


        num_faces = len(faces)
        # print(num_faces)
        average_dict = {k: v/num_faces for k, v in sum_dict.items()}
        del average_dict['neutral']

        max_emotion = max(average_dict.values())
        for emotion in average_dict.keys():
            average_dict[emotion] /= max_emotion

        print(average_dict)

        sleep(1)

    # Display the resulting frame
    cv2.imshow('Video', frame)



    response = None


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
