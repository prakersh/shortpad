from evdev import InputDevice, categorize, ecodes
import evdev

dev = InputDevice('/dev/input/event5')

for event in dev.read_loop():
	if event.code == 0 and event.value !=0:
		print("x-coordinate = ",event.value)
	elif event.code == 1 and event.value !=0:
		print("y-coordinate = ",event.value)
		
