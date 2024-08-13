import cv2
import mediapipe as mp
import pyautogui

# Initialize camera and hand tracking
cam = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
screen_w, screen_h = pyautogui.size()

# Variable to track if the mouse button is held down
mouse_down = False

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hands.process(rgb_frame)
    frame_h, frame_w, _ = frame.shape

    if output.multi_hand_landmarks:
        hand_landmarks = output.multi_hand_landmarks[0].landmark

        # Index fingertip (landmark 8) and thumb tip (landmark 4)
        index_finger_tip = hand_landmarks[8]
        thumb_tip = hand_landmarks[4]

        # Calculate screen position from index fingertip
        screen_x = int(index_finger_tip.x * screen_w)
        screen_y = int(index_finger_tip.y * screen_h)

        # Move the cursor
        pyautogui.moveTo(screen_x, screen_y)

        # Draw fingertip landmarks on the frame
        index_x = int(index_finger_tip.x * frame_w)
        index_y = int(index_finger_tip.y * frame_h)
        thumb_x = int(thumb_tip.x * frame_w)
        thumb_y = int(thumb_tip.y * frame_h)
        cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), -1)
        cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 255, 0), -1)

        # Detect touch between index fingertip and thumb tip to hold/release mouse button
        distance = ((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2) ** 0.5
        if distance < 30:  # Threshold for detecting touch
            if not mouse_down:
                pyautogui.mouseDown()
                mouse_down = True
        else:
            if mouse_down:
                pyautogui.mouseUp()
                mouse_down = False

    # Display the frame
    cv2.imshow('Finger Controlled Mouse', frame)
    cv2.waitKey(1)
