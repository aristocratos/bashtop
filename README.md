# ![bashtop](logo-t.png)

**Usage:** Linux resource monitor  
**Language:** Bash  

## Description

Resource monitor that shows usage and stats for processor, memory, disks, network and processes.

## Features

* Easy to use, with a game inspired menu system.
* Fast and responsive UI with UP, DOWN keys process selection.
* Function for showing detailed stats for selected process.
* Ability to filter processes.
* Easy switching between sorting options.
* Send SIGTERM, SIGKILL, SIGINT to selected process.
* UI menu for changing all config file options.
* Auto scaling graph for network usage.
* Shows message in menu if new version is available

## Themes

Bashtop now has theme support and a function to download missing local themes from repository.

See [themes](themes) folder for available themes.

Let me know if you want to contribute with new themes.

## Upcoming (osx and bsd support)

Currently rewriting to use python3 [psutil](https://github.com/giampaolo/psutil) for data collection instead of linux specific tools.
This will add python 3 and psutil as dependencies, but will make bashtop cross platform compatible.

This will be in a new branch called bashtop-psutil when I'm done with inital testing

## Support and funding

Bug fixes and updates might be slow during normal workdays since i work full time as an industrial worker and don't have much time or energy left during the week.
I'm looking into ways of funding this project that would allow me to take off time from my day job to work on this.
Any advice on how to get funding for open source projects is very welcome!

## Compability

Should work on most modern linux distributions with a truecolor capable terminal.

## Dependencies

**[bash](https://www.gnu.org/software/bash/)** (v4.4 or later) Script functionality will most probably break with earlier versions.  
Bash version 5 is higly recommended to make use of $EPOCHREALTIME variable instead of alot of external date command calls.

**[GNU Core Utilities](https://www.gnu.org/software/coreutils/)**

**[GNU Grep](https://www.gnu.org/software/grep/)**

**[ps from procps-ng](https://gitlab.com/procps-ng/procps)** (v3.1.15 or later)

**[sed](https://www.gnu.org/software/sed/)**

**[awk](https://www.gnu.org/software/gawk/)**

(Optional) **[lm-sensors](https://github.com/lm-sensors/lm-sensors)** Needed to show CPU temperatures

(Optional) **[curl](https://curl.haxx.se/download.html)** (v7.16.2 or later) Needed if you want messages about updates and the ability to download themes.

## Screenshots

Main UI showing details for a selected process.  
![Screenshot 1](main.png)

Main menu.  
![Screenshot 2](menu.png)

Options menu.  
![Screenshot 3](options.png)

## Installation

Copy or link "bashtop" into PATH, or just run from cloned directory...

Also available in the Arch Linux repository as [bashtop](https://www.archlinux.org/packages/community/any/bashtop/)

Also available in the AUR as [bashtop-git](https://aur.archlinux.org/packages/bashtop-git/)

Also available for debian/ubuntu from [Azlux's repository](http://packages.azlux.fr/)

## Configurability

All options changeable from within UI.
Config files stored in "$HOME/.config/bashtop" folder

#### bashtop.cfg: (auto generated if not found)

```bash
#? Config file for bashtop v. 0.8.0

#* Color theme, looks for a .theme file in "$HOME/.config/bashtop/themes", "Default" for builtin default theme
color_theme="Default"

#* Update time in milliseconds, increases automatically if set below internal loops processing time, recommended 2000 ms or above for better sample times for graphs
update_ms="2500"

#* Processes sorting, "pid" "program" "arguments" "threads" "user" "memory" "cpu lazy" "cpu responsive"
#* "cpu lazy" upates sorting over time, "cpu responsive" updates sorting directly at a cpu usage cost
proc_sorting="cpu lazy"

#* Reverse sorting order, "true" or "false"
proc_reversed="false"

#* Check cpu temperature, only works if "sensors" command is available and have values for "Package" and "Core"
check_temp="true"

#* Draw a clock at top of screen, formatting according to strftime, empty string to disable
draw_clock="%R"

#* Update main ui when menus are showing, set this to false if the menus is flickering too much for comfort
background_update="true"

#* Custom cpu model name, empty string to disable
custom_cpu_name=""

#* Enable error logging to "$HOME/.config/bashtop/error.log", "true" or "false"
error_logging="true"
```

#### Command line options: (not yet implemented)

```
USAGE: bashtop

```



## TODO


- [x] TODO Add options to change colors for text, graphs and meters.
- [ ] TODO Add options for resizing all boxes.
- [ ] TODO Add command line argument parsing.
- [ ] TODO Miscellaneous optimizations and code cleanup.
- [ ] TODO Add more commenting where it's sparse.


## LICENSE
[Apache License 2.0](LICENSE)
