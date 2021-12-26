#!/usr/bin/env python3

from os.path import abspath, dirname, join
import argparse
from i3pystatus import Status

HERE = abspath(dirname(__file__))

# https://fontawesome.com/v4.7/cheatsheet/
FONT_AWESOME = {
    "poweroff": "",
    "lock": "",
    "screenshot": "",
    "note": "",
    "bluetooth": "",
    "sound": "",
    "sleep": "",
    "logout": "",
    "settings": "",
}


EMOJI = {
}


ICON = FONT_AWESOME


def icon(name):
    return ICON.get(name, "")


parser = argparse.ArgumentParser(
    "i3pystatus bar",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description="i3pystatus bar",
)

parser.add_argument(
    "-m",
    "--mode",
    dest="mode",
    choices=["top", "bottom", "one"],
    default="one",
    help="status bar mode"
)

args = parser.parse_args()
mode = args.mode
status = Status()

if mode in ["one", "bottom"]:

    status.register(
        "text",
        text=icon("poweroff"),
        on_leftclick='gnome-session-quit --power-off',
    )

    status.register(
        "text",
        text=icon("lock"),
        on_leftclick='gnome-screensaver-command --lock',
    )

    status.register(
        "text",
        text=icon("sleep"),
        on_leftclick='systemctl suspend',
    )

    status.register(
        "text",
        text=icon("logout"),
        on_leftclick='gnome-session-quit --logout',
    )

    status.register(
        "text",
        text=icon("settings"),
        on_leftclick='gnome-control-center',
    )

    status.register(
        "text",
        text=icon("sound"),
        on_leftclick='gnome-control-center sound',
        on_rightclick='pavucontrol',
    )

    status.register(
        "bluetooth",
        format="{}".format(icon("bluetooth")),
        show_disconnected=True,
        on_leftclick='gnome-control-center bluetooth',
    )

    status.register(
        "text",
        text=icon("screenshot"),
        on_leftclick='/usr/bin/flameshot gui',
        on_rightclick='/usr/bin/flameshot config',
    )

    status.register(
        "text",
        text=icon("note"),
        on_leftclick='code -n ~/note.md',
        on_rightclick='code -n ~/note.md',
    )

if mode in ["one", "top"]:

    # refer to /usr/share/zoneinfo for tz
    status.register(
        "clock",
        format=[
            ("🇳🇿%m-%d %H:%M:%S %a", "NZ"),
        ],
        color="#00FF00",
        on_rightclick='gnome-control-center datetime',
    )

    status.register(
        "clock",
        format=[
            ("🇨🇳%d %H:%M", "Asia/Shanghai"),
        ],
        on_rightclick='gnome-control-center datetime',
    )

    status.register(
        "clock",
        format=[
            ("🌎%d %H:%M", "UTC"),
        ],
        on_rightclick='gnome-control-center datetime',
    )

    status.register(
        'shell',
        command='sensors | grep "Package" | cut -d" " -f5',
        format='{output}',
        on_rightclick='gnome-system-monitor --show-processes-tab',
    )

    status.register(
        "mem",
        format='{used_mem}G',
        divisor=1024 * 1024 * 1024,
        on_rightclick='gnome-system-monitor --show-processes-tab',
    )

    status.register(
       "load",
       format='{avg1} {avg5} {avg15}',
       on_rightclick='gnome-system-monitor --show-processes-tab',
    )

    status.register(
        "disk",
        path="/",
        format="{used:.0f}G",
        on_rightclick='baobab',  # Disk Usage Analyzer
    )

    status.register(
        "uptime",
        format='{days}d{hours}h',
    )

    status.register(
        "network",
        detect_active=True,
        interval=5,
        auto_units=True,
        format_up="{essid} {bytes_recv:>5}",
        on_leftclick='gnome-control-center wifi',
        on_rightclick='nm-connection-editor',
    )

    status.register(
        'shell',
        command='nmcli -t connection show --active | grep -i vpn | cut -d: -f1',  # noqa
        format='{output}',
        on_leftclick='gnome-control-center network',  # vpn is in network panel
        on_rightclick='nm-connection-editor',
    )
    status.register(
        'shell',
        interval=60,
        command=join(HERE, 'stock.py'),
        format='{output}',
        on_leftclick='google-chrome https://www.binance.com/zh-CN/markets',
    )
    status.register(
        'shell',
        interval=2,
        command='(xclip -o 2> /dev/null || echo ".") | cut -c 1-20',
        format='{output}',
    )


status.run()
