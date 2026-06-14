#!/usr/bin/env python3
# coding: utf-8
"""Minimal, non-interactive verification for the Simple-Projects launcher.

Run with:  python verify.py

It checks three things without needing any user input:
  1. the project registry is well-formed (every script file exists, names unique);
  2. the selector resolver maps numbers and (partial) names correctly;
  3. the real CLI works end to end -- '--list', '--check', an unknown
     selector, and a genuine direct launch of a safe, dependency-free project.

Exits 0 only if every check passes; prints a PASS/FAIL line per check.
"""

import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import main as launcher  # noqa: E402  (path set above)

MAIN_PY = os.path.join(BASE_DIR, "main.py")
_failures = []


def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    line = "[%s] %s" % (status, label)
    if detail:
        line += " -- " + detail
    print(line)
    if not condition:
        _failures.append(label)


def run_cli(*cli_args):
    """Run main.py with given args, no stdin, return (returncode, output)."""
    proc = subprocess.run(
        [sys.executable, MAIN_PY, *cli_args],
        cwd=BASE_DIR, stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, timeout=30)
    return proc.returncode, proc.stdout


# 1) Registry integrity --------------------------------------------------------
names = [p["name"] for p in launcher.PROJECTS]
check("registry: at least 10 projects", len(launcher.PROJECTS) >= 10,
      "%d found" % len(launcher.PROJECTS))
check("registry: names are unique", len(names) == len(set(names)))
missing = [p["file"] for p in launcher.PROJECTS
           if not os.path.isfile(os.path.join(BASE_DIR, p["file"]))]
check("registry: every script file exists", not missing,
      ("missing: %s" % missing) if missing else "all present")
bad_keys = [p["name"] for p in launcher.PROJECTS
            if not {"name", "file", "desc", "requires", "gui", "extra"} <= set(p)]
check("registry: every entry has required keys", not bad_keys,
      ("bad: %s" % bad_keys) if bad_keys else "ok")

# 2) Selector resolver ---------------------------------------------------------
check("resolve: number '1' -> first project",
      launcher.find_projects("1") == [launcher.PROJECTS[0]])
check("resolve: exact name (case-insensitive)",
      launcher.find_projects("snake game") == [
          p for p in launcher.PROJECTS if p["name"] == "Snake Game"])
check("resolve: space-insensitive name 'snakegame'",
      [p["name"] for p in launcher.find_projects("snakegame")] == ["Snake Game"])
check("resolve: unique partial 'calc' -> Calculator",
      [p["name"] for p in launcher.find_projects("calc")] == ["Calculator"])
check("resolve: out-of-range number '999' -> no match",
      launcher.find_projects("999") == [])
check("resolve: nonsense 'zzz' -> no match",
      launcher.find_projects("zzz") == [])
check("resolve: ambiguous 'c' -> multiple matches",
      len(launcher.find_projects("c")) > 1)

# 3) Environment checks (deterministic part) -----------------------------------
stdlib_project = next(p for p in launcher.PROJECTS
                      if not p["requires"] and not p["gui"])
check("env: dependency-free project has no problems",
      launcher.environment_problems(stdlib_project) == [],
      stdlib_project["name"])

# 4) Real CLI, end to end ------------------------------------------------------
rc, out = run_cli("--list")
check("cli: --list exits 0 and lists all projects",
      rc == 0 and all(n in out for n in names), "rc=%d" % rc)

rc, out = run_cli("--check")
check("cli: --check exits 0", rc == 0, "rc=%d" % rc)

rc, out = run_cli("nope-not-a-project")
check("cli: unknown selector exits non-zero", rc != 0, "rc=%d" % rc)

# Direct launch of a safe, no-input, no-dependency project (#1 Binary Search).
rc, out = run_cli("1")
check("cli: direct launch by number runs the project",
      rc == 0 and "index 3" in out, "rc=%d" % rc)

rc, out = run_cli("binary")
check("cli: direct launch by partial name runs the project",
      rc == 0 and "index 3" in out, "rc=%d" % rc)

# Summary ----------------------------------------------------------------------
print("-" * 50)
if _failures:
    print("RESULT: FAIL (%d) -> %s" % (len(_failures), ", ".join(_failures)))
    sys.exit(1)
print("RESULT: PASS (all checks green)")
sys.exit(0)
