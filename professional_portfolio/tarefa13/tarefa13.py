# Write Python code to play the Google Dinosaur Game.

import time
from PIL import ImageGrab
import pyautogui

def get_screen(region=None):
    screenshot = ImageGrab.grab(bbox=region)
    return screenshot

def is_obstacle(pixel):
    obstacle_color = (83, 83, 83) 
    return pixel == obstacle_color

def jump():
    pyautogui.press('space')

def main():
    region = (440, 320, 840, 400) 
    pyautogui.click() 

    while True:
        screen = get_screen(region)

        for x in range(100, 200, 10):
            pixel = screen.getpixel((x, 50))
            if is_obstacle(pixel):
                jump()
                break

        time.sleep(0.1) 

if __name__ == "__main__":
    main()
