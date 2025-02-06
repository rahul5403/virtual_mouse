# Finger-Controlled Mouse

This project uses computer vision and hand tracking to control your computer's mouse cursor with your finger. It leverages the Mediapipe library for hand tracking and PyAutoGUI for mouse control. The program detects the position of your index finger and moves the cursor accordingly. Additionally, it allows you to click by touching your index finger and thumb together.

## Features
- Real-time hand tracking using a webcam.
- Control the mouse cursor with your index finger.
- Click by touching your index finger and thumb together.
- Simple and easy-to-use interface.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- Mediapipe (`mediapipe`)
- PyAutoGUI (`pyautogui`)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nikhil135246/virtual_mouse.git
   cd finger-controlled-mouse
   ```

2. **Install the required Python packages:**
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

3. **Run the script:**
   ```bash
   python finger_controlled_mouse.py
   ```

## Usage
1. Ensure your webcam is connected and functioning.
2. Run the script using the command above.
3. Position your hand in front of the camera. The program will detect your index finger and move the cursor accordingly.
4. To click, touch your index finger and thumb together. The program will detect the gesture and perform a mouse click.

## Notes
- The program is designed to work with a single hand.
- The sensitivity of the click gesture can be adjusted by modifying the `distance` threshold in the code.
- Ensure proper lighting conditions for accurate hand tracking.

