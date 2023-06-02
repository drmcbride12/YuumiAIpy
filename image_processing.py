import cv2
import pyautogui

def capture_screen():
    # Use pyautogui to capture the screen
    screenshot = pyautogui.screenshot()

    # Convert the PIL Image to an OpenCV image (BGR to RGB)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    return screenshot
