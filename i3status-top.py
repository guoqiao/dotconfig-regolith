#!/usr/bin/env python3
from i3pystatus import Status

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
    command="curl https://api.exchangeratesapi.io/latest?base=NZD | jq '.rates.CNY' | cut -c1-4",
    format='NZD/CNY: {output}',
    on_leftclick='google-chrome https://api.exchangeratesapi.io/latest?base=NZD',
    interval=3600,
)


status.run()
