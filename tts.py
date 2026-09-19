"""Offline text-to-speech feedback so the assistant can talk back."""
import pyttsx3
import config


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", config.TTS_RATE)

    def say(self, text: str):
        print(f"[assistant] {text}")
        self.engine.say(text)
        self.engine.runAndWait()
