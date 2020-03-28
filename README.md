# bashtop

**Version:** 0.6.2  
**Usage:** Tmp
**Language:** Bash & Python  

## Description

Internet speeds are tested against random servers from speedtest.net at an timed interval (defined by user).  
If slow speed (defined by user) is detected, then runs a number of download and upload test with optional route tests to servers and writes to a logfile.

## Screenshots

Main UI with graph on.

![Screenshot 1]()

## Features

* Function for checking current bandwidth usage to block false positives. Can optionally collect bandwidth usage from a router running linux with a ssh server enabled.
* Scrollable graph showing speeds over time.
* All output in the UI is also scrollabe with UP, DOWN, PAGE_UP, PAGE_DOWN, HOME, END keys working as you would expect.
* Option to have the timer reset on any mouse or keyboard activity in XServer.
* Option to have the timer auto pause when monitor is on and unpause when monitor is off.
* Unit used can be switched between Mbits and MB/s.
* Function for splitting log files at a defined size, old log files can also be automatically compressed.

## Configurability

Config files stored in "$HOME/.config/spdtest" folder

#### spdtest.cfg: (auto generated if not found)
```bash
net_device="auto"		#* Network interface to get current speed from, set to "auto" to get default interface from "ip route" command
unit="megabit"			#* Default speed value to use, valid values are "megabit" and "megabyte"
slowspeed="30"			#* Download speed in unit defined above that triggers more tests, recommended set to 10%-40% of your max speed
numservers="30"			#* How many of the closest servers to get from speedtest.net, used as random pool of servers to test against
slowretry="1"			#* When speed is below slowspeed, how many retries of random servers before running full tests
max_err_retry="3"		#* Max servers to test if an error is encountered in slowcheck
numslowservers="8"		#* How many of the closest servers from list to test if slow speed has been detected, tests all if not set
precheck="true"			#* Check current bandwidth usage before slowcheck, blocks if speed is higher then values set below
precheck_samplet="5"		#* Time in seconds to sample bandwidth usage, defaults to 5 if not set
precheck_down="50"		#* Download speed in unit defined above that blocks slowcheck
precheck_up="50"		#* Upload speed in unit defined above that blocks slowcheck
precheck_ssh_host="192.168.1.1" #* If set, precheck will fetch data from /proc/net/dev over SSH, for example from a router running linux
				#* remote machine needs to have: "/proc/net/dev" and be able to run commands "ip route" and "grep"
				#* copy SSH keys to remote machine if you don't want to be asked for password at start, guide: https://www.ssh.com/ssh/copy-id
precheck_ssh_user="admin" 	#* Username for ssh connection
precheck_ssh_nd="auto" 		#* Network interface on remote machine to get speeds from, set to "auto" if unsure
waittime="00:20:00"		#* Default wait timer between slowchecks, format: "HH:MM:SS"
slowwait="00:10:00"		#* Time between tests when slow speed has been detected, uses wait timer if unset, format: "HH:MM:SS"
idle="false"			#* If "true", resets timer if keyboard or mouse activity is detected in XServer
# idletimer="00:30:00"		#* If set and idle="true", the script uses this timer until first test, then uses standard wait time,
				#* any X Server activity resets back to idletimer, format: "HH:MM:SS"
displaypause="false"		#* If "true" automatically pauses timer when display is on, unpauses when off, overrides idle="true" if set, needs xset to work
paused="false"			#* If "true", the timer is paused at startup, ignored if displaypause="true"
startuptest="false"		#* If "true" and paused="false", tests speed at startup before timer starts
main_menu_start="shown" 	#* The status of the main menu at start, possible values: "shown", "hidden"
graph_start="shown"		#* The status of the speed graph at start, possible values: "shown", "hidden"
loglevel="2"			#* 0 : No logging
				#* 1 : Log only when slow speed has been detected
				#* 2 : Also log slow speed check
				#* 3 : Also log server updates
				#* 4 : Log all including forced tests
logdir="$HOME/spdtest-logs" 	#* Logfile save directory
quiet_start="true"		#* If "true", don't print serverlist and routelist at startup
maxlogsize="1024"		#* Max logsize (in kilobytes) before log is split
logcompress="gzip"		#* Command for compressing logs, only log splits beyond the last split is compressed, disabled if not set
# custom_log=""			#* Custom logfile (full path), if a custom logfile is set log splitting is disabled
max_buffer="1000"		#* Max number of lines to buffer in internal scroll buffer
buffer_save="true"		#* Save buffer to disk on exit and restore on start
mtr="true"			#* Set "false" to disable route testing with mtr, automatically set to "false" if mtr is not found in PATH
mtr_internal="true"		#* Use hosts from full test with speeds below $slowspeed in mtr test
mtr_internal_ok="false"		#* Use hosts from full test with speeds above $slowspeed in mtr test
# mtr_internal_max=""		#* Set max hosts to add from full test
mtr_external="false"		#* Use hosts from route.cfg, see route.cfg.sample for formatting
mtrpings="25"			#* Number of pings sent with mtr
testonly="false" 		#* If "true", never enter UI mode, always run full tests and quit
testnum="1"			#* Number of times to loop full tests in testonly mode

ookla_speedtest="speedtest"	#* Command or full path to official speedtest client 

trace_errors="true"		#* In event of error print line number of offending command to $HOME/.config/spdtest/errors
```

