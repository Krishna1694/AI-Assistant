# Zion - Your Personal Voice Assistant

**Zion** is a Jarvis-inspired, AI-powered voice assistant built to help you with daily tasks through speech recognition and speech synthesis. It integrates powerful machine learning models for speech-to-text transcription and offers voice-based interactions with various commands.

## Current Capabilities

- **Speech-to-Text**: Transcribes audio input into text using OpenAI's Whisper model.
- **Text-to-Speech**: Converts text responses into speech using pyttsx3.
- **Noise Reduction**: Applies noise reduction to recorded audio for clearer voice input.
- **Basic Commands**: Handles a set of voice commands, including telling the time, opening websites, and exiting the program.
- **Continuous Listening**: Continuously listens for commands, enabling hands-free interaction.

## Present Features

- **Time & Date Commands**:
  - "What is the time?"
  - "What is today's date?"

- **Website Opening**:
  - "Open Google"
  - "Open YouTube"

- **Exit Command**:
  - "Exit"
  - "Stop"
  - "Shutdown"

- **Noise Reduction**: Automatically reduces background noise during recording to improve speech recognition accuracy.

## Requirements

- Python 3.8 or higher
- Virtual environment (recommended)

### Install the dependencies:
To install the necessary dependencies, you can use the `requirements.txt` file.

```bash
pip install -r requirements.txt 
```
## License

This project is licensed under the **Non-Commercial Use License**, which means it can be viewed and modified but not used for commercial purposes without permission.

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

Install the dependencies:

```bash
pip install -r requirements.txt
```
Run the application:

```bash
python jarvis.py
```


**You can start giving voice commands, such as:**

- "What is the time?"

- "Open YouTube"

- "Stop"

## Acknowledgments
This project was made possible with the help of ChatGPT, which provided guidance in coding, troubleshooting, and implementing features. Special thanks to OpenAI for making ChatGPT available!

## Contributing
Feel free to fork this project and submit pull requests if you'd like to contribute. Ensure that you follow the Non-Commercial Use License for any modifications.
