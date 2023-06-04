import pyautogui
from pynput import mouse, keyboard
import time
import os
import cv2
import numpy as np

# Create a directory to save screenshots
os.makedirs('screenshots', exist_ok=True)

# Output file for actions
output_file = open('output.txt', 'w')

# Colors
colors = [
    np.array([255, 0, 0]),  # Red
    np.array([0, 255, 0]),  # Green
    np.array([0, 0, 255]),  # Blue
    np.array([0, 0, 0]),    # Black
    np.array([255, 255, 255]) # White
]

def reduce_colors(img):
    # Euclidean distance between the image and each of the colors
    distances = [np.linalg.norm(img - color, axis=-1) for color in colors]

    # Create a new image, starting off all black (color 3)
    new_img = np.zeros(img.shape, np.uint8)
    for i in range(4):
        new_img[distances[i] < distances[i + 1]] = colors[i]

    return new_img

# Mouse and keyboard listeners
def on_click(x, y, button, pressed):
    output_file.write(f'Mouse {button} {"Pressed" if pressed else "Released"} at {(x, y)}, {time.time()}\n')
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.resize(screenshot, (320, 180))
    screenshot = reduce_colors(screenshot)
    cv2.imwrite(f'screenshots/{time.time()}_click.png', screenshot)

def on_key_press(key):
    x, y = pyautogui.position()
    output_file.write(f'Key {key} pressed at {(x, y)}, {time.time()}\n')
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.resize(screenshot, (320, 180))
    screenshot = reduce_colors(screenshot)
    cv2.imwrite(f'screenshots/{time.time()}_keypress.png', screenshot)

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_key_press)

# Start listeners
mouse_listener.start()
keyboard_listener.start()

try:
    # Keep the script running.
    while True:
        pass
except KeyboardInterrupt:
    # When Ctrl+C is pressed, stop listeners and close the output file.
    mouse_listener.stop()
    keyboard_listener.stop()
    output_file.close()
