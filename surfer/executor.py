from dotenv import load_dotenv

from WebSurfer.surfer.model_calls import text_request
from WebSurfer.surfer.prompts import AI_TEXT

if __name__ == '__main__':
    load_dotenv()
    questions = [
        "Does Jack Lucci appear as one of the founders of DataSense on the website?"
    ]
    for question in questions:
        print("\n----------------\n")
        print(question)
        print(text_request(
            user_text=question,
            ai_text=AI_TEXT
        ))