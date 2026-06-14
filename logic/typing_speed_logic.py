"""
Pure typing-speed calculation logic.

No I/O — the timing and input collection happen in the runner script.
"""

DEFAULT_SENTENCE = "The quick brown fox jumps over the lazy dog."


def calculate_wpm(text, elapsed_seconds):
    """
    Return typing speed in words per minute.

    A "word" is any whitespace-separated token, matching the original script.
    """
    if elapsed_seconds <= 0:
        return 0.0
    words = len(text.split())
    return words / elapsed_seconds * 60


def calculate_accuracy(typed_text, reference_text):
    """
    Return character-level accuracy as a float between 0.0 and 1.0.

    Compares the typed text against the reference character by character;
    extra or missing characters count as mismatches.
    """
    if not reference_text:
        return 0.0
    matches = sum(a == b for a, b in zip(typed_text, reference_text))
    return matches / max(len(typed_text), len(reference_text))
