#!/usr/bin/env python3

'''This is a copy of the python script that bashtop starts in a coprocess when using psutil for data collection'''

import os, sys, subprocess, re, time, psutil
from datetime import timedelta
from collections import defaultdict
from typing import List, Set, Dict, Tuple, Optional, Union

system: str
if "linux" in sys.platform: system = "Linux"
elif "bsd" in sys.platform: system = "BSD"
elif "darwin" in sys.platform: system = "MacOS"
else: system = "Other"

parent_pid: int = psutil.Process(os.getpid()).ppid()

allowed_commands: Tuple[str] = (
	'get_proc',
	'get_disks',
	'get_cpu_name',
	'get_cpu_cores',
	'get_nics',
	'get_cpu_cores',
	'get_cpu_usage',
	'get_cpu_freq',
	'get_uptime',
	'get_load_avg',
	'get_mem',
	'get_detailed_names_cmd',
	'get_detailed_mem_time',
	'get_net',
	'get_cmd_out',
	'get_sensors',
	'get_sensors_check'
	)
command: str = ''
cpu_count: int = psutil.cpu_count()
disk_hist: Dict = {}

def cleaned(string: str) -> str:
	'''Escape characters not suitable for "echo -e" in bash'''
	return string.replace("\\", "\\\\").replace("$", "\\$").replace("\n", "\\n").replace("\t", "\\t").replace("\"", "\\\"").replace("\'", "\\\'")

def get_cmd_out(cmd: str):
	'''Save bash the trouble of creating child processes by running through python instead'''
	print(subprocess.check_output(cmd, shell=True, universal_newlines=True).rstrip())

def get_sensors():
	'''A clone of "sensors" but using psutil'''
	temps = psutil.sensors_temperatures()
	if not temps:
		return
	try:
		for name, entries in temps.items():
			print(name)
			for entry in entries:
				print(f'{entry.label or name}: {entry.current}°C (high = {entry.high}°C, crit = {entry.critical}°C)')
			print()
	except:
		pass

def get_sensors_check():
	'''Check if get_sensors() output contains accepted CPU temperature values'''
	if not hasattr(psutil, "sensors_temperatures"): print("false"); return
	try:
		temps = psutil.sensors_temperatures()
	except:
		pass
		print("false"); return
	if not temps: print("false"); return
	try:
		for _, entries in temps.items():
			for entry in entries:
				if entry.label.startswith(('Package', 'Core 0', 'Tdie')):
					print("true")
					return
	except:
		pass
	print("false")

def get_cpu_name():
	'''Fetch a suitable CPU identifier from the CPU model name string'''
	name: str = ""
	command: str = ""
	all_info: str = ""
	rem_line: str = ""
	if system == "Linux":
		command = "cat /proc/cpuinfo"
		rem_line = "model name"
	elif system == "MacOS":
		command ="sysctl -n machdep.cpu.brand_string"
	elif system == "BSD":
		command ="sysctl hw.model"
		rem_line = "hw.model"

	all_info = subprocess.check_output("LANG=C " + command, shell=True, universal_newlines=True)
	if rem_line:
		for line in all_info.split("\n"):
			if rem_line in line:
				name = re.sub( ".*" + rem_line + ".*:", "", line,1).lstrip()
	else:
		name = all_info
	if "Xeon" in name:
		name = name.split(" ")
		name = name[name.index("CPU")+1]
	elif "Ryzen" in name:
		name = name.split(" ")
		name = " ".join(name[name.index("Ryzen"):name.index("Ryzen")+3])
	elif "CPU" in name:
		name = name.split(" ")
		name = name[name.index("CPU")-1]

	print(name)

def get_cpu_cores():
	'''Get number of CPU cores and threads'''
	cores: int = psutil.cpu_count(logical=True)
	threads: int = psutil.cpu_count(logical=False)
	print(f'{cores} {threads if threads else cores}')

