from evdev import InputDevice, categorize, ecodes
from time import sleep
import subprocess
import os
import evdev

def runcmd(cmd):
    out = subprocess.Popen(cmd,
            shell = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            close_fds=True)
    (stdout, stderr) = out.communicate()
    if 'byte' in str(type(stdout)) :
        stdout = stdout.decode("utf-8")
    if 'byte' in str(type(stderr)) :
        stderr = stderr.decode("utf-8")
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
        cmd=cmd1
    elif (num == 2):
        cmd=cmd2
    elif (num == 3):
        cmd=cmd3
    elif (num == 4):
        cmd=cmd4
    print(cmd)
    cmd='su akash -c "%s" &' %(cmd)
    os.system(cmd)
    return (1)


global dev,x_min,x_max,y_min,y_max
def main():
	global dev,x_min,x_max,y_min,y_max
	cmd="cat /proc/bus/input/devices | awk '/[Tt]ouch[Pp]ad/{for(a=0;a<=3;a++){getline;{{ print $NF;}}}}' | tail -1"
	(ret, out, err) = runcmd(cmd)
	device="/dev/input/"+out.strip()
	dev = InputDevice(device)
	cmd="evemu-describe " + device + " | awk '/ABS_X/{for(a=0;a<=2;a++){getline;{{ print $NF;}}}}'"
	(ret, out, err) = runcmd(cmd)
	offset=175
	x_min=int(out.split()[1])+offset
	x_max=int(out.split()[2])-offset
	cmd="evemu-describe " + device + " | awk '/ABS_Y/{for(a=0;a<=2;a++){getline;{{ print $NF;}}}}'"
	(ret, out, err) = runcmd(cmd)
	y_min=int(out.split()[1])+offset
	y_max=int(out.split()[2])-offset
	(ret, out, err) = runcmd("cat /var/shorttouch")
	global cmd1, cmd2, cmd3, cmd4
	if (ret == 0):
		cmd1=out.split("\n")[0]
		cmd2=out.split("\n")[1]
		cmd3=out.split("\n")[2]
		cmd4=out.split("\n")[3]
	else:
		cmd1=""
		cmd2=""
		cmd3=""
		cmd4=""

	for i in range(100):
		print(call_cmd(trig_event()))

if __name__=="__main__":
	main()
