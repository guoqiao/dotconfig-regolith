#!/usr/bin/env python3
from i3pystatus import Status
from i3pystatus.weather import weathercom

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

status.register(
    'weather',
    format='{city} {condition} {current_temp}{temp_unit}[ {icon}][ Hi: {high_temp}][ Lo: {low_temp}][ {update_error}]',
    interval=900,
    colorize=True,
    hints={'markup': 'pango'},
    backend=weathercom.Weathercom(
        location_code='a923c5e150d89346b6976561f561bd5a1e5d04bd21f95ff5fa5f62d9df22a03b',
        units='metric',  # imperial|metric
        update_error='<span color="#ff0000">!</span>',
    ),
)


status.run()
