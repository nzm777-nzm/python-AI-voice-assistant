import webbrowser
from googlesearch import search
from assistant.text_to_speech import speak
from assistant.speech_to_text import listen_command

def web_search(query, num_results=5):
    """Perform a web search and return the top results"""
    return list(search(query, num_results=num_results))

if __name__ == "__main__":
    speak("Hey Nazeem! I'm your voice assistant. How can I help you today?")

    while True:
        command = listen_command().lower()

        if not command:
            speak("Sorry, I didn't catch that. Please say again.")
            continue

        print(f"🎧 Command heard: {command}")

        # EXIT COMMANDS
        if 'stop' in command or 'exit' in command or 'quit' in command:
            speak("Goodbye Nazeem! Have a great day!")
            break

        # WEBSITE COMMANDS
        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open facebook' in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

        elif 'open instagram' in command:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        # SEARCH COMMAND
        elif 'search' in command:
            speak("Searching the web for your query.")
            query = command.replace('search', '').strip()
            results = web_search(query, num_results=3)

            for idx, result in enumerate(results, start=1):
                speak(f"Result {idx}")
                print(result)

        # UNKNOWN COMMAND
        else:
            speak("Sorry, I didn’t understand that command.")
