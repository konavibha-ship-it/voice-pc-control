# Voice PC Control

Say "hey jarvis", then a command — it opens/closes apps, controls system
power, volume, brightness, and can type/click for you. Runs 100% offline
on Windows: nothing is sent to the cloud.

## Setup

1. Install Python 3.10 or 3.11 (64-bit) from python.org if you don't have it.
2. Open PowerShell in this folder and install dependencies:
   ```
   pip install -r requirements.txt
   ```
   If `pyautogui` or `pycaw` fail to install, run PowerShell as Administrator
   and try again.
3. Run it:
   ```
   python main.py
   ```
   The first run downloads the wake-word and Whisper models (small, a few
   hundred MB total) — after that it's fully offline.

## Using it

1. Say **"hey jarvis"**. It'll respond "Yes?"
2. Within 5 seconds, say your command, e.g.:
   - "open chrome" / "open notepad" / "open spotify"
   - "close chrome"
   - "shut down" / "restart" / "sleep" / "lock"
   - "volume up" / "volume down" / "mute"
   - "brightness up" / "brightness down"
   - "type hello world"
   - "click" / "double click" / "scroll up" / "scroll down"
   - "screenshot" / "switch window" / "show desktop"

## Customizing

- **`config.py`** — add exact paths for apps you want launched precisely
  (edit the `APPS` dict). Anything you *don't* add still works — it falls
  back to searching the Windows Start Menu for whatever name you say.
- **`commands.py`** — add new phrases/intents here. Each rule is just a
  regex pattern mapped to a function; copy an existing line and change it.
- **`config.WAKE_WORD_THRESHOLD`** — lower it if the wake word isn't
  triggering, raise it if it triggers too often from background noise.
- Want a different wake phrase than "hey jarvis"? openWakeWord ships a
  few other built-in models (e.g. "alexa", "hey_mycroft") — swap the name
  in `config.WAKE_WORD_MODEL`. A fully custom phrase requires training
  your own model with openWakeWord's training notebook (linked in their repo).

## Notes & safety

- `shutdown` and `restart` have a 5-second grace period — say **"cancel
  shutdown"** in that window to abort.
- Run your terminal as Administrator if system actions (volume, brightness,
  shutdown) get blocked by Windows permissions.
- Since this can type and click on your behalf, keep the window it's
  controlling in mind — it acts on whatever currently has focus.
