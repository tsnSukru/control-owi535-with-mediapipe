# el açık yada kapalı iken ekrana yazdırır
import threading

import cv2
import mediapipe as mp

import robotControl

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y
                x1, y1 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y

                font = cv2.FONT_HERSHEY_PLAIN
                if y1 > y:
                    cv2.putText(image, "KAPALI", (10, 50), font, 4, (0, 0, 0), 3)
                    robotControl.gripperClose()
                else:
                    cv2.putText(image, "ACIK", (10, 50), font, 4, (0, 0, 0), 3)
                    robotControl.gripperOpen()

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
