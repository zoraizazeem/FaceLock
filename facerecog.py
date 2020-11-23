import numpy as np
import face_recognition as fr
import cv2
from sendsms import *
from decrypt import *

video_capture = cv2.VideoCapture(0)

zoraiz_image = fr.load_image_file("zoraiz-azeem.jpg.jpeg")
zoraiz_face_encoding = fr.face_encodings(zoraiz_image)[0]

known_face_encodings = [zoraiz_face_encoding]
known_face_names = ["Zoraiz"]
counter = 0

namelist = []
while True:
    
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]
    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
        matches = fr.compare_faces(known_face_encodings, face_encodings)

        matches = fr.compare_faces(known_face_encodings, face_encodings)

        name= "Unknown"

        face_distances = fr.face_distance(known_face_encodings, face_encodings)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0,0,255), 2)

        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0,0, 255), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left +6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        namelist.append(name)
        

    cv2.imshow('Webcam_facerecognition', frame)
    if "Zoraiz" in namelist:
        sendmess()
        decryptpass()
        print("is in list")
        break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
