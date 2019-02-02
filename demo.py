from evdev import InputDevice, categorize, ecodes
from time import sleep
import subprocess
import os
import evdev


dev = InputDevice('/dev/input/event5')
x_min=1600
y_min=1600
x_max=5100
y_max=4300

def runcmd(cmd):
    out = subprocess.Popen(cmd,
            shell = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            close_fds=True)
    (stdout,stderr) = out.communicate()
    ret =  (out.returncode)
    return (ret, stdout ,stderr)

def scan_touch(*args):
	x_cord=y_cord=0
	for event in dev.read_loop():
		ts=event.timestamp()
		if (event.code == 0  and event.value !=0):
			x_cord=event.value
		if (event.code == 1  and event.value !=0):
			y_cord=event.value
		if (x_cord != 0 and y_cord != 0):
			break
	return (x_cord, y_cord, ts)

def type_touch(*args):
	(x_cord, y_cord, ts) = scan_touch()
	if (x_cord < x_min) and (y_cord < y_min):
		return("upper left")
	elif (x_cord < x_min) and (y_cord > y_max):
		return("lower left")
	elif (x_cord > x_max) and (y_cord < y_min):
		return("upper right")
	elif (x_cord > x_max) and (y_cord > y_max):
		return("lower right")
	else:
		return("somewhere middle")

def trig_event(*args):
    tt1=type_touch()
    tt2=type_touch()
    while(True):
        if tt1 != tt2:
            if (tt2 == "upper left"):
                return 1
            elif (tt2 == "upper right"):
                return 2
            elif (tt2 == "lower left"):
                return 3
            elif (tt2 == "lower right"):
                return 4
            else:
                tt2=tt1
                tt1=type_touch()
        else:
            tt2=tt1
            tt1=type_touch()
def call_cmd(num):
    if (num == 1):
        cmd='ls /tmp'
    elif (num == 2):
        cmd='ls /var'
    elif (num == 3):
        cmd='ls ~/'
    elif (num == 4):
        cmd='ls /home/prakersh/'
    (ret,out,err)=runcmd(cmd)
    print(cmd)
    return (out)

for i in range(100):
	print(call_cmd(trig_event()))


"""

for event in dev.read_loop():
	out = (type_touch(event))
	if out != None:
		print(out)

"""
