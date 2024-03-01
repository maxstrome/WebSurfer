from dotenv import load_dotenv
from openai import OpenAI
import base64
import requests
import pyautogui
import tempfile
import base64
import requests
import numpy as np
import matplotlib.pyplot as plt
# OpenAI API Key



def take_screenshot():
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

        # Capture screenshot and save to a temporary file

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        screenshot = pyautogui.screenshot()
        screenshot_array = np.array(screenshot)
        height, width, _ = screenshot_array.shape

        plt.imshow(screenshot_array)
        plt.show()
        screenshot.save(temp_file.name)
        image_path = temp_file.name

        # Encode the screenshot
    base64_image = encode_image(image_path)
    return base64_image

def get_screen_dimensions():
    screenWidth, screenHeight = pyautogui.size()
    return screenWidth, screenHeight

def get_current_cursor_location():
    currentMouseX, currentMouseY = pyautogui.position()
    return currentMouseX, currentMouseY


def moveTo(x, y):
    pyautogui.moveTo(x, y)