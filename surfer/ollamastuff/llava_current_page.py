import pyautogui
import requests
import base64
from io import BytesIO

from langchain_community.llms.ollama import Ollama

llava = Ollama(model="llava")


# Take a screenshot using pyautogui
screenshot = pyautogui.screenshot()

# Convert the screenshot to a bytes-like object
buffered = BytesIO()
screenshot.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Prepare the data for the POST request

llm_with_image_context = llava.bind(images=[img_str])
print(llm_with_image_context.invoke("What is in this image"))