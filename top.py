#!/usr/bin/env python3
from pathlib import Path
from i3pystatus import Status

HERE = Path(__file__).absolute().parent

status = Status()

# refer to /usr/share/zoneinfo for tz
status.register(
    "clock",
    format=[
        ("🇳🇿%Z %m.%d %a %H:%M:%S", "NZ"),
    ],
    on_rightclick='gnome-control-center datetime',
)

status.register(
    "clock",
    format=[
        ("🇨🇳%Z %d %a %H:%M", "Asia/Shanghai"),
    ],
    on_rightclick='gnome-control-center datetime',
)

status.register(
    "clock",
    format=[
        ("🌎%Z %d %a %H:%M", "UTC"),
    ],
    on_rightclick='gnome-control-center datetime',
)


status.register(
    "disk",
    path="/",
    format="💽{used:.0f}G",
    on_rightclick='baobab',  # Disk Usage Analyzer
)

status.register(
    "mem",
    format='📈{used_mem}G',
    divisor=1024 * 1024 * 1024,
    on_rightclick='gnome-system-monitor --show-processes-tab',
)

status.register(
    "load",
    format='🔥{avg1} {avg5} {avg15}',
    on_rightclick='gnome-system-monitor --show-processes-tab',
)

status.register(
    'shell',
    command='sensors | grep "Package" | cut -d" " -f5',
    format='🌡️{output}',
    on_rightclick='gnome-system-monitor --show-processes-tab',
)

status.register(
    "uptime",
    format='⏳{days}d{hours}h',
)

# status.register('shell', command=str(HERE/'status.py'), format='{output}', interval=600)

status.run()
