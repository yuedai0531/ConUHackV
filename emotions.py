import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

GOOGLE_APPLICATION_CREDENTIALS = {
  "type": "service_account",
  "project_id": "conu-266219",
  "private_key_id": "4894156455ccd186a8e1e7bb3a8cf6a499500d9e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQDRMcR+eD+jPuEg\nrOzxMduYuozNmlbBVKVvZjHmHuw4YZPB6BRscly2Jei7YvNh41gXyHK7eHQq+OsK\nq0k6QBpENd3leCwtWoV0Rg4BVBu61q+vyuiJ2+ab2OzaYFJEk3UrQ1hSQ1FbrUUw\nMuxQEomnNpDbGZmGrbEMfXSoaPaEiX1vuv4SWhcPr2v0fJXwehdtPIpeCNAQIQkv\n99ZaosJ7oCM7BTg/rLP2+k0/VkRADE+HQ54HQ4EVnlY62TmBQ8jTdR6SghyVyVDh\nl2RZrEIUcsNIL7Ztvq742St6u5lLXHOdRkzv+khBiJaXn4wFFYgFwyylSXGmYaX8\njDYW9yATAgMBAAECgf9gbJAlu0eZ92HNreeJRXHy9AnyuzFB68JVlsVpTNeVJWT1\n/ANt+UjCrLaZqQKGHER+seYwg1UIebPdNxaJwwJYbnvZSYsTXKYm8iOCeUJO3KYe\nYWjOIo4pR9Pk1IEXGuDnECOlx2G44CUEEnTac7D/Yidi1mntqiHxn+Ilvjvi2qdn\n0oZu+OxsbRkBfMrw3WQCctAtZPA3EUhA9uhiKjtW45Guk3ixDQikgXeDSN3fVeBz\nPjTCXr32Bohc9JtJo6Q8irdf9wJI8d+6aOAj3brE253mZys1QxcLoJnnKbHQNeFQ\nch/FOZdftvHJbI3RVtoFPWMGMVOq8oaPV8FBJEECgYEA8jMJ52MAjZ/DOE39wq7i\nrxjWelj0/PRwnsucQVXN8xALhMWEtFAt2QbpmcvZOSRx2zOcxu6xY53iouz0Xo4x\ns4+/805tLrszwPRW2/E6B8MJ1Ztjosh9bbmC7sfPztHPj/slc99M71rdUd5KM9oq\nN9sDHQwbmUcMkdaWnq5nFjECgYEA3R1JGngIfbsYoVt2lZTGasWPqt2Tkt7uQHmE\nc7i9x9FI4qTqfNiq10OBRu+wSa6wsYmhE9Y8atndV1eurwg7dP3i1Kq9URvE8kNq\nnOkBsm6CIBk6klHhJovh2evW+BX1sJi+RRIW3hw+Gmpuo5NJUY5ZNhOVOCH94SY+\nq87A1YMCgYBaVAKrk1bPevgZ9axggUz1tLO46ZhlBt1Bu/pIu7GVpzREjk3R2d1f\nhZ51x3r6Psdf0z3zS25JEsdFsE3rPej3aPNT0LoTpanFmtsSKENWRb1TNyLPwSpW\nU8urNkYggkuBDU+IiY1t71t/fwH5mLIKJtpgaPWaEs9zTK7b+3ti4QKBgBxjTCVn\nz79ErA7bTUg7B5ZhsuY++Flc4b3JXCX3S/ZBelgO0EQjFRv6ALj4wOtU0D6a6uE/\nGhalzfMOwNCb//YvOlYPbariI9DustteVudvpKk2U/zBImTuhJqT2s+TEi4QDi2T\n+vedLKP7kiTSHhGocu+sZ/YC9zNW06j/LGa9AoGBAJ3JRVUmKb3izY6+cDaoxvhv\nrxVg6CIvnoOaQbq+TnCh+bLc6IqzQSlkNna916MSXpAQc4kXFTHWHZlviKcsO2AV\nv2YTA5tIUIFhkgAw8zmVelNGy7B8Kvlobfe5eCgVmAhSdMHNnwzsiBd5iGtJqN62\n6uyOEtNveM9jnAFYliZR\n-----END PRIVATE KEY-----\n",
  "client_email": "conu-235@conu-266219.iam.gserviceaccount.com",
  "client_id": "111294613708189003482",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/conu-235%40conu-266219.iam.gserviceaccount.com"
}
#
# # Instantiates a client
# client = vision.ImageAnnotatorClient(credentials=GOOGLE_APPLICATION_CREDENTIALS)
#
# # The name of the image file to annotate
# file_name = os.path.abspath('ohwonder.jpg')
#
# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()
#
# image = types.Image(content=content)
#
# # Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations
#
# # print('Labels:')
# # for label in labels:
# #     print(label.description)



def detect_faces(path):
    """Detects faces in an image."""

    from google.oauth2 import service_account

    credentials = service_account.Credentials. from_service_account_file('GCapikey.json')

    client = vision.ImageAnnotatorClient(credentials=credentials)

    # client = vision.ImageAnnotatorClient(credentials=GOOGLE_APPLICATION_CREDENTIALS)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    count = 0
    for face in faces:
        print(count)
        count += 1

        print(face)

        # print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        # print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        # print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


