import re

dir_led="/sys/class/leds/led0"
original_use=None

def led_claim():
	"Take control of the LED"
	global original_use
	trigger_file = dir_led+"/trigger"
	with open(trigger_file, 'r') as f:
		m = re.match('\[(.*)\]', f.read())
	if m:
		original_use = m.group(1)
	else:
		original_use = None
	with open(trigger_file, 'w') as f:
		f.write('none')

def led_release():
	"relinquish control of the LED"
	global original_use
	if original_use:
		with open(dir_led+"/trigger", 'w') as f:
			f.write(original_use)

def led_on():
	"turn the led on"
	with open(dir_led+"/brightness", 'w') as f:
		f.write('255')

def led_off():
	"turn the LED off"
	with open(dir_led+"/brightness", 'w') as f:
		f.write('0')

import time

#def main():
led_claim()
for i in range(100):
	print("on")
	led_on()
	time.sleep(1)
	print("off")
	led_off()
	time.sleep(1)
	led_release()
# return 0