def get_cpu_usage():
	cpu: float = psutil.cpu_percent(percpu=False)
	threads: List[float] = psutil.cpu_percent(percpu=True)
	print(f'{cpu:.0f}')
	for thread in threads:
		print(f'{thread:.0f}')

def get_cpu_freq():
	'''Get current CPU frequency'''
	try:
		print(f'{psutil.cpu_freq().current:.0f}')
	except:
		print(0)

def get_uptime():
	'''Get current system uptime'''
	print(str(timedelta(seconds=round(time.time()-psutil.boot_time(),0)))[:-3])

def get_load_avg():
	'''Get CPU load average'''
	for lavg in os.getloadavg():
		print(round(lavg, 2), ' ', end='')
	print()

def get_mem():
	'''Get current system memory and swap usage'''
	mem = psutil.virtual_memory()
	swap = psutil.swap_memory()
	try:
		cmem = mem.cached>>10
	except:
		cmem = mem.active>>10
	print(mem.total>>10, mem.free>>10, mem.available>>10, cmem, swap.total>>10, swap.free>>10)

def get_nics():
	'''Get a list of all network devices sorted by highest throughput'''
	io_all = psutil.net_io_counters(pernic=True)
	up_stat = psutil.net_if_stats()

	for nic in sorted(psutil.net_if_addrs(), key=lambda nic: (io_all[nic].bytes_recv + io_all[nic].bytes_sent), reverse=True):
		if up_stat[nic].isup is False:
			continue
		print(nic)

def get_net(net_dev: str):
	'''Emulated /proc/net/dev for selected network device'''
	net = psutil.net_io_counters(pernic=True)[net_dev]
	print(0,net.bytes_recv,0,0,0,0,0,0,0,net.bytes_sent)

def get_detailed_names_cmd(pid: int):
	'''Get name, parent name, username and arguments for selected pid'''
	p = psutil.Process(pid)
	pa = psutil.Process(p.ppid())
	with p.oneshot():
		print(p.name())
		print(pa.name())
		print(p.username())
		cmd = ' '.join(p.cmdline()) or '[' + p.name() + ']'
		print(cleaned(cmd))

def get_detailed_mem_time(pid: int):
	'''Get memory usage and runtime for selected pid'''
	p = psutil.Process(pid)
	with p.oneshot():
		print(p.memory_info().rss)
		print(timedelta(seconds=round(time.time()-p.create_time(),0)))