#### route.cfg.sample: (rename to route.cfg to use additional hosts in route test)
```bash
#? List of routes to test with mtr
#? Format:
#? routelista+=("host")
#? routelistdesc["host"]=("Name")
#? routelistport["host"]=("port")  'Set port to "auto" if you don't want to set a custom port!'

routelista+=("google.com")
routelistdesc["google.com"]="Google"
routelistport["google.com"]="auto"

routelista+=("reddit.com")
routelistdesc["reddit.com"]="Reddit"
routelistport["reddit.com"]="auto"

routelista+=("twitch.tv")
routelistdesc["twitch.tv"]="Twitch"
routelistport["twitch.tv"]="auto"

routelista+=("amazon.com")
routelistdesc["amazon.com"]="Amazon"
routelistport["amazon.com"]="auto"
```

#### Command line options: (to be updated)
```
USAGE: ./spdtest.sh [OPTIONS]

OPTIONS:
        -t, --test [num]            Runs full test 1 or <x> number of times and quits
        -u, --unit megabit/megabyte Which unit to show speed in, [default: megabit]
        -s, --slow-speed speed      Defines what speed in defined unit that will trigger more tests
        -n, --num-servers num       How many of the closest servers to get from speedtest.net
        -i, --interface name        Network interface being used [default: auto]
        -l, --loglevel 0-3          0 No logging
                                    1 Log only when slow speed has been detected
                                    2 Also log slow speed check and server update
                                    3 Log all including forced tests
        -lf, --log-file file        Full path to custom logfile, no log rotation is done on custom logfiles
        -p, --paused                Sets timer to paused state at startup
        -wt, --wait-time HH:MM:SS   Time between tests when NO slowdown is detected [default: 00:10:00]
        -st, --slow-time HH:MM:SS   Time between tests when slowdown has been detected, uses wait timer if unset
        -x, --x-reset [HH:MM:SS]    Reset timer if keyboard or mouse activity is detected in X Server
                                    If HH:MM:SS is included, the script uses this timer until first test, then uses
                                    standard wait time, any activity resets to idle timer [default: unset]
        -d, --display-pause         Automatically pauses timer when display is on, unpauses when off
        -gs, --gen-server-cfg num   Writes <x> number of the closest servers to "server.cfg" and quits
                                    Servers aren't updated automatically at start if "server.cfg" exists
        -sc, --server-config file   Reads server config from <file> [default: server.cfg]
                                    If used in combination with -gs a new file is created
        -h, --help                  Shows help information
CONFIG:
                                    Note: All config files are stored in: $HOME/.config/spdtest
        spdtest.cfg                 Automatically created with default values if removed
        [server.cfg]                Stores server id's to use with speedtest, delete to refresh servers on start
        [route.cfg]                 Additional hosts to test with mtr, see route.cfg.sample for formatting
LOG:
                                    Logfile location can be changed in config file
                                    Currently: $HOME/spdtest-logs
```

## Dependencies

**bash** (v4.4 or later) Script functionality might brake with earlier versions.  

**[Python 3](https://www.python.org/downloads)** (v3.7 or later) Needed for speedtest-cli, grc and getIdle.  

**[speedtest](https://www.speedtest.net/apps/cli)** Official speedtest client from Ookla, needs to be in path or defined in config.

**[jq](https://stedolan.github.io/jq/)** Needed for json parsing.  

## Included

**[speedtest-cli](https://github.com/sivel/speedtest-cli)** Used to get serverlist, since official speedtest client from Ookla is limited to 10 servers.  
Modified and heavily stripped down, based on version 2.1.2. Python code included in the script.

**[grc](https://github.com/garabik/grc)** For making text output in the UI pretty.  
Modified version of grcat. Python code included in the script.

**getIdle** Get XServer idle time. Python code included in script.

## Optionals

**[mtr](https://github.com/traviscross/mtr)** Needed if you want to check routes to slow servers.  

**[less](http://www.greenwoodsoftware.com/less/)** Needed if you want option to view logfile from UI.  

## TODO


- [ ] TODO Fix argument parsing and error messages
- [ ] TODO Change slowtest to multiple servers and compare results
- [ ] TODO fix wrong keypress in inputwait, esc codes etc
- [ ] TODO fix up README.md
- [x] TODO extern config and save to config?
- [x] TODO ssh controlmaster, server, client for precheck_speed
- [ ] TODO buffer logview
- [ ] TODO route test menu, choose host to test
- [ ] TODO windows: help, options, route
- [x] TODO plot speedgraphs overtime in UI  
- [ ] TODO stat file
- [ ] Everything else...

## LICENSE
[Apache License 2.0](LICENSE)
