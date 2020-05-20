#!/usr/bin/env python3
from i3pystatus import Status

status = Status()

status.register(
    "text",
    text='',
    on_leftclick='gnome-session-quit --power-off',
)

status.register(
    "text",
    text='',
    on_leftclick='gnome-session-quit --logout',
)

status.register(
    "text",
    text='',
    on_leftclick='systemctl suspend',
)


status.register(
    "text",
    text='',
    on_leftclick='gnome-control-center info-overview',
)

status.register(
    "text",
    text='',
    on_leftclick='gnome-control-center',
)

status.register(
    "text",
    text='',
    on_leftclick='gnome-screenshot --interactive --area',
)

status.register(
    "text",
    text='',
    on_leftclick='gnome-calculator',
)

status.register(
    "text",
    text='',
    on_leftclick='gnome-clocks',
)

# refer to /usr/share/zoneinfo for tz
status.register(
    "clock",
    format=[
        #  ("%m-%d %a %H:%M:%S %Z", "NZ"),
        ("%d %a %H:%M:%S %Z", "NZ"),
        ("%d %a %H:%M %Z", "Asia/Shanghai"),
        ("%d %a %H:%M %Z", "UTC"),
    ],
    on_leftclick='gnome-control-center datetime',
)

status.register(
    "weekcal",
    interval=60,
    startofweek=0,  # 0 = Monday, 6 = Sunday
    prefixformat=' %Y %B',  # Feb
    suffixformat='%A',  # Sat
    todayhighlight=[' [', '] '],
    on_leftclick='gnome-calendar',
)

status.run()
