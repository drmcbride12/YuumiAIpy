import pyautogui

# Define the coordinates for different actions
# You'll need to adjust these values based on your game setup
ACTION_COORDINATES = {
    'move_up': (100, 200),
    'move_down': (100, 300),
    'move_left': (50, 250),
    'move_right': (150, 250),
    # ... add more actions as needed ...
}

def execute_action(action):
    # Get the coordinates for the action
    coordinates = ACTION_COORDINATES.get(action)

    if coordinates is not None:
        # Move the mouse to the specified coordinates and click
        pyautogui.moveTo(coordinates)
        pyautogui.click()
    else:
        print(f'Unknown action: {action}')