def get_proc(sorting='cpu lazy', tree=False, prog_len=0, arg_len=0, search='', reverse=True, proc_per_cpu=True, max_lines=0):
	'''List all processess with pid, name, arguments, threads, username, memory percent and cpu percent'''
	line_count: int = 0
	err: float = 0.0
	reverse = not reverse

	if sorting == 'pid':
		sort_cmd = "p.info['pid']"
	elif sorting == 'program' or tree and sorting == "arguments":
		sort_cmd = "p.info['name']"
		reverse = not reverse
	elif sorting == 'arguments':
		sort_cmd = "' '.join(str(p.info['cmdline'])) or p.info['name']"
		reverse = not reverse
	elif sorting == 'threads':
		sort_cmd = "str(p.info['num_threads'])"
	elif sorting == 'user':
		sort_cmd = "p.info['username']"
		reverse = not reverse
	elif sorting == 'memory':
		sort_cmd = "str(p.info['memory_percent'])"
	elif sorting == 'cpu responsive':
		sort_cmd = "p.info['cpu_percent']" if proc_per_cpu else "(p.info['cpu_percent'] / cpu_count)"
	else:
		sort_cmd = "(sum(p.info['cpu_times'][:2] if not p.info['cpu_times'] == 0.0 else [0.0, 0.0]) * 1000 / (time.time() - p.info['create_time']))"

	if tree:
		proc_tree(width=prog_len + arg_len, sorting=sort_cmd, reverse=reverse, max_lines=max_lines, proc_per_cpu=proc_per_cpu, search=search)
		return


	print(f"{'Pid:':>7} {'Program:':<{prog_len}}", f"{'Arguments:':<{arg_len-4}}" if arg_len else '', f"{'Threads:' if arg_len else ' Tr:'} {'User:':<9}Mem%{'Cpu%':>11}", sep='')

	for p in sorted(psutil.process_iter(['pid', 'name', 'cmdline', 'num_threads', 'username', 'memory_percent', 'cpu_percent', 'cpu_times', 'create_time'], err), key=lambda p: eval(sort_cmd), reverse=reverse):
		if p.info['name'] == 'idle':
			continue
		if p.info['cpu_times'] == err:
			p.info['num_threads'] = 0
			p.info['cmdline'] = ''
		if search:
			found = False
			for value in [ p.info['name'], ' '.join(p.info['cmdline']), str(p.info['pid']), p.info['username'] ]:
				if search in value:
					found = True
					break
			if not found:
				continue

		cpu = p.info['cpu_percent'] if proc_per_cpu else (p.info['cpu_percent'] / psutil.cpu_count())
		mem = p.info['memory_percent']
		cmd = ' '.join(p.info['cmdline']) or '[' + p.info['name'] + ']'
		print(f"{p.info['pid']:>7} ",
			f"{cleaned(p.info['name']):<{prog_len}.{prog_len-1}}",
			f"{cleaned(cmd):<{arg_len}.{arg_len-1}}" if arg_len else '',
			f"{p.info['num_threads']:>4} " if p.info['num_threads'] < 1000 else '999> ',
			f"{p.info['username']:<9.9}" if len(p.info['username']) < 10 else f"{p.info['username'][:8]:<8}+",
			f"{mem:>4.1f}" if mem < 100 else f"{mem:>4.0f} ",
			f"{cpu:>11.1f} " if cpu < 100 else f"{cpu:>11.0f} ",
			sep='')
		line_count += 1
		if max_lines and line_count == max_lines:
			break

def proc_tree(width: int, sorting: str = 'cpu lazy', reverse: bool = True, max_lines: int = 0, proc_per_cpu=True, search=''):
	'''List all processess in a tree view with pid, name, threads, username, memory percent and cpu percent'''
	tree_line_count: int = 0
	err: float = 0.0

	def create_tree(parent: int, tree, indent: str = '', inindent: str = ' ', found: bool = False):
		nonlocal infolist, tree_line_count, max_lines, tree_width, proc_per_cpu, search
		cont: bool = True
		if max_lines and tree_line_count >= max_lines:
			return
		try:
			name: str = psutil.Process(parent).name()
			if name == "idle": return
		except psutil.Error:
			pass
			name: str = ''
		try:
			getinfo: Dict = infolist[parent]
		except:
			pass
			getinfo: bool = False
		if search and not found:
			for value in [ name, str(parent), getinfo['username'] if getinfo else '' ]:
				if search in value:
					found = True
					break
			if not found:
				cont = False
		if cont: print(f"{f'{inindent}{parent} {cleaned(name)}':<{tree_width}.{tree_width-1}}", sep='', end='')
		if getinfo and cont:
			if getinfo['cpu_times'] == err:
				getinfo['num_threads'] = 0
			cpu = getinfo['cpu_percent'] if proc_per_cpu else (getinfo['cpu_percent'] / psutil.cpu_count())
			print(f"{getinfo['num_threads']:>4} " if getinfo['num_threads'] < 1000 else '999> ',
				f"{getinfo['username']:<9.9}" if len(getinfo['username']) < 10 else f"{getinfo['username'][:8]:<8}+",
				f"{getinfo['memory_percent']:>4.1f}" if getinfo['memory_percent'] < 100 else f"{getinfo['memory_percent']:>4.0f} ",
				f"{cpu:>11.1f} " if cpu < 100 else f"{cpu:>11.0f} ",
				sep='')
		elif cont:
			print(f"{'':>14}{'0.0':>4}{'0.0':>11} ", sep='')
		tree_line_count += 1
		if parent not in tree:
			return
		children = tree[parent][:-1]
		for child in children:
			create_tree(child, tree, indent + " │ ", indent + " ├─ ", found=found)
			if max_lines and tree_line_count >= max_lines:
				break
		child = tree[parent][-1]
		create_tree(child, tree, indent + "  ", indent + " └─ ")

	infolist: Dict = {}
	tree: List = defaultdict(list)
	for p in sorted(psutil.process_iter(['pid', 'name', 'num_threads', 'username', 'memory_percent', 'cpu_percent', 'cpu_times', 'create_time'], err), key=lambda p: eval(sorting), reverse=reverse):
		try:
			tree[p.ppid()].append(p.pid)
		except (psutil.NoSuchProcess, psutil.ZombieProcess):
			pass
		else:
			infolist[p.pid] = p.info
	if 0 in tree and 0 in tree[0]:
		tree[0].remove(0)

	tree_width: int = width + 8

	print(f"{' Tree:':<{tree_width-4}}", 'Threads: ', f"{'User:':<9}Mem%{'Cpu%':>11}", sep='')
	create_tree(min(tree), tree)

