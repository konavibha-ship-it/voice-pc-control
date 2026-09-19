"""Records a short clip after the wake word and transcribes it offline."""
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

import config


class Transcriber:
    def __init__(self):
        self.model = WhisperModel(
            config.WHISPER_MODEL_SIZE,
            device=config.WHISPER_DEVICE,
            compute_type="int8",
        )

    def record_and_transcribe(self) -> str:
        print("[listening for command...]")
        audio = sd.rec(
            int(config.COMMAND_RECORD_SECONDS * config.SAMPLE_RATE),
            samplerate=config.SAMPLE_RATE,
            channels=1,
            dtype="float32",
        )
        sd.wait()
        audio = np.squeeze(audio)

        segments, _ = self.model.transcribe(audio, language="en")
        text = " ".join(seg.text for seg in segments).strip()
        print(f"[heard] {text}")
        return text
