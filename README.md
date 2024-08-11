# 🎙️ Voice Assistant

Voice Assistant is a simple Python application that uses speech recognition to interact with users. It can perform various tasks such as playing songs, providing date and time, and answering questions about people or phone numbers.

## Features ✨

- 👋 Greet the user with "Hi" or "Hello".
- 😊 Respond to queries about emotions.
- 📅 Provide the current date.
- 🕒 Provide the current time.
- 🎵 Play songs on YouTube.
- 🧠 Answer questions about people using Wikipedia.
- 📞 Provide stored phone numbers.
- 💬 Handle basic conversational interactions.

## Requirements 📦

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- `pywhatkit` library
- `wikipedia` library
- `pyaudio` library

## Installation 🚀

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/voice-assistant.git
    cd voice-assistant
    ```

2. Install the required libraries:

    ```bash
    pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyaudio
    ```

## Usage 🎤

1. Run the script:

    ```bash
    python your_script_name.py
    ```

2. Speak to the assistant to interact. The assistant can:
    - 👋 Greet you with "Hi" or "Hello".
    - 😊 Respond to questions like "How are you?" or "How are you doing?".
    - 📅 Provide the current date.
    - 🕒 Provide the current time.
    - 🎵 Play a song on YouTube if you say "play [song name]".
    - 🧠 Provide details about a person using Wikipedia if you say "who is [person name]".
    - 📞 Provide a phone number if you ask for it.
    - 👋 End the session if you say "see you".

## Example 🗣️

```text
User: Hi
Assistant: Hello, I'm Lara, How can I help you?

User: What is the date today?
Assistant: [Date]
```

## **License 📜**

This project is licensed under the MIT License - see the LICENSE file for details.
