#!/usr/bin/env python3
# coding: utf-8
"""Unified launcher for the Simple-Projects collection.

This is a thin, non-invasive dispatcher. It runs each project as a separate
subprocess, so every original script keeps working exactly the same way when
run on its own (e.g. ``python "Calculator.py"``) -- nothing in those files is
modified or imported.

Usage:
    python main.py                 # interactive menu
    python main.py --list          # print the project list and exit
    python main.py --check         # report which projects can run here
    python main.py 2               # launch project #2 directly
    python main.py calculator      # launch by (partial) name directly
    python main.py "Snake Game"    # launch by full name

Projects that need a graphical display, audio hardware, a network connection
or a third-party library are checked up front: if the current environment
can't support one, the launcher prints a friendly note and carries on instead
of crashing with a traceback.
"""

import importlib.util
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Each entry describes one project.
#   name     : human-friendly title (also used for name-based selection)
#   file     : script filename, run as-is in a subprocess
#   desc     : one-line summary shown in the menu
#   requires : third-party / optional modules that must be importable
#   gui      : True if a graphical display is required
#   extra    : short human tags shown next to the name (audio, network, ...)
PROJECTS = [
    {"name": "Binary Search Algorithm", "file": "Binary Search Algorithm.py",
     "desc": "Demo of binary search on a sorted list (runs a built-in example).",
     "requires": [], "gui": False, "extra": []},
    {"name": "Calculator", "file": "Calculator.py",
     "desc": "Command-line calculator: add, subtract, multiply or divide two numbers.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Countdown Timer", "file": "Countdown Timer.py",
     "desc": "Counts down from a number of seconds you enter.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Currency Converter", "file": "Currency Converter.py",
     "desc": "Converts an amount from USD to EUR using a live exchange-rate API.",
     "requires": ["requests"], "gui": False, "extra": ["network"]},
    {"name": "Dice Simulation", "file": "Dice Simulation.py",
     "desc": "Rolls a six-sided die as many times as you ask.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Email Slicer", "file": "Email Slicer.py",
     "desc": "Splits an email address into its username and domain.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Hangman", "file": "Hangman.py",
     "desc": "Classic word-guessing Hangman game in the terminal.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Music Player", "file": "Music Player.py",
     "desc": "Tkinter + pygame GUI player for local .mp3 files.",
     "requires": ["tkinter", "pygame"], "gui": True, "extra": ["audio"]},
    {"name": "Password Generator", "file": "Password Generator.py",
     "desc": "Prints a random 10-character password.",
     "requires": [], "gui": False, "extra": []},
    {"name": "QR Code Generator", "file": "QR Code Generator.py",
     "desc": "Generates and saves a QR code image (qrcode.png).",
     "requires": ["qrcode"], "gui": False, "extra": ["image"]},
    {"name": "Quiz Application", "file": "Quiz Application.py",
     "desc": "Multiple-choice quiz that scores your answers.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Rock Paper Scissors", "file": "Rock Paper Scissors.py",
     "desc": "Play rock-paper-scissors against the computer.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Snake Game", "file": "Snake Game.py",
     "desc": "Arrow-key Snake game in a pygame window.",
     "requires": ["pygame"], "gui": True, "extra": []},
    {"name": "Tic Tac Toe", "file": "Tic Tac Toe.py",
     "desc": "Two-player Tic-Tac-Toe on a 3x3 text board.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Typing Speed Test", "file": "Typing Speed Test.py",
     "desc": "Measures your typing speed in words per minute.",
     "requires": [], "gui": False, "extra": []},
    {"name": "Voice Recorder", "file": "Voice Recorder.py",
     "desc": "Records 5 seconds of microphone audio to output.wav.",
     "requires": ["pyaudio"], "gui": False, "extra": ["microphone"]},
    {"name": "Youtube Downloader", "file": "Youtube Downloader.py",
     "desc": "Downloads a YouTube video by URL.",
     "requires": ["pytube"], "gui": False, "extra": ["network"]},
]

# Most importable names match their pip package; record the exceptions here.
PIP_HINTS = {
    "tkinter": None,  # ships with python; on Linux install the OS Tk package
}


def normalize(text):
    """Lower-case and drop spaces so 'Snake Game' == 'snakegame'."""
    return "".join(text.lower().split())


def find_projects(selector):
    """Return the projects matching a number or (partial) name selector."""
    sel = selector.strip()
    if sel.isdigit():
        index = int(sel)
        if 1 <= index <= len(PROJECTS):
            return [PROJECTS[index - 1]]
        return []

    wanted = normalize(sel)
    if not wanted:
        return []
    exact = [p for p in PROJECTS if normalize(p["name"]) == wanted]
    if exact:
        return exact
    prefix = [p for p in PROJECTS if normalize(p["name"]).startswith(wanted)]
    if prefix:
        return prefix
    return [p for p in PROJECTS if wanted in normalize(p["name"])]


