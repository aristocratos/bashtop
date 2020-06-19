# Changelog

## v0.9.13

* Added: More robust psutil error handling

## v0.9.12

* Changed: Psutil data collection now runs a python script in a coprocess taking commands and sending output over coproc pipes
* Added: Psutil data collection now replaces most external calls including sensors, cpu info, disks info and io collection
* Changed: Tree view is now a toggle instead of sorting option
* Fixed: Cpu temp check not using vcgencmd when sensors is available

## v0.9.11

* Fixed: Processes text color now sets RGB instead of RBB...

## v0.9.10

* Fixed: Humanizer function now round values 1000-1023 up to 1024 to fit size constraints.
* Added: More error checks for psutil
* Changed: Terminal title now includes original title if $TERMINAL_TITLE is set, suggested by @theytaz

## v0.9.9

* Fixed: Fixed theme downloader not reporting new themes and corrected comment in config

## v0.9.8

* Added: Nord theme by Justin Zobel
* Changed: Theme downloader now overwrites default themes, folder user_themes (safe from overwrites) added
* Changed: Cleaned up monokai theme variants
* Added: Base for testing with BATS by Maciek Swiech

## v0.9.7

* Changed: UTF-8 locale check, try to find UTF-8 for current language if LANG is set but not with "UTF-8" suffix

## v0.9.6

* Fixed: UTF-8 locale check

## v0.9.5

* Added: UTF-8 locale check and automatic LANG variable set if not UTF-8
* Fixed: Filter out zero sized disks and added some psutil error checks

## v0.9.4

* Fixed: Missing path for OSX df and correct swap usage reporting for OSX

## v0.9.3

* Fixed: Resizing problems in iTerm2
* Changed: Removed redundant error checking in print function for lower cpu usage
* Fixed: Memory in OSX now shows active memory usage and /private/var/vm as swap memory
* Fixed: Disks in OSX changed from using "GNU df" to "BSD df" for better compatibility

## v0.9.2

* Fixed: Correct prefixes for some missed GNU tools
* Added: Startup progress screen
* Changed: replaced tput commands with escape sequence commands

## v0.9.1

* Added: FreeBSD support with python3 psutil data collection
* Added: Check for gnu tools on non Linux platforms
* Fixed: Increased graph history to avoid cut off on high resolution graphs

## v0.9.0

* Added: Mac OS X support with python3 psutil data collection
* Added: Ability to switch between all available network devices

## v0.8.32

* Fixed: Error in theme error checking corrupting default theme

## v0.8.31

* Fixed: Theme 2-color gradient generation
* Fixed: Theme file error checking

## v0.8.30

* Fixed: Crash on missing net device

## v0.8.29

* Fixed: Cpu temperature colors not working when above high temp value
* Fixed: Unescaped "\" in process list and indent fixes
* Changed: Changes to net graph rescaling parameters

## v0.8.28

* Fixed: Ctrl-C and Ctrl-Z not registering after change to "dd"
* Added: Option to switch to high resolution graphs
* Added: Current peak value for download/upload graphs

## v0.8.27

* Fixed: Use value for "Inactive"+"MemFree" if "MemAvailable" is missing in /proc/meminfo
* Added: Option to toggle update check at start

## v0.8.26

* Fixed: Escaped delimiter for sed to fix config not saving "/" character
* Fixed: Detailed process view missing info and slowdown in certain cases
* Optimization: Fork cleanup

## v0.8.25

* Fixed: Backspace not registering when not set to send ascii delete
* Fixed: Broken cpu temperature graph when is value over cpu high temp
* Added: Possibility to run date through background fifo for bash <5

## v0.8.24

* Fixed: Input error freezes, by changing from using "read" command to using "dd" for reading keyboard input.

## v0.8.23

* Added: Support for Raspberry Pi cpu temperature reporting
* Fixed: Decreased chance of read command stalling on lower spec systems
* Added: Failover to nproc if lscpu are reporting 0 cpu cores
* Changed: Moved page display for options and help to bottom and changed to Page Up/Down for changing page

## v0.8.22

* Added: Sorting option "tree", shows processes in a tree structure
* Added: Option to toggle process cpu usage per core instead of total available cpu power
* Fixed: Possible fix for stalling read command
* Added: Multiple while loop fail safes

## v0.8.21

* Fixed: iostat flag compatibility for older iostat versions
* Fixed: possible fix for script stall on bash 4

## v0.8.20

* Fixed: Update slowdown when not sorting by cpu
* Added: New version desktop notification

## v0.8.19

* Added: Disks read and write stats, requires new optional dependency "iostat (part of sysstat)"
* Fixed: Ctrl-C not working when showing resize error message
* Fixed: Network download/upload offset auto switched off if /proc/net/dev resets
* Fixed: Removed trailing whitespace in script

## v0.8.18

* Added: Pagination for help and options windows if items don't fit
* Added: Option to turn off color gradient in process list
* Changed: bash version check to use $BASH_VERSINFO array
* Added: Filter for shown disks
* Added: Option to reset network totals in options menu

## v0.8.17

* Fixed: Not showing CPU temperatures when "Package" temp is missing
* Added: CPU temperature support for AMD Ryzen
* Changed: Minimum size changed from 80x25 to 80x24
* Fixed: High cpu usage on systems with a lot of mounted disks

## v0.8.16

* Added: Bash version check, by Calinou
* Added: OS check, by kpucynski
* Fixed: number of themes reported in options when theme folder is empty, by deluxe
* Fixed: README.md typos, by lucaskim1233
* Added: CHANGELOG.md

## v0.8.15

* Added: deb build script by Jukoo
* Fixed: load average and uptime not showing
* Fixed: freeze on reverse process order when showing detailed information
* Fixed: single quotes on associative arrays

## v0.8.14

* Fixed: disks usage runaway array
* Fixed: disks used not reporting new values
* Changed: memory and disks update frequency increased

## v0.8.13

* Fixed: get_value() regex
* Added: 2 new themes, flat-remix and flat-remix-light, by Daniel Ruiz de Alegría
* Other: general cleanup and formatting

## v0.8.12

* Fixed: changed remaining ps thcount flags to nlwp

## v0.8.11

* Fixed: ps flag thcount changed to nlwp for greater compability
* Fixed: regex and float to int rounding in get_value()

## v0.8.10

* Fixed: erroneous regular expressions

## v0.8.9

* Added: functions is_int, is_float, is_hex
* Fixes: error checking on internal functions

## v0.8.8

* Fixed: load average max length

## v0.8.7

* Fixed: load average clipping
* Fixed: cpu box calculations error

## v0.8.6

* Added: load average and uptime
* Fixed: cohesive window size representation
* Added: unset LC_ALL to not override wanted locale
* Fixed: cpu box calculation errors

## v0.8.5

* Fixed: cpu frequency and /proc/stat error checks
