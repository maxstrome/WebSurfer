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
load_dotenv()
client = OpenAI()


def text_request(user_text, ai_text):
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": ai_text
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_text
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content

def image_request(image, text):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image}"
                        }
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    print(text_request(user_text="What is my name", ai_text="Say their name is Max"))