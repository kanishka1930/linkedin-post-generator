import os
from dotenv import load_dotenv
import google.generativeai as genai

#A function which will check if the api key is present in the .env file or not
def load_api():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print('Gemini API key was not found in the .env file')
    else:
        print('Gemini API key was successfully loaded from the .env file')
    
    return api_key


#Configure the API key
def configure_api():
    api_key = load_api() #aapki api key aa rhi hai , load_api wale function se.
    genai.configure(api_key=api_key) #ab api key ko genai ke sath configure karna hai.


#Creating a function for gemini model
def get_model():
    configure_api()
    gemini_model = "gemini-2.5-flash"
    model = genai.GenerativeModel(gemini_model)

    return model
if __name__ == "__main__": #Enty point of the program
    get_model()
    resp = get_model().generate_content("What is capital of India?")
    print(resp.text)