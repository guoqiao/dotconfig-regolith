#!/usr/bin/env python3

import argparse
from i3pystatus import Status

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
        text='💀',
        on_leftclick='gnome-session-quit --power-off',
    )

    status.register(
        "text",
        text='🔓',
        on_leftclick='gnome-screensaver-command --lock',
    )

    status.register(
        "text",
        text='😴',
        on_leftclick='systemctl suspend',
    )

    status.register(
        "text",
        text='👋',
        on_leftclick='gnome-session-quit --logout',
    )

    status.register(
        "text",
        text='⚙️',
        on_leftclick='gnome-control-center',
    )

    status.register(
        "text",
        text='🔊',
        on_leftclick='gnome-control-center sound',
        on_rightclick='pavucontrol',
    )

    status.register(
        "text",
        text='📸',
        on_leftclick='/usr/bin/flameshot gui',
        on_rightclick='/usr/bin/flameshot config',
    )

    # status.register(
    #     "bluetooth",
    #     format='🎧{name}',
    #     show_disconnected=True,
    #     on_leftclick='gnome-control-center bluetooth',
    # )

if mode in ["one", "top"]:

    # refer to /usr/share/zoneinfo for tz
    status.register(
        "clock",
        format=[
            ("🇳🇿%m-%d %H:%M:%S %a", "NZ"),
        ],
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
        format='🌡️{output}',
        on_rightclick='gnome-system-monitor --show-processes-tab',
    )

    status.register(
        "mem",
        format='📈{used_mem}G',
        divisor=1024 * 1024 * 1024,
        on_rightclick='gnome-system-monitor --show-processes-tab',
    )

    # status.register(
    #     "load",
    #     format='🔥{avg1} {avg5} {avg15}',
    #     on_rightclick='gnome-system-monitor --show-processes-tab',
    # )

    status.register(
        "disk",
        path="/",
        format="💽{used:.0f}G",
        on_rightclick='baobab',  # Disk Usage Analyzer
    )

    status.register(
        "uptime",
        format='⏳{days}d{hours}h',
    )

    status.register(
        "network",
        detect_active=True,
        interval=5,
        auto_units=True,
        format_up="📶{essid} {bytes_recv:>5}",
        on_leftclick='gnome-control-center wifi',
        on_rightclick='nm-connection-editor',
    )

    status.register(
        'shell',
        command='nmcli -t connection show --active | grep -i vpn | cut -d: -f1',  # noqa
        format='👻{output}',
        on_leftclick='gnome-control-center network',  # vpn is in network panel
        on_rightclick='nm-connection-editor',
    )



status.run()
