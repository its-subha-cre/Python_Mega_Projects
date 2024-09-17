import pyautogui
import pyperclip
import time 
import google.generativeai as genai
from dotenv import load_dotenv

pyautogui.click(752,1057)
time.sleep(1)
pyautogui.moveTo(595,279)
pyautogui.dragTo(594,912,duration=1,button="left")
pyautogui.hotkey('ctrl','c')
time.sleep(1)
text=pyperclip.paste()
print(text)
