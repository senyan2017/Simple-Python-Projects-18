#!/usr/bin/env python3
"""
Simple-Projects Launcher
========================
Unified entry point for all mini-projects in this repository.

Usage:
    python main.py              # interactive menu
    python main.py <number>     # launch by number  (e.g. python main.py 2)
    python main.py <name>       # launch by name    (e.g. python main.py calculator)
    python main.py --list       # list all projects and exit
"""

import importlib
import os
import sys
import subprocess

# ── Project registry ────────────────────────────────────────────────
# (filename_without_extension, display_name, short_description)
PROJECTS = [
    ("Binary Search Algorithm", "Binary Search",       "Search a sorted list using binary search"),
    ("Calculator",              "Calculator",           "Basic arithmetic: add, subtract, multiply, divide"),
    ("Countdown Timer",         "Countdown Timer",     "Count down from a given number of seconds"),
    ("Currency Converter",      "Currency Converter",  "Convert between currencies via exchange-rate API"),
    ("Dice Simulation",         "Dice Roll",           "Simulate rolling one or more dice"),
    ("Email Slicer",            "Email Slicer",        "Split an email address into username and domain"),
    ("Hangman",                 "Hangman",             "Classic word-guessing game"),
    ("Music Player",            "Music Player",        "Play MP3 files (requires GUI + pygame)"),
    ("Password Generator",      "Password Generator",  "Generate a random secure password"),
    ("QR Code Generator",       "QR Code Generator",   "Create a QR code image from any data"),
    ("Quiz Application",        "Quiz",                "Answer multiple-choice trivia questions"),
    ("Rock Paper Scissors",     "Rock Paper Scissors", "Play rock-paper-scissors against the computer"),
    ("Snake Game",              "Snake Game",          "Classic snake game (requires GUI + pygame)"),
    ("Tic Tac Toe",             "Tic Tac Toe",         "Two-player tic-tac-toe in the terminal"),
    ("Typing Speed Test",       "Typing Speed Test",   "Measure your typing speed (WPM)"),
    ("Voice Recorder",          "Voice Recorder",      "Record audio from microphone (requires pyaudio)"),
    ("Youtube Downloader",      "YouTube Downloader",  "Download YouTube videos (requires pytube)"),
]


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    """Print the project menu."""
    print("=" * 56)
    print("       Simple-Projects Launcher")
    print("=" * 56)
    print()
    for i, (_, name, desc) in enumerate(PROJECTS, 1):
        print(f"  {i:>2}. {name:<22} - {desc}")
    print()
    print("  Type a number or name to launch, 'q' to quit.")
    print("-" * 56)


def find_project(query):
    """Find a project by 1-based index or case-insensitive name substring."""
    # Try as number
    try:
        idx = int(query)
        if 1 <= idx <= len(PROJECTS):
            return idx - 1
    except ValueError:
        pass

    # Try as name (case-insensitive substring match)
    q = query.lower()
    matches = [
        i for i, (fname, name, _) in enumerate(PROJECTS)
        if q in fname.lower() or q in name.lower()
    ]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        print(f"\n  Ambiguous — matched {len(matches)} projects:")
        for m in matches:
            print(f"    {m + 1}. {PROJECTS[m][1]}")
        return None

    print(f"\n  No project matching '{query}'.")
    return None


def run_project(idx):
    """Import and run a project by index, with dependency/error handling."""
    filename, name, _ = PROJECTS[idx]
    module_name = filename  # Python resolves filenames with spaces as module names

    clear_screen()
    print(f">>> Launching: {name}")
    print("-" * 56)

    try:
        mod = importlib.import_module(module_name)
        fn = getattr(mod, "main", None)
        if callable(fn):
            fn()
            return
        # Fallback: if the module was successfully imported but has no
        # callable entry point (shouldn't happen after our refactor)
        print(f"  [!] '{name}' loaded but no entry point found.")

    except ImportError as e:
        missing = _extract_missing_package(e)
        print(f"\n  [!] Missing dependency: {missing}")
        print(f"      Install it with:  pip install {missing}")
        print(f"      Then try again.")

    except (SystemExit, KeyboardInterrupt):
        pass  # user quit or Ctrl-C inside the project

    except Exception as e:
        print(f"\n  [!] '{name}' encountered an error: {e}")


def _extract_missing_package(exc):
    """Best-effort extraction of the missing package name from an ImportError."""
    msg = str(exc)
    # "No module named 'xxx'"
    if "No module named" in msg:
        name = msg.split("'")[1] if "'" in msg else msg.split()[-1]
        # Top-level package only
        return name.split(".")[0]
    return msg


def list_projects():
    """Print a plain list of all projects (for scripting / piping)."""
    for i, (_, name, desc) in enumerate(PROJECTS, 1):
        print(f"{i:>2}. {name} — {desc}")


def interactive_menu():
    """Run the interactive menu loop."""
    while True:
        show_menu()
        try:
            choice = input("  > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye!")
            break

        if not choice:
            continue
        if choice.lower() in ("q", "quit", "exit"):
            print("  Goodbye!")
            break

        idx = find_project(choice)
        if idx is not None:
            run_project(idx)
            print()
            input("  Press Enter to return to menu...")
            clear_screen()


# ── Entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ("--list", "-l"):
            list_projects()
        else:
            idx = find_project(arg)
            if idx is not None:
                run_project(idx)
            else:
                sys.exit(1)
    else:
        interactive_menu()
