🎙️ Voice AI Assistant

A simple Voice-Activated AI Assistant built using Python, capable of listening to voice commands, speaking responses, opening websites, and performing web searches.
Designed as a beginner-friendly mini project to explore voice recognition, text-to-speech, and automation in Python.

🚀 Features

✅ Speech Recognition — Listens to your voice and understands your commands.
✅ Text-to-Speech (TTS) — Replies to you using a natural computer voice.
✅ Web Automation — Opens popular websites like YouTube, Google, and Facebook using voice commands.
✅ Web Search Integration — Performs Google searches and reads out results.
✅ Continuous Listening Mode — Keeps running until you say “stop” or “exit”.

🧩 Technologies Used

🐍 Python 3

🎤 SpeechRecognition (for voice input)

🔊 pyttsx3 (for text-to-speech)

🌐 googlesearch-python (for search results)

🧠 webbrowser (to open websites)

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/voice-ai-assistant.git
cd voice-ai-assistant

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate     # for Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


(If you don’t have a requirements.txt yet, create one with these contents:)

pyttsx3
SpeechRecognition
googlesearch-python
pyaudio

4️⃣ Run the Assistant
python main.py

🗣️ Example Commands
Command	Action
“Open YouTube”	Opens YouTube in browser
“Open Google”	Opens Google in browser
“Search AI tools”	Performs a Google search
“Stop” or “Exit”	Closes the assistant
🧠 Project Structure
voice_assistant/
│
├── assistant/
│   ├── __init__.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── main.py
├── requirements.txt
└── README.md



[![GitHub](https://img.shields.io/badge/GitHub-nzm--777-black?logo=github)](https://github.com/nzm-777)

