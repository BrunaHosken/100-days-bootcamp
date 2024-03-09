# Write Python code to play the Google Dinosaur Game.

import time
from PIL import ImageGrab
import pyautogui

def get_screen(region=None):
    screenshot = ImageGrab.grab(bbox=region)
    return screenshot

def is_obstacle(pixel):
    # You may need to adjust the color values based on your screen and browser theme
    obstacle_color = (83, 83, 83)  # Color of the obstacle in RGB
    return pixel == obstacle_color

def jump():
    pyautogui.press('space')

def main():
    region = (440, 320, 840, 400)  # Adjust these coordinates based on your screen resolution
    pyautogui.click()  # Click on the game to focus

    while True:
        screen = get_screen(region)

        # Check the pixels in the middle of the screen for obstacles
        for x in range(100, 200, 10):
            pixel = screen.getpixel((x, 50))
            if is_obstacle(pixel):
                jump()
                break

        time.sleep(0.1)  # Adjust the sleep time as needed

if __name__ == "__main__":
    main()
