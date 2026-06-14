"""
Pure countdown logic — separated from I/O for reuse and testing.
"""

import time


def countdown(total_seconds, tick=1):
    """
    Count down from `total_seconds` to zero, printing each remaining second.

    Parameters
    ----------
    total_seconds : int
        Starting value (must be > 0).
    tick : float
        Seconds to sleep between ticks (default 1).
    """
    remaining = total_seconds
    while remaining > 0:
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(tick)
        remaining -= 1
    print("Timer completed!")
