"""
Central configuration for the voice assistant.

APPS: map spoken names -> exact launch command / path.
Anything NOT in this dict still works: the assistant falls back to
searching the Windows Start Menu for the spoken name (types it into
the Start menu and hits Enter), so you don't have to register every
app you own -- only the ones where you want a specific exe/shortcut
or a custom alias (e.g. "code" -> VS Code).

Edit the paths below to match your machine, or just leave the dict
mostly empty and rely on the Start Menu fallback.
"""

WAKE_WORD_MODEL = "hey_jarvis"   # built-in openWakeWord model
WAKE_WORD_THRESHOLD = 0.5        # 0-1, lower = more sensitive (more false triggers)

WHISPER_MODEL_SIZE = "base"      # tiny / base / small -- bigger = more accurate, slower
WHISPER_DEVICE = "cpu"

COMMAND_RECORD_SECONDS = 5        # how long to listen after the wake word fires
SAMPLE_RATE = 16000

TTS_RATE = 175                    # words per minute for the speech output

# spoken name (lowercase) -> command to run.
# Use raw exe paths, or just the exe name if it's on PATH.
APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "code": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "spotify": r"C:\Users\%USERNAME%\AppData\Roaming\Spotify\Spotify.exe",
    "file explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "settings": "start ms-settings:",
}

# spoken name -> the process name Task Manager would show (for closing apps
# that aren't in APPS, add an alias here too)
PROCESS_ALIASES = {
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "notepad": "notepad.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "spotify": "spotify.exe",
    "code": "Code.exe",
    "calculator": "CalculatorApp.exe",
}
