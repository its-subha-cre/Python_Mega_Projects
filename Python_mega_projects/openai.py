
import google.generativeai as genai
from dotenv import load_dotenv
import os
text='''0:35, 28/7/2024] Adri ❤️🍫: Krooooo
[20:35, 28/7/2024] Adri ❤️🍫: Kro
[20:35, 28/7/2024] Adri ❤️🍫: Jaaantu koro
[20:35, 28/7/2024] Adri ❤️🍫: Koro
[20:35, 28/7/2024] Adri ❤️🍫: Koro
[20:35, 28/7/2024] Adri ❤️🍫: Kror
[20:35, 28/7/2024] Adri ❤️🍫: Kor
[20:35, 28/7/2024] Adri ❤️🍫: Korro
[20:35, 28/7/2024] Subhyan Chatterjee: Ha
[20:36, 28/7/2024] Adri ❤️🍫: 😃'''

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