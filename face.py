import cv2

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

recognizer = cv2.face.LBPHFaceRecognizer_create()