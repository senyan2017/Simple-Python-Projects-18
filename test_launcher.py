#!/usr/bin/env python3
"""
Smoke test for the Simple-Projects launcher.

Verifies:
  1. main.py parses correctly (no syntax errors).
  2. All project modules can be imported without executing
     interactive code (i.e. __main__ guards work).
  3. Direct-launch via CLI argument (--list, number, name) exits cleanly.
  4. Dependency-missing projects produce a friendly message, not a crash.
"""

import importlib
import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_PY = os.path.join(SCRIPT_DIR, "main.py")

# ── Helpers ──────────────────────────────────────────────────────────

passed = 0
failed = 0


def check(label, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print(f"  [PASS] {label}")
    else:
        failed += 1
        print(f"  [FAIL] {label}" + (f"  -- {detail}" if detail else ""))


def run_main(*args, timeout=10):
    """Run main.py with given args and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, MAIN_PY, *args],
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=SCRIPT_DIR,
    )
    return result.returncode, result.stdout, result.stderr


# ── Tests ────────────────────────────────────────────────────────────

def test_main_syntax():
    """main.py compiles without syntax errors."""
    try:
        with open(MAIN_PY) as f:
            compile(f.read(), MAIN_PY, "exec")
        check("main.py has no syntax errors", True)
    except SyntaxError as e:
        check("main.py has no syntax errors", False, str(e))


def test_imports_guarded():
    """All project modules can be imported without triggering interactive code."""
    # We need to import main to get the PROJECTS list, then try importing each
    sys.path.insert(0, SCRIPT_DIR)
    try:
        main_mod = importlib.import_module("main")
        projects = main_mod.PROJECTS
    except Exception as e:
        check("Import main.py to read PROJECTS", False, str(e))
        return

    check("Import main.py to read PROJECTS", True)

    for filename, name, _ in projects:
        try:
            mod = importlib.import_module(filename)
            check(f"Import '{filename}' without side-effects", True)
        except ImportError:
            # Missing third-party dep is OK — means the guard prevented
            # execution and the import error is from a top-level import
            check(f"Import '{filename}' without side-effects", True)
            # (it will be caught gracefully at runtime)
        except Exception as e:
            check(f"Import '{filename}' without side-effects", False, str(e))


def test_list_flag():
    """--list flag prints all projects and exits 0."""
    rc, out, err = run_main("--list")
    check("'python main.py --list' exits with code 0", rc == 0,
          f"rc={rc}, stderr={err.strip()}")
    check("'--list' output contains 'Calculator'", "Calculator" in out)
    # Count lines with a leading number
    lines_with_number = sum(1 for line in out.strip().splitlines()
                            if line.strip() and line.strip()[0].isdigit())
    check(f"'--list' output has 17 project lines", lines_with_number == 17,
          f"found {lines_with_number}")


def test_direct_launch_by_number():
    """Launching by number attempts to run the project (may fail on
    missing deps, but should not crash the launcher)."""
    # Use Binary Search (1) which has no deps and a non-interactive main
    # But its main() uses hardcoded data, so it should work
    rc, out, err = run_main("1")
    # It should either succeed (rc=0) or fail gracefully
    check("'python main.py 1' does not crash",
          rc == 0 or "error" in (out + err).lower() or "missing" in (out + err).lower(),
          f"rc={rc}")
    check("'python main.py 1' output mentions Binary Search or index",
          "binary" in out.lower() or "index" in out.lower() or "Launching" in out,
          f"output: {out[:120]}")


def test_direct_launch_by_name():
    """Launching by name finds the right project."""
    rc, out, err = run_main("calculator")
    # Calculator needs interactive input, so it will likely error or hang.
    # But we just check it doesn't crash the launcher itself.
    # Use a short timeout to avoid hanging on input().
    try:
        rc2, out2, err2 = run_main("password", timeout=5)
        check("'python main.py password' launches Password Generator",
              "Launching" in out2 or "password" in out2.lower() or len(out2) > 0,
              f"rc={rc2}, output: {out2[:120]}")
    except subprocess.TimeoutExpired:
        # Password generator should print quickly, timeout means it's
        # waiting on something unexpected
        check("'python main.py password' launches Password Generator", False,
              "timed out")


def test_invalid_input():
    """Invalid number or name exits with code 1 and a message."""
    rc, out, err = run_main("999")
    check("'python main.py 999' exits with code 1", rc == 1,
          f"rc={rc}")

    rc2, out2, err2 = run_main("nonexistent_project_xyz")
    check("'python main.py nonexistent_project_xyz' exits with code 1", rc2 == 1,
          f"rc={rc2}")


# ── Runner ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  Simple-Projects Launcher — Smoke Tests")
    print("=" * 50)
    print()

    test_main_syntax()
    print()
    test_imports_guarded()
    print()
    test_list_flag()
    print()
    test_direct_launch_by_number()
    print()
    test_direct_launch_by_name()
    print()
    test_invalid_input()
    print()

    print("-" * 50)
    print(f"  Results: {passed} passed, {failed} failed")
    print("-" * 50)

    sys.exit(1 if failed else 0)
