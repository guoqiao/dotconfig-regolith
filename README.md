# regolith config

Config files for [Regolith Linux](https://regolith-linux.org/), a modern Linux Desktop Environment, built on top of Ubuntu, GNOME and i3wm.

## Usage

1) setup regolith
```
cd ~/.config
git clone git@github.com:guoqiao/regolith-config.git regolith
cd regolith
./bootstrap.sh
```

2) Logout and switch login manager to Regolith


## Status Bar

status bar is very similar to the classic task bar in Windows XP.
This repo use [pyi3status](https://github.com/enkore/i3pystatus) to generate status bar items:

![bar.png](./bar.png)

In `i3/config`, you can config status bar with `bar.py` in 2 ways:

1) one single bar:


```
bar {
  ...
  status_command ~/.config/regolith/bar.py --mode one
  ...
}
```

`--mode one` is default, can be omitted.


2) top bar +  bottom bar:


```
bar {
  id top
  status_command ~/.config/regolith/bar.py --mode top
  ...
}

bar {
  id bottom
  status_command ~/.config/regolith/bar.py --mode bottom
  ...
}
```
