#!/usr/bin/env python3
from i3pystatus import Status

status = Status()

status.register(
    "text",
    text='power',
    on_leftclick='gnome-session-quit --power-off',
)

status.register(
    "text",
    text='logout',
    on_leftclick='gnome-session-quit --logout',
)

status.register(
    "text",
    text='suspend',
    on_leftclick='systemctl suspend',
)


status.register(
    "text",
    text='settings',
    on_leftclick='gnome-control-center',
)

status.register(
    "text",
    text='flameshot',
    on_leftclick='/usr/bin/flameshot gui',
    on_rightclick='/usr/bin/flameshot config',
)


status.register(
  "bluetooth",
  format='bluetooth',
  show_disconnected=True,
  on_leftclick='gnome-control-center bluetooth',
)

status.register(
    "disk",
    path="/",
    format="disk:{used:.0f}G",
    on_leftclick='baobab',  # Disk Usage Analyzer
)

status.register(
    "mem",
    format='ram:{used_mem}G',
    divisor=1024 * 1024 * 1024,
)

status.register(
    "load",
    format='cpu:{avg1} {avg5} {avg15}',
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
    format="{temp:.0f}°C",
)

status.register(
    "uptime",
    format='up:{days}d{hours}h',
)

status.register(
    'shell',
    command='nmcli -t connection show --active | grep -i vpn | cut -d: -f1',
    format='vpn:{output}',
    on_leftclick='gnome-control-center network',  # vpn is in network panel
    on_rightclick='nm-connection-editor',
)

status.register(
    "network",
    detect_active=True,
    interval=5,
    auto_units=True,
    format_up="wifi:{essid} {bytes_recv}",
    on_leftclick='gnome-control-center wifi',
    on_rightclick='nm-connection-editor',
)

status.run()
