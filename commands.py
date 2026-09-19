"""
Turns a transcribed sentence into an action.

Keyword-based on purpose: it's transparent, easy to extend, and
doesn't need an internet call or an LLM just to know "open chrome"
means open_app("chrome"). Add new phrases/intents here as you find
gaps.
"""
import re

from actions import app_control, system_control, input_control

# (regex pattern, handler) -- checked in order, first match wins.
# Handler receives the regex match object.
_RULES = [
    (r"^open (.+)$", lambda m: app_control.open_app(m.group(1))),
    (r"^launch (.+)$", lambda m: app_control.open_app(m.group(1))),
    (r"^start (.+)$", lambda m: app_control.open_app(m.group(1))),
    (r"^close (.+)$", lambda m: app_control.close_app(m.group(1))),
    (r"^quit (.+)$", lambda m: app_control.close_app(m.group(1))),
    (r"^exit (.+)$", lambda m: app_control.close_app(m.group(1))),

    (r"^shut ?down$", lambda m: system_control.shutdown()),
    (r"^turn off( the computer| the laptop| the pc)?$", lambda m: system_control.shutdown()),
    (r"^restart$", lambda m: system_control.restart()),
    (r"^reboot$", lambda m: system_control.restart()),
    (r"^sleep$", lambda m: system_control.sleep_pc()),
    (r"^lock( the screen)?$", lambda m: system_control.lock()),
    (r"^cancel shutdown$", lambda m: system_control.cancel_shutdown()),

    (r"^volume up$", lambda m: system_control.volume_up()),
    (r"^turn (the )?volume up$", lambda m: system_control.volume_up()),
    (r"^volume down$", lambda m: system_control.volume_down()),
    (r"^turn (the )?volume down$", lambda m: system_control.volume_down()),
    (r"^mute$", lambda m: system_control.mute()),
    (r"^unmute$", lambda m: system_control.unmute()),

    (r"^brightness up$", lambda m: system_control.brightness_up()),
    (r"^brighten( the screen)?$", lambda m: system_control.brightness_up()),
    (r"^brightness down$", lambda m: system_control.brightness_down()),
    (r"^dim( the screen)?$", lambda m: system_control.brightness_down()),

    (r"^type (.+)$", lambda m: input_control.type_text(m.group(1))),
    (r"^click$", lambda m: input_control.click()),
    (r"^double click$", lambda m: input_control.double_click()),
    (r"^scroll up$", lambda m: input_control.scroll_up()),
    (r"^scroll down$", lambda m: input_control.scroll_down()),
    (r"^screenshot$", lambda m: input_control.take_screenshot()),
    (r"^take a screenshot$", lambda m: input_control.take_screenshot()),
    (r"^switch window$", lambda m: input_control.switch_window()),
    (r"^show desktop$", lambda m: input_control.minimize_all()),
    (r"^minimize everything$", lambda m: input_control.minimize_all()),
]


def handle(text: str) -> str:
    text = text.lower().strip().rstrip(".")
    if not text:
        return "I didn't catch that"

    for pattern, handler in _RULES:
        match = re.match(pattern, text)
        if match:
            try:
                return handler(match)
            except Exception as e:
                return f"That failed: {e}"

    return f"I don't have a command for '{text}' yet"
