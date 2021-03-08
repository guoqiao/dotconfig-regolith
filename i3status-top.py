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
    on_leftclick='baobab',  # Disk Usage Analyzer
)

status.register(
    "mem",
    format='📈{used_mem}G',
    divisor=1024 * 1024 * 1024,
)

status.register(
    "load",
    format='🔥{avg1} {avg5} {avg15}',
    on_leftclick='/snap/bin/gnome-system-monitor --show-processes-tab',
)

# status.register(
#     'shell',
#     command='sensors | grep fan | cut -d: -f2 | tr -d " "',
#     format='{output}',
#     on_leftclick='/snap/bin/gnome-system-monitor --show-processes-tab',
# )

status.register(
    "temp",
    format="🌡️{temp:.0f}°C",
)

status.register(
    "uptime",
    format='⏳{days}d{hours}h',
)

status.register(
    "bitcoin",
    interval=3600,
)

# status.register('shell', command=str(HERE/'status.py'), format='{output}', interval=600)

status.run()
