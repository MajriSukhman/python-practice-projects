# PronounceList

Text to speech for Python lists using pyttsx3.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```python
from main import PronounceList

tts = PronounceList()
words = ['Hello', 'World']
tts.speak(words)

# customize
tts.rate = 150
tts.volume = 0.8
tts.voice = 1

# options
tts.speak(words, reverse=True)
tts.speak(words, randomize=True)
```

## CLI

```bash
python main.py
```

Gives you a menu to speak lists, change settings, etc.

## Requirements

Python 3.6+ and pyttsx3
