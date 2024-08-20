import speech_recognition as sr
import subprocess
import re

apps = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe"
}

def open_app(app_name):
    if app_name in apps:
        app_path = apps[app_name]
        print(f"Opening {app_name}...")
        subprocess.Popen([app_path])
    else:
        print(f"Aplication '{app_name}' not found.")

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="en")
            print("Recognized text: " + text)
            if 'open' in text.lower():
                match = re.search(r'open\s+(\w+)', text.lower())
                if match:
                    app_name = match.group(1)
                    open_app(app_name)
                else:
                    print("Nije prepoznata aplikacija nakon komande 'open'.")
        except sr.UnknownValueError:
            print("Text is not recognized")
        except sr.RequestError as e:
            print(f"Error; {e}")

if __name__ == "__main__":
    recognize_speech()
