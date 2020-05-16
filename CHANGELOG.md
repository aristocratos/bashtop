# Changelog

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
