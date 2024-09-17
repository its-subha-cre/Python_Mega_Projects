# import pyautogui
# while True:
#      a=pyautogui.position()
#      print(a)
# #     # 594 217 594 914
# #      779 1075
import pyautogui
import pyperclip
import time 
import google.generativeai as genai
from dotenv import load_dotenv
import os

pyautogui.click(752,1057)
time.sleep(1)
pyautogui.moveTo(595,279)
pyautogui.dragTo(594,912,duration=1,button="left")
pyautogui.hotkey('ctrl','c')
time.sleep(1)
text=pyperclip.paste()
print(text)

genai.configure(api_key=os.getenv("api_key"))

    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                                        }
                

model = genai.GenerativeModel(
                        model_name="gemini-1.5-pro",
                        generation_config=generation_config,
                        # safety_settings = Adjust safety settings
                        # See https://ai.google.dev/gemini-api/docs/safety-settings
                        )
                
                
chat_session = model.start_chat(
                        history=[
                        ]
                        )
response = chat_session.send_message(text)

print(response.text)