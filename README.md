# ![bashtop](Imgs/logo-t.png)

![Linux](https://img.shields.io/badge/-Linux-grey?logo=linux)
![OSX](https://img.shields.io/badge/-OSX-black?logo=apple)
![FreeBSD](https://img.shields.io/badge/-FreeBSD-red?logo=freebsd)
![Usage](https://img.shields.io/badge/Usage-System%20resource%20monitor-blue)
![Bash](https://img.shields.io/badge/Bash-v4.4%5E-green?logo=GNU%20bash)
![Python](https://img.shields.io/badge/Python-v3.6%5E-orange?logo=python)
![bashtop_version](https://img.shields.io/github/v/tag/aristocratos/bashtop?label=version)
[![Build Status](https://travis-ci.com/aristocratos/bashtop.svg?branch=master)](https://travis-ci.com/aristocratos/bashtop)
[![Donate](https://img.shields.io/badge/-Donate-yellow?logo=paypal)](https://paypal.me/aristocratos)
[![Sponsor](https://img.shields.io/badge/-Sponsor-red?logo=github)](https://github.com/sponsors/aristocratos)
[![Coffee](https://img.shields.io/badge/-Buy%20me%20a%20Coffee-grey?logo=Ko-fi)](https://ko-fi.com/aristocratos)

## Index

* [Documents](#documents)
* [Description](#description)
* [Features](#features)
* [Themes](#themes) (Updated)
* [Upcoming](#upcoming) (Python port)
* [Support and funding](#support-and-funding)
* [Compatibility](#compatibility) (OSX and FreeBSD Support)
* [Dependencies](#dependencies) (Updated)
* [Screenshots](#screenshots)
* [Installation](#installation) (Updated)
* [Configurability](#configurability)
* [TODO](#todo) (Updated)
* [License](#license)

## Documents

#### [CHANGELOG.md](CHANGELOG.md)

#### [CONTRIBUTING.md](CONTRIBUTING.md)

#### [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## Description

Resource monitor that shows usage and stats for processor, memory, disks, network and processes.

## Features

* Easy to use, with a game inspired menu system.
* Fast and "mostly" responsive UI with UP, DOWN keys process selection.
* Function for showing detailed stats for selected process.
* Ability to filter processes.
* Easy switching between sorting options.
* Send SIGTERM, SIGKILL, SIGINT to selected process.
* UI menu for changing all config file options.
* Auto scaling graph for network usage.
* Shows message in menu if new version is available
* Shows current read and write speeds for disks
* Multiple data collection methods which can be switched if running on Linux

## Themes

Bashtop now has theme support and a function to download missing local themes from repository.

See [themes](themes) folder for available themes.

The builtin theme downloader places the default themes in `$HOME/.config/bashtop/themes`.
User created themes should be placed in `$HOME/.config/bashtop/user_themes` to be safe from overwrites.

Let me know if you want to contribute with new themes.

## Upcoming

~~Currently rewriting to use python3 [psutil](https://github.com/giampaolo/psutil) for data collection instead of linux specific tools.
This will add python 3 and psutil as dependencies, but will make bashtop cross platform compatible.~~

~~This will be integrated in to main version when done and add the possibility to switch between psutil and linux tools for users running linux.~~

Bashtop is now Mac OS X and FreeBSD compatible!

#### Python port

Work on a complete python port ~~will begin this summer~~ has begun. My aim is to keep it compatible with pypy3 for a lot of added efficiency.

PyPyTop?

## Support and funding

Bug fixes and updates might be slow during normal workdays since I work full time as an industrial worker and don't have much time or energy left during the week.
I'm looking into ways of funding this project that would allow me to take off time from my day job to work on this.

Any advice on how to get funding for open source projects is very welcome!

#### Update

You can now sponsor this project through github, see [my sponsors page](https://github.com/sponsors/aristocratos) for options.

Also added donation links for [paypal](https://paypal.me/aristocratos) and [ko-fi](https://ko-fi.com/aristocratos).

Any support is greatly appreciated!

## Compatibility

Should work on most modern linux distributions, on Mac OS X and on FreeBSD.

Will not display correctly on the standard terminal on OSX!
Recommended alternative [iTerm2](https://www.iterm2.com/)

Will also need to be run as superuser on OSX to display stats for processes not owned by user.

The disk io stats on OSX and FreeBSD shows iostats for all disks at the top instead of per disk.

For correct display, a terminal with support for:

* 24-bit truecolor
* Wide characters

Also needs a UTF8 locale and a font that covers:

* Unicode Block “Braille Patterns” U+2800 - U+28FF
* Unicode Block “Geometric Shapes” U+25A0 - U+25FF
* Unicode Block "Box Drawing" and "Block Elements" U+2500 - U+259F

#### Notice

Dropbear seems to not be able to set correct locale. So if accessing bashtop over ssh, OpenSSH is recommended.

## Dependencies

## Linux, OSX and FreeBSD

**[bash](https://www.gnu.org/software/bash/)** (v4.4 or later) Script functionality will most probably break with earlier versions.
Bash version 5 is highly recommended to make use of $EPOCHREALTIME variable instead of a lot of external date command calls.

**[GNU coreutils](https://www.gnu.org/software/coreutils/)**

**[GNU sed](https://www.gnu.org/software/sed/)**

## Linux using /proc for data collection

**[GNU grep](https://www.gnu.org/software/grep/)**

**[ps from procps-ng](https://gitlab.com/procps-ng/procps)** (v3.1.15 or later)

**[GNU awk](https://www.gnu.org/software/gawk/)**

## OSX and FreeBSD or Linux using psutil for data collection

**[Python3](https://www.python.org/downloads/)** (v3.6 or later)

**[psutil python module](https://github.com/giampaolo/psutil)**

## Optionals for additional stats

(Optional OSX) **[osx-cpu-temp](https://github.com/lavoiesl/osx-cpu-temp)** Needed to show CPU temperatures.

(Optional Linux) **[lm-sensors](https://github.com/lm-sensors/lm-sensors)** Needed to show CPU temperatures.

(Optional Linux) **[iostat (part of sysstat)](https://github.com/sysstat/sysstat)** Needed if you want disk read/write stats and are not using psutil data collection.

(Optional OSX/Linux/FreeBSD) **[curl](https://curl.haxx.se/download.html)** (v7.16.2 or later) Needed if you want messages about updates and the ability to download themes.

## Screenshots

Main UI showing details for a selected process.
![Screenshot 1](Imgs/main.png)

Main menu.
![Screenshot 2](Imgs/menu.png)

Options menu.
![Screenshot 3](Imgs/options.png)

## Installation

#### Dependencies installation OSX

>Install homebrew if not already installed

``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

>Install dependencies

``` bash
brew install bash coreutils gnu-sed python3 git
pip3 install psutil
```

>Install optional dependency osx-cpu-temp

``` bash
brew install osx-cpu-temp
```

#### Dependencies installation FreeBSD

>Install with pkg and pip

``` bash
sudo pkg install coreutils gsed python3 git
sudo python3 -m ensurepip
sudo pip3 install psutil
```

#### Manual installation Linux, OSX and FreeBSD

>Clone and install

``` bash
git clone https://github.com/aristocratos/bashtop.git
cd bashtop
sudo make install
```

>to uninstall it

``` bash
sudo make uninstall
```

#### Arch based

Available in the AUR as [bashtop-git](https://aur.archlinux.org/packages/bashtop-git/)

Available in the Arch Linux repository as [bashtop](https://www.archlinux.org/packages/community/any/bashtop/)

#### Debian based

Available for debian/ubuntu from [Azlux's repository](http://packages.azlux.fr/)

Or use quick installation:

>Quick install go to DEB  folder  and type

``` bash
 sudo ./build
```

>to uninstall it   go to DEB  folder  and type

``` bash
 sudo ./build --remove
```

#### Ubuntu based

Available for Ubuntu from [PPA repository](https://code.launchpad.net/~bashtop-monitor/+archive/ubuntu/bashtop)

>Add PPA repository and install bashtop

``` bash
 sudo add-apt-repository ppa:bashtop-monitor/bashtop
 sudo apt update
 sudo apt install bashtop
```

#### Fedora

Available in the Fedora repository.

>Installation

``` bash
sudo dnf install bashtop
```

#### CentOS

>Installation

``` bash
dnf config-manager --set-enabled PowerTools
dnf install epel-release
dnf install bashtop
```

#### RHEL 8

>Installation

``` bash
ARCH=$( /bin/arch )
subscription-manager repos --enable
"codeready-builder-for-rhel-8-${ARCH}-rpms"
dnf install epel-release
dnf install bashtop
```

## Configurability

All options changeable from within UI.
Config files stored in "$HOME/.config/bashtop" folder

#### bashtop.cfg: (auto generated if not found)

```bash
#? Config file for bashtop v. 0.9.0

#* Color theme, looks for a .theme file in "$HOME/.config/bashtop/themes", "Default" for builtin default theme
color_theme="Default"

#* Update time in milliseconds, increases automatically if set below internal loops processing time, recommended 2000 ms or above for better sample times for graphs
update_ms="2500"

#* Processes sorting, "pid" "program" "arguments" "threads" "user" "memory" "cpu lazy" "cpu responsive" "tree"
#* "cpu lazy" updates sorting over time, "cpu responsive" updates sorting directly at a cpu usage cost
proc_sorting="cpu lazy"

#* Reverse sorting order, "true" or "false"
proc_reversed="false"

#* Check cpu temperature, only works if "sensors", "vcgencmd" or "osx-cpu-temp" commands is available
check_temp="true"

#* Draw a clock at top of screen, formatting according to strftime, empty string to disable
draw_clock="%X"

#* Update main ui when menus are showing, set this to false if the menus is flickering too much for comfort
background_update="true"

#* Custom cpu model name, empty string to disable
custom_cpu_name=""

#* Enable error logging to "$HOME/.config/bashtop/error.log", "true" or "false"
error_logging="true"

#* Show color gradient in process list, "true" or "false"
proc_gradient="true"

#* If process cpu usage should be of the core it's running on or usage of the total available cpu power
proc_per_core="false"

#* Optional filter for shown disks, should be names of mountpoints, "root" replaces "/", separate multiple values with space
disks_filter=""

#* Enable check for new version from github.com/aristocratos/bashtop at start
update_check="true"

#* Enable graphs with double the horizontal resolution, increases cpu usage
hires_graphs="false"

#* Enable the use of psutil python3 module for data collection, default on OSX
use_psutil="true"
```

#### Command line options: (not yet implemented)

``` bash
USAGE: bashtop

```

## TODO

Might finish off items out of order since I usually work on multiple at a time.

- [x] Add options to change colors for text, graphs and meters.
- [x] Fix cross platform compatibility for Mac OSX and *BSD: Working on OSX, and FreeBSD.
- [x] Add support for showing AMD cpu temperatures.
- [x] Add option to show tree view of processes.
- [x] Add option to reset network download/upload totals.
- [x] Add option to turn of gradient in processes list.
- [ ] Add gpu temp and usage. (If feasible)
- [x] Add io stats for disks.
- [ ] Add cpu and mem stats for docker containers. (If feasible)
- [ ] Change process list to line scroll instead of page change.
- [ ] Add option for custom color gradient in process list in theme settings.
- [ ] Add optional window for tailing log files.
- [ ] Add options for resizing all boxes.
- [ ] Add command line argument parsing.
- [ ] Builtin updater. Relevant PR #96 by Jukoo
- [ ] Add support for zram in memory box. Relevant PR #122 by perkinslr

- [ ] Miscellaneous optimizations and code cleanup.
- [ ] Add more commenting where it's sparse.

- [ ] Python port. (Porting started)

## LICENSE

[Apache License 2.0](LICENSE)
