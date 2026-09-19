"""Power state, volume, and brightness control."""
import os

import screen_brightness_control as sbc
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def _get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))


def shutdown() -> str:
    os.system("shutdown /s /t 5")
    return "Shutting down in 5 seconds"


def restart() -> str:
    os.system("shutdown /r /t 5")
    return "Restarting in 5 seconds"


def sleep_pc() -> str:
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    return "Going to sleep"


def lock() -> str:
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locking the screen"


def cancel_shutdown() -> str:
    os.system("shutdown /a")
    return "Cancelled the scheduled shutdown"


def volume_up() -> str:
    vol = _get_volume_interface()
    current = vol.GetMasterVolumeLevelScalar()
    vol.SetMasterVolumeLevelScalar(min(1.0, current + 0.1), None)
    return "Volume up"


def volume_down() -> str:
    vol = _get_volume_interface()
    current = vol.GetMasterVolumeLevelScalar()
    vol.SetMasterVolumeLevelScalar(max(0.0, current - 0.1), None)
    return "Volume down"


def mute() -> str:
    vol = _get_volume_interface()
    vol.SetMute(1, None)
    return "Muted"


def unmute() -> str:
    vol = _get_volume_interface()
    vol.SetMute(0, None)
    return "Unmuted"


def brightness_up() -> str:
    current = sbc.get_brightness()[0]
    sbc.set_brightness(min(100, current + 15))
    return "Brightness up"


def brightness_down() -> str:
    current = sbc.get_brightness()[0]
    sbc.set_brightness(max(0, current - 15))
    return "Brightness down"
