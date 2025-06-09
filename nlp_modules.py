'''
import openai

openai.api_key = "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"  # My OpenAI API key

def get_answer(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip() 

# nlp_modules.py
import os
from openai import OpenAI
from dotenv import load_dotenv




load_dotenv()
print("API KEY:", os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_answer(question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful tutor."},
                {"role": "user", "content": question}
            ],
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

'''

import os
from dotenv import load_dotenv
import requests
import time
import pyttsx3

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
print("🔑 API KEY LOADED:", API_KEY)  # Debug line

if not API_KEY:
    raise ValueError("❌ ASSEMBLYAI_API_KEY not found. Check your .env file.")
upload_url = "https://api.assemblyai.com/v2/upload"
transcript_url = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization': API_KEY}


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def upload(filename):
    try:
        with open(filename, 'rb') as f:
            response = requests.post(upload_url, headers=headers, data=f)

        print("Response Status Code:", response.status_code)
        print("Response Text:", response.text)

        # Check for a successful HTTP response
        if response.status_code != 200:
            raise Exception(f"Upload failed. Status code: {response.status_code}, Response: {response.text}")

        # Parse JSON response
        data = response.json()

        # Check if 'upload_url' is in response
        #upload_url_key = data.get('upload_url')
        if 'upload_url' in data:
            return data['upload_url']
        else:
            raise Exception(f"❌ Unexpected response structure. Missing 'upload_url'. Response: {data}")

    except requests.exceptions.JSONDecodeError:
        raise Exception(f"❌ Failed to decode JSON. Raw Response: {response.text}")

    except FileNotFoundError:
        raise Exception(f"❌ File not found: {filename}")

    except Exception as e:
        raise Exception(f"❌ Upload Error: {str(e)}")




def request_transcript(audio_url):
    json = {"audio_url": audio_url}
    response = requests.post(transcript_url, json=json, headers=headers)
    #return response.json()['id']
    try:
        data = response.json()
        if response.status_code != 200:
            print("❌ Upload error:", data)
        return data['id']
    except Exception as e:
        print("❌ Failed to parse JSON response:", response.text)
        raise e


def get_transcript_result(transcript_id):
    response = requests.get(f"{transcript_url}/{transcript_id}", headers=headers)
    return response.json()


def process_audio_input(filename):
    print("🔁 Processing voice input...")
    audio_url = upload(filename)
    transcript_id = request_transcript(audio_url)

    while True:
        result = get_transcript_result(transcript_id)
        if result['status'] == 'completed':
            #print("📝 Transcription:", result['text'])
            #speak_text(result['text'])  # Speak the result
            print("📝 You said:", result['text'])
            # Get response from Ollama
            ai_response = generate_response(result['text'])
            print("🤖 AI Tutor:", ai_response)
            # Speak the AI response aloud
            speak_text(ai_response)
            break
        elif result['status'] == 'error':
            print("❌ Error:", result['error'])
            speak_text("Sorry, there was an error in processing your voice.")
            break
        time.sleep(5)

def generate_response(prompt):
    try:
        url = "http://localhost:11434/api/chat"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama3",  # You can also use mistral, gemma, etc.
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        return result["message"]["content"]
    
    except Exception as e:
        return f"❌ Error from Ollama: {str(e)}"

