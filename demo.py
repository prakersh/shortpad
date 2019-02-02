from evdev import InputDevice, categorize, ecodes
from time import sleep
import evdev


dev = InputDevice('/dev/input/event5')
x_min=1600
y_min=1600
x_max=5100
y_max=4300
	
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


for i in range(100):
	print(type_touch())
	sleep(0.1)

"""

for event in dev.read_loop():
	out = (type_touch(event))
	if out != None:
		print(out) 

"""		
