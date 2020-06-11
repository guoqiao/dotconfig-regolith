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

#  status.register(
    #  "weekcal",
    #  interval=60,
    #  startofweek=0,  # 0 = Monday, 6 = Sunday
    #  prefixformat=' %Y %B',  # Feb
    #  suffixformat='%A',  # Sat
    #  todayhighlight=[' [', '] '],
    #  on_leftclick='gnome-calendar',
#  )

status.register(
    "bluetooth",
    format='',
    color="#808080",
    show_disconnected=True,
    on_leftclick='gnome-control-center bluetooth',
)

status.register(
    "battery",
    format='{status}{percentage:.0f}%',
    status={
        'DPL': '',  # Depleted
        'CHR': '',
        'DIS': '',
        'FULL': '',
    },
    on_leftclick='gnome-control-center power',
)

status.register(
    "tlp",
    ac_text='',
    bat_text='',
    na_text='',
)

status.register(
    "disk",
    path="/",
    format="{used:.0f}G",
    on_leftclick='baobab',  # Disk Usage Analyzer
)

status.register(
    "mem",
    format='{used_mem}G',
    divisor=1024 * 1024 * 1024,
)

status.register(
    "load",
    format='{avg1} {avg5} {avg15}',
    on_leftclick='/snap/bin/gnome-system-monitor --show-processes-tab',
)

status.register(
    'shell',
    command='sensors | grep fan | cut -d: -f2 | tr -d " "',
    format='{output}',
    on_leftclick='/snap/bin/gnome-system-monitor --show-processes-tab',
)

status.register(
    "temp",
    format="{temp:.0f}°C",
)

status.register(
    "uptime",
    format='{days}d{hours}h',
)

status.register(
    'shell',
    command='nmcli -t connection show --active | grep -i vpn | cut -d: -f1',
    format='{output}',
    on_leftclick='gnome-control-center network',  # vpn is in network panel
    on_rightclick='nm-connection-editor',
)

status.register(
    "network",
    interface="wlp3s0",
    interval=5,
    auto_units=True,
    format_up="{essid} {bytes_recv}",
    on_leftclick='gnome-control-center wifi',
    on_rightclick='nm-connection-editor',
)

status.run()
