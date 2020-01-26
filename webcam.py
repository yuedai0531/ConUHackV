import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
from acs import send
import os
from emotions import detect_faces
import datetime as dt
from datetime import timedelta
from post_elasticsearch import data_generation

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

emotion_threshold = 0.05

prevtime = dt.datetime.now()

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

    # Display the resulting frame
    cv2.imshow('Video', frame)
    try:
        # If faces are detected, send the api call with the biggest face found
        # API call only runs once every five seconds at most
        curtime = dt.datetime.now()
        if (len(faces) != 0) and (abs((prevtime-curtime).total_seconds()) > 4):

            prevtime = curtime
            # Find the biggest face, will be closest user
            max_area = 0
            biggest_face = None
            for (x, y, w, h) in faces:
                area = w * h
                if area > max_area:
                    max_area = area
                    biggest_face = (x, y, w, h)

            if biggest_face is not None:
                biggest_face_frame = frame[y:y+h, x:x+w]
                cv2.imwrite("image.jpg", biggest_face_frame)
                # acs.send("image.jpg")q

                # Draw a rectangle around the biggest face
                (x, y, w, h) = (biggest_face[0], biggest_face[1], biggest_face[2], biggest_face[3])
                (cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2))

            if anterior != len(faces):
                anterior = len(faces)
                log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

            # Send jpg to azure cognitive services and get the faceattributes
            image_directory = os.path.dirname(__file__) + '/image.jpg'
            response = send(image_directory)
            # print(response)
            if response:
                face_attributes = response[0]['faceAttributes']
                emotion = face_attributes['emotion']
                # print(emotion)

                response = None

                # Remove neutral emotion. If any of the other emotions exceed the threshold value,
                # send the emotion's key to Kibana
                del emotion['neutral']
                max_emotion = 0
                max_emotion_string = None
                for key in emotion.keys():
                    if emotion[key] > max_emotion and emotion[key] > emotion_threshold:
                        max_emotion = emotion[key]
                        max_emotion_string = key

                if max_emotion_string is not None:
                    print('You are feeling :' + max_emotion_string)
                    # Send the max_emotion_string to the kibana
                    json_object = {
                        "sentiment": max_emotion_string,
                        "timestamp": dt.datetime.now().isoformat()
                    }
                    data_generation(json_object)
    except:
        print("API limit exhausted")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
