import subprocess
from pathlib import Path

from libqtile import hook
from groups import groups
from keys import keys
from layouts import layouts
from mouse import mouse
from screens import screens

# @hook.subscribe.startup_once
# def autostart():
#     subprocess.call(Path(__file__).parent / "autostart.sh")


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
wmname = "LG3D"