def get_disks(exclude: str = None, filtering: str = None):
	'''Get stats, current read and current write for all disks'''
	global disk_hist
	disk_read: int = 0
	disk_write: int = 0
	dev_name: str
	disk_name: str
	disk_list: List[str] = []
	excludes: List[str] = []
	if exclude: excludes = exclude.split(' ')
	if system == "BSD": excludes += ["devfs", "tmpfs", "procfs", "linprocfs", "gvfs", "fusefs"]
	if filtering: filtering: Tuple[str] = tuple(filtering.split(' '))
	io_counters = psutil.disk_io_counters(perdisk=True if system == "Linux" else False, nowrap=True)
	print("Ignored line")
	for disk in psutil.disk_partitions():
		disk_io = None
		disk_name = disk.mountpoint.rsplit('/', 1)[-1] if not disk.mountpoint == "/" else "root"
		while disk_name in disk_list: disk_name += "_"
		disk_list += [disk_name]
		if excludes and disk.fstype in excludes or filtering and not disk_name.endswith(filtering):
			continue
		if system == "MacOS" and disk.mountpoint == "/private/var/vm":
			continue
		try:
			disk_u = psutil.disk_usage(disk.mountpoint)
		except:
			pass
		print(f'{disk.device} {disk_u.total >> 10} {disk_u.used >> 10} {disk_u.free >> 10} {disk_u.percent:.0f} ', end='')
		try:
			if system == "Linux":
				dev_name = os.path.realpath(disk.device).rsplit('/', 1)[-1]
				if dev_name.startswith("md"):
					try:
						dev_name = dev_name[:dev_name.index("p")]
					except:
						pass
				disk_io = io_counters[dev_name]
			elif disk.mountpoint == "/":
				disk_io = io_counters
			else:
				raise Exception
			disk_read = disk_io.read_bytes
			disk_write = disk_io.write_bytes

			disk_read -= disk_hist[disk.device][0]
			disk_write -= disk_hist[disk.device][1]
		except:
			pass
			disk_read = 0
			disk_write = 0

		if disk_io: disk_hist[disk.device] = (disk_io.read_bytes, disk_io.write_bytes)
		print(f'{disk_read >> 10} {disk_write >> 10} {disk_name}')

#* The script takes input over coproc pipes and runs command if in the accepted commands list
while command != 'quit':
	if not psutil.pid_exists(parent_pid):
		quit()
	try:
		command = input()
	except:
		pass
		quit()

	if not command or command == 'test':
		continue
	elif command.startswith(allowed_commands):
		try:
			exec(command)
		except Exception as e:
			pass
			print('\n', '/ERROR')
			print(f'PSUTIL ERROR! Command: {command}\n{e}', file=sys.stderr)
	else:
		continue
	print('/EOL')
	#print(f'{command}', file=sys.stderr)