"""
Always-on wake word listener using openWakeWord.

Runs a tiny model continuously on the mic stream (cheap on CPU),
and returns control the moment "hey jarvis" (or whichever model you
configure) is detected -- at which point main.py switches to full
recording + Whisper transcription for the actual command.
"""
import numpy as np
import sounddevice as sd
from openwakeword.model import Model

import config


class WakeWordListener:
    def __init__(self):
        self.model = Model(wakeword_models=[config.WAKE_WORD_MODEL])
        self.frame_size = 1280  # openWakeWord expects 80ms chunks @ 16kHz

    def listen_for_wake_word(self):
        """Blocks until the wake word is heard, then returns."""
        triggered = False

        def callback(indata, frames, time_info, status):
            nonlocal triggered
            if triggered:
                return
            audio = np.frombuffer(indata, dtype=np.int16)
            prediction = self.model.predict(audio)
            score = prediction.get(config.WAKE_WORD_MODEL, 0)
            if score > config.WAKE_WORD_THRESHOLD:
                triggered = True

        with sd.InputStream(
            samplerate=config.SAMPLE_RATE,
            blocksize=self.frame_size,
            dtype="int16",
            channels=1,
            callback=callback,
        ):
            while not triggered:
                sd.sleep(50)
