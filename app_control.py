"""Open and close applications by spoken name."""
import os
import subprocess
import time

import psutil
import pyautogui

import config


def open_app(name: str) -> str:
    name = name.lower().strip()

    if name in config.APPS:
        cmd = os.path.expandvars(config.APPS[name])
        try:
            if cmd.startswith("start "):
                os.system(cmd)
            else:
                subprocess.Popen(cmd, shell=True)
            return f"Opening {name}"
        except Exception as e:
            return f"I found {name} in my list but couldn't launch it: {e}"

    # Fallback: use the Windows Start Menu search, which can find
    # literally anything installed, without needing an exact path.
    pyautogui.press("win")
    time.sleep(0.6)
    pyautogui.write(name, interval=0.03)
    time.sleep(0.4)
    pyautogui.press("enter")
    return f"Searching Start Menu for {name}"


def close_app(name: str) -> str:
    name = name.lower().strip()
    process_name = config.PROCESS_ALIASES.get(name, name if name.endswith(".exe") else name + ".exe")

    closed_any = False
    for proc in psutil.process_iter(["name"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() == process_name.lower():
                proc.terminate()
                closed_any = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if closed_any:
        return f"Closing {name}"
    return f"I couldn't find {name} running"
