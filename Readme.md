# Zion - Your Personal Voice Assistant

**Zion** is a Jarvis-inspired, AI-powered voice assistant built to help you with daily tasks through speech recognition and speech synthesis. It integrates powerful machine learning models for speech-to-text transcription and offers voice-based interactions with various commands.

## Current Capabilities

- **Speech-to-Text**: Uses Google Speech Recognition for transcribing voice input.
- **Hotword Detection**: Uses porcupine free version for detecting Hotword "Jarvis".
- **Text-to-Speech**: Converts responses into spoken words using `pyttsx3`.
- **Intelligent Responses**: Zion queries OpenHermes-based local model for a natural, intelligent reply.
- **Noise Reduction**:  Automatically reduces background noise during audio capture.
- **Time & Date Commands**: Responds with the current time or date when asked.
- **Web Commands**: Opens websites like Google and YouTube, and performs searches via voice.
- **Continuous Listening**: Listens for voice commands in a loop until instructed otherwise.
- **Sleep Mode**: Enters a low-resource sleep state, wakes up on key press.

## Present Features

- **Time & Date**
  - "What is the time?"
  - "What is today's date?"

- **Website Access**
  - "Open Google"
  - "Open YouTube"

- **Search Function after website access**
  - "Search Google for cats"
  - "Search YouTube for lo-fi music"

- **Exit Commands**
  - "Exit"
  - "Stop"
  - "Shutdown"

- **Hotword Detection**
  - When the hotword "Jarvis" is detected, it wakes up and starts listening for commands.

- **Intelligent Chit-Chat**
  - Ask any general question when no specific command is recognized.

- **Noise Reduction**
  - Automatically filters background noise during listening for better recognition.

## Requirements

- Python 3.8 or higher
- Virtual environment (recommended)
- Ollama installed locally to run the OpenHermes model

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/Krishna1694/AI-Assistant.git
```
2. Navigate into the project folder and set up a virtual environment:

```bash
cd Zion
python -m venv Zion-env
```
3. Activate the virtual environment:

For Windows:

```bash
.\Zion-env\Scripts\activate
```

For macOS/Linux:
```bash
source Zion-env/bin/activate
```

### Install the dependencies:

To install the necessary dependencies, you can use the requirements.txt file.

```bash
pip install -r requirements.txt
```
**Note**: requirements.txt contain all necessary yet also some unnecessary listings, will update SOON.

### Run the application:

You have two ways to run Zion depending on your needs:

#### Default Mode (with LLM support)
Uses OpenHermes via Ollama for intelligent conversations:

```bash
python hotword.py
```

#### Basic Mode (Predefined Commands Only)
Only basic, predefined commands are supported (no LLM needed):

```bash
python Zion_pre_defined.py
```


**You can start interacting with Zion**

- Start by saying the hotword "Jarvis"

- Once detected, Zion will:

  1. Play a chime sound to signal it's ready for your voice command.

  2. Listen to your command. Following are some examples

    - "What is the time?"

    - "Open google" then follow with "search for {any query}"

    - "Go to sleep"

    - "Stop"

Zion will also answer general questions intelligently by utilizing the local OpenHermes model on Zion_AI.py.

**Note**: Hotword detection is only enables for Zion_AI.py not for Zion_pre_defined.

## Acknowledgments
This project was made possible with the help of ChatGPT, which provided guidance in coding, troubleshooting, and implementing features. Special thanks to OpenAI for making ChatGPT available!

## License
This project is licensed for Personal and Educational Use Only.

- You may use Zion for your own learning, growth, and non-commercial purposes.
- You may not modify, redistribute, or sell this project or its derivatives without explicit permission from the author.

For commercial use, modification, or redistribution, please contact the project owner.

> "Zion" is always improving. Stay tuned for vision support, offline memory, and much more in future updates!