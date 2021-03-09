#!/usr/bin/env python3
from i3pystatus import Status

status = Status()

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
    text='📸',
    on_leftclick='/usr/bin/flameshot gui',
    on_rightclick='/usr/bin/flameshot config',
)

status.register(
    "network",
    detect_active=True,
    interval=5,
    auto_units=True,
    format_up="📶{essid} {bytes_recv}",
    on_leftclick='gnome-control-center wifi',
    on_rightclick='nm-connection-editor',
)

status.register(
    'shell',
    command='nmcli -t connection show --active | grep -i vpn | cut -d: -f1',
    format='👻{output}',
    on_leftclick='gnome-control-center network',  # vpn is in network panel
    on_rightclick='nm-connection-editor',
)

status.register(
  "bluetooth",
  format='🎧{name}',
  show_disconnected=True,
  on_leftclick='gnome-control-center bluetooth',
)

status.run()
