# Simple-Projects

Python projects for beginners — with a unified launcher.

## Quick Start

```bash
# Interactive menu
python main.py

# Launch a specific project by number
python main.py 2

# Launch a specific project by name
python main.py calculator

# List all available projects
python main.py --list
```

## Projects

|  # | Name                | Description                                      | Extra Deps          |
|---:|---------------------|--------------------------------------------------|---------------------|
|  1 | Binary Search       | Search a sorted list using binary search          | —                   |
|  2 | Calculator          | Basic arithmetic: add, subtract, multiply, divide | —                   |
|  3 | Countdown Timer     | Count down from a given number of seconds         | —                   |
|  4 | Currency Converter  | Convert between currencies via exchange-rate API  | `requests`          |
|  5 | Dice Roll           | Simulate rolling one or more dice                 | —                   |
|  6 | Email Slicer        | Split an email address into username and domain   | —                   |
|  7 | Hangman             | Classic word-guessing game                        | —                   |
|  8 | Music Player        | Play MP3 files                                    | `pygame`, GUI (tk)  |
|  9 | Password Generator  | Generate a random secure password                 | —                   |
| 10 | QR Code Generator   | Create a QR code image from any data              | `qrcode`            |
| 11 | Quiz                | Answer multiple-choice trivia questions           | —                   |
| 12 | Rock Paper Scissors | Play rock-paper-scissors against the computer     | —                   |
| 13 | Snake Game          | Classic snake game                                | `pygame`, GUI       |
| 14 | Tic Tac Toe         | Two-player tic-tac-toe in the terminal            | —                   |
| 15 | Typing Speed Test   | Measure your typing speed (WPM)                   | —                   |
| 16 | Voice Recorder      | Record audio from microphone                      | `pyaudio`           |
| 17 | YouTube Downloader  | Download YouTube videos                           | `pytube`            |

## Running Individual Scripts

Each script can still be run on its own:

```bash
python "Calculator.py"
python "Hangman.py"
```

## Verification

Run the built-in smoke test to check the launcher and project imports:

```bash
python test_launcher.py
```
