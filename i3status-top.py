#!/usr/bin/env python3
from pathlib import Path
from i3pystatus import Status

HERE = Path(__file__).absolute().parent

status = Status()

# refer to /usr/share/zoneinfo for tz
status.register(
    "clock",
    format=[
        ("%d %a %H:%M %Z", "UTC"),
        ("%d %a %H:%M %Z", "Asia/Shanghai"),
        ("%d %a %H:%M:%S %Z", "NZ"),
    ],
    on_leftclick='gnome-control-center datetime',
)

status.register(
    'shell',
    command=str(HERE/'status.py'),
    format='{output}',
    interval=3600,
)

status.run()
