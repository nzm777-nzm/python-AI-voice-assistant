import speech_recognition as sr

def listen_command():
    """Listen to user voice and convert it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        recognizer.pause_threshold = 1  # wait for user pause
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"👉 You said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        print("❌ Sorry, I didn’t understand that.")
        return ""
    except sr.RequestError:
        print("⚠️ Network error.")
        return ""
