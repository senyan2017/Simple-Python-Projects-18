# Simple-Projects

A small collection of beginner-friendly Python projects, now with a single
launcher so you can pick and run any of them without hunting through files.

## Quick start

```bash
python main.py            # interactive menu: pick a project by number or name
python main.py --list     # just print the project list and exit
python main.py --check    # report which projects can run in this environment
python main.py 2          # run project #2 (Calculator) directly
python main.py calculator # run by (partial) name directly
python main.py "Snake Game"
```

In the interactive menu you can type a **number** or a **name**, type `l` to
re-list, and type `q` (or `quit` / `exit`) to leave. Invalid or out-of-range
input just shows a hint and asks again -- it never gets stuck.

The launcher runs each project as a separate process and **does not modify the
original scripts**, so every file below still works on its own, e.g.:

```bash
python "Hangman.py"
```

## Requirements & graceful fallback

Most projects use only the Python standard library and run anywhere. A few need
extra libraries, a graphical display, the network, or audio hardware. The
launcher checks for these *before* starting a project: if something is missing
it prints a short note (and the `pip install ...` command to fix it) and returns
to the menu instead of crashing. Run `python main.py --check` to see the status
of every project at a glance.

| # | Project | What it does | Needs |
|---|---------|--------------|-------|
| 1 | Binary Search Algorithm | Binary search on a sorted list (built-in example) | stdlib |
| 2 | Calculator | Add / subtract / multiply / divide two numbers | stdlib |
| 3 | Countdown Timer | Counts down from a number of seconds | stdlib |
| 4 | Currency Converter | Converts USD to EUR via a live API | `requests`, network |
| 5 | Dice Simulation | Rolls a six-sided die N times | stdlib |
| 6 | Email Slicer | Splits an email into username + domain | stdlib |
| 7 | Hangman | Word-guessing game in the terminal | stdlib |
| 8 | Music Player | GUI player for local `.mp3` files | `tkinter`, `pygame`, display, audio |
| 9 | Password Generator | Prints a random 10-character password | stdlib |
| 10 | QR Code Generator | Saves a QR code image (`qrcode.png`) | `qrcode` |
| 11 | Quiz Application | Multiple-choice quiz with scoring | stdlib |
| 12 | Rock Paper Scissors | Play against the computer | stdlib |
| 13 | Snake Game | Arrow-key Snake in a window | `pygame`, display |
| 14 | Tic Tac Toe | Two-player 3x3 text board | stdlib |
| 15 | Typing Speed Test | Words-per-minute typing test | stdlib |
| 16 | Voice Recorder | Records 5s of mic audio to `output.wav` | `pyaudio`, microphone |
| 17 | Youtube Downloader | Downloads a YouTube video by URL | `pytube`, network |

> Note: `QR Code Generator`, `Snake Game`, `Voice Recorder` and
> `Youtube Downloader` were exported from Jupyter notebooks and still contain a
> leftover bare `pip install ...` line at the top. Install the listed package
> first; the launcher's pre-check will flag these for you.

## Verify it works

A minimal, non-interactive self-test is included. It checks the project
registry, the number/name resolver, and the real CLI end to end (including a
genuine direct launch of a dependency-free project):

```bash
python verify.py
```

It prints a `PASS`/`FAIL` line per check and exits non-zero if anything is
broken. You can also sanity-check manually:

```bash
python main.py --list      # should list all 17 projects
python main.py 1           # should run Binary Search and print "... index 3"
```