def environment_problems(project):
    """List the reasons (if any) a project can't run in this environment."""
    problems = []
    for module in project["requires"]:
        if importlib.util.find_spec(module) is not None:
            continue
        if module == "tkinter":
            problems.append(
                "missing module 'tkinter' (install your OS Tk package, "
                "e.g. 'sudo apt-get install python3-tk')")
        else:
            pkg = PIP_HINTS.get(module, module)
            problems.append(
                "missing module '%s' (install with: pip install %s)" % (module, pkg))

    if project["gui"] and sys.platform not in ("win32", "darwin"):
        if not os.environ.get("DISPLAY") and not os.environ.get("WAYLAND_DISPLAY"):
            problems.append(
                "no graphical display detected (a desktop session / DISPLAY is required)")
    return problems


def format_tags(project):
    """Build a short ' [GUI, network]' style label for the menu."""
    tags = (["GUI"] if project["gui"] else []) + list(project["extra"])
    return "  [" + ", ".join(tags) + "]" if tags else ""


def launch(project):
    """Run a project as a subprocess, skipping gracefully if unsupported."""
    problems = environment_problems(project)
    if problems:
        print("\n[skip] '%s' can't run in this environment:" % project["name"])
        for problem in problems:
            print("   - " + problem)
        print("   (The other projects still work; this one needs the above first.)")
        return False

    path = os.path.join(BASE_DIR, project["file"])
    if not os.path.isfile(path):
        print("\n[error] file not found: %s" % project["file"])
        return False

    print("\n>>> Launching: %s\n" % project["name"])
    try:
        subprocess.run([sys.executable, path], cwd=BASE_DIR)
    except KeyboardInterrupt:
        print("\n[interrupted] returned from '%s'." % project["name"])
    except Exception as exc:  # keep the launcher alive on any child failure
        print("\n[error] failed to run '%s': %s" % (project["name"], exc))
        return False
    return True


def print_banner():
    print("=" * 60)
    print(" Simple-Projects launcher")
    print(" Pick a project to run; type 'q' any time to quit.")
    print("=" * 60)


def print_menu():
    print("\nAvailable projects:")
    for index, project in enumerate(PROJECTS, 1):
        print("  %2d) %-24s%s" % (index, project["name"], format_tags(project)))
        print("       %s" % project["desc"])


def print_list_plain():
    """Compact one-line-per-project listing for --list."""
    for index, project in enumerate(PROJECTS, 1):
        print("%2d) %s%s" % (index, project["name"], format_tags(project)))


def print_check_report():
    """Report readiness of every project without running anything."""
    print("Environment readiness report:\n")
    for index, project in enumerate(PROJECTS, 1):
        problems = environment_problems(project)
        status = "READY" if not problems else "needs setup"
        print("%2d) %-24s %s" % (index, project["name"], status))
        for problem in problems:
            print("       - " + problem)


def print_cli_help():
    print(__doc__.strip())


def interactive_loop():
    print_banner()
    while True:
        print_menu()
        try:
            choice = input(
                "\nSelect a project (number/name), 'l' to list, 'q' to quit: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return 0

        if not choice:
            print("Please type a number, a name, or 'q' to quit.")
            continue

        lowered = choice.lower()
        if lowered in ("q", "quit", "exit"):
            print("Bye!")
            return 0
        if lowered in ("l", "list", "ls"):
            continue  # menu is reprinted at the top of the loop
        if lowered in ("h", "help", "?"):
            print_cli_help()
            continue

        matches = find_projects(choice)
        if not matches:
            print("No project matches %r. Type 'l' to see the list." % choice)
            continue
        if len(matches) > 1:
            print("Ambiguous %r -- did you mean:" % choice)
            for project in matches:
                print("   - " + project["name"])
            continue

        launch(matches[0])
        try:
            input("\nPress Enter to return to the menu...")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            return 0


def main(argv):
    args = argv[1:]
    if not args:
        return interactive_loop()

    first = args[0].lower()
    if first in ("-h", "--help", "help"):
        print_cli_help()
        return 0
    if first in ("-l", "--list", "list"):
        print_list_plain()
        return 0
    if first in ("--check", "check"):
        print_check_report()
        return 0

    selector = " ".join(args)
    matches = find_projects(selector)
    if not matches:
        print("No project matches %r.\n" % selector)
        print_list_plain()
        return 1
    if len(matches) > 1:
        print("Ambiguous %r -- candidates:" % selector)
        for project in matches:
            print("   - " + project["name"])
        return 1

    return 0 if launch(matches[0]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
