"""
Voice PC Control -- main loop.

Say "hey jarvis" (configurable in config.py), wait for the beep-less
listen window, then say a command like "open chrome" or "shut down".

Runs fully offline: wake word (openWakeWord), speech-to-text
(faster-whisper), and text-to-speech (pyttsx3) all run locally --
nothing is sent anywhere.
"""
import commands
from tts import Speaker
from stt import Transcriber
from wake_word import WakeWordListener


def main():
    speaker = Speaker()
    print("Loading models (wake word + whisper)... this can take a few seconds")
    listener = WakeWordListener()
    transcriber = Transcriber()

    speaker.say("Voice control is ready")

    while True:
        listener.listen_for_wake_word()
        speaker.say("Yes?")
        text = transcriber.record_and_transcribe()
        if not text:
            speaker.say("I didn't hear anything")
            continue

        response = commands.handle(text)
        speaker.say(response)


if __name__ == "__main__":
    main()
