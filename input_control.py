"""Typing, clicking, and screenshots -- the 'do things for me' tier."""
import time
from datetime import datetime

import pyautogui


def type_text(text: str) -> str:
    pyautogui.write(text, interval=0.02)
    return f"Typed: {text}"


def click() -> str:
    pyautogui.click()
    return "Clicked"

def double_click() -> str:
    pyautogui.doubleClick()
    return "Double clicked"


def scroll_up() -> str:
    pyautogui.scroll(400)
    return "Scrolled up"


def scroll_down() -> str:
    pyautogui.scroll(-400)
    return "Scrolled down"


def take_screenshot() -> str:
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    pyautogui.screenshot(filename)
    return f"Saved screenshot as {filename}"


def switch_window() -> str:
    pyautogui.hotkey("alt", "tab")
    return "Switched window"


def minimize_all() -> str:
    pyautogui.hotkey("win", "d")
    return "Showing desktop"
