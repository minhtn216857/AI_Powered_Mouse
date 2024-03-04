import mediapipe as mp
import cv2
import pyautogui

# ve tien ich + show landmarks
mp_drawing = mp.solutions.drawing_utils
# Dua mo hinh ban tay co san
mp_hands = mp.solutions.hands

screen_width, screen_height = pyautogui.size()
index_y = 0
thumb_y = 0
mid_finger_y = 0

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.8,
        min_tracking_confidence=0.5
) as hands:

    while cap.isOpened():
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

        frame_height, frame_width, _ = frame.shape

        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame)
    
        # Draw the hand annotations on the image
        frame.flags.writeable = False
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(231, 22, 176), thickness=2, circle_radius=2))
                landmarks = hand_landmarks.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(frame_width * landmark.x)
                    y = int(frame_height * landmark.y)
                    #print(x, y)
                    if id == 8:
                        cv2.circle(frame, (x, y), radius=15, color=(0, 255, 255))
                        index_x = x * screen_width / frame_width
                        index_y = y * screen_height / frame_height
                        pyautogui.moveTo(index_x, index_y)

                    if id == 4:
                        cv2.circle(frame, (x, y), radius=15, color=(0, 255, 255))
                        thumb_x = x * screen_width / frame_width
                        thumb_y = y * screen_height / frame_height

                    if id == 11:
                        cv2.circle(frame, (x, y), radius=15, color=(0, 255, 255))
                        mid_finger_x = x * screen_width / frame_width
                        mid_finger_y = y * screen_height / frame_height
                        if abs(thumb_y - mid_finger_y) < 15:
                            print('Output: ', abs(thumb_y - mid_finger_y))
                            pyautogui.click()
                            pyautogui.sleep(0.3)

        cv2.imshow('test', frame)
        if cv2.waitKey(10) & 0xFF == ord(' '):
            break


