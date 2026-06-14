# Simple-Projects
Python projects for beginners

## How to run

Every script still runs on its own, just like before. For example:

    python "Calculator.py"
    python "Password Generator.py"
    python "Quiz Application.py"
    python "Tic Tac Toe.py"

## Project layout

The reusable logic for the scripts above lives in the `core/` package
(`calculator`, `password`, `quiz`, `tic_tac_toe`), with shared input helpers in
`core/cli_helpers.py`. Importing those modules has no side effects, so the logic
can be reused or tested on its own. Quiz questions and default settings sit next
to their logic in `core/` rather than inside the run flow, so they are easy to
change. The scripts in the root just handle the command-line interaction.

Run the tests with:

    python -m unittest discover

### 1) Binary Search Algorithm



### 2) Calculator



### 3) Countdown Timer



### 4) Currency Converter



### 5) Dice Simulation




### 6) Email Slicer






### 7) Hangman





### 8) Music Player






### 9) Password Generator






### 10) QR Code Generator





### 11) Quiz Application







### 12) Rock Paper Scissors






### 13) Snake Game






### 14) Tic Tac Toe






### 15) Typing Speed Test






### 16) Voice Recorder






### 17) Youtube Downloader
