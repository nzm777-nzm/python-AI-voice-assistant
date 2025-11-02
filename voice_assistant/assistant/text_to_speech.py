import pyttsx3

def speak(text):
    """Convert text to speech"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)        # Speed of speech
    engine.setProperty('volume', 1.0)      # Volume (0.0 to 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female (you can change)
    engine.say(text)
    engine.runAndWait()
