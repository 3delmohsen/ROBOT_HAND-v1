import pyrebase
import cv2
from cvzone.HandTrackingModule import HandDetector

# config connection with firebase
firebaseConfig = {
    "apiKey": "AIzaSyD_gWN2fEjU1Kky3VshiY5ITEtolmgFN0s",
    "authDomain": "robothand-2de5a.firebaseapp.com",
    "databaseURL": "https://robothand-2de5a-default-rtdb.firebaseio.com",
    "projectId": "robothand-2de5a",
    "storageBucket": "robothand-2de5a.appspot.com",
    "messagingSenderId": "415701415735",
    "appId": "1:415701415735:web:7e0605c422c34b56c60cb2",
    "measurementId": "G-G4T6SW59HE"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        finger = detector.fingersUp(hand)
        data = {"1": finger[0], "2": finger[1], "3": finger[2], "4": finger[3], "5": finger[4]}
        db.update(data)

        print(finger)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
