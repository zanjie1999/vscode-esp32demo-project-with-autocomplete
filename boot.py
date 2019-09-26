# -*- encoding:utf-8 -*-

#import esp
#esp.osdebug(None)
import gc
import webrepl
import time
import network
import machine
from machine import Pin
import utelnetserver

wlanDict = {'ssid':'pwd'}

print()
machine.freq(160000000)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print('Wlan scanning...')
Pin(2, Pin.OUT).value(0)
apScan = wlan.scan()
if Pin(0, Pin.IN).value() == 0:
	print("\nStart cancel\n")
	Pin(2, Pin.OUT).value(1)
else:
	if wlan.isconnected():
		print('Network config:\n', wlan.ifconfig(),'\n')
	else:
		for ssid,pwd in wlanDict.items():
			for ap in apScan:
				if "b'" + ssid + "'" == str(ap[0]):
					if not wlan.isconnected():
						print('Connecting to "'+ ssid +'"...')
						wlan.connect(ssid, pwd)
				
					start = time.time()
					while not wlan.isconnected():
						time.sleep(1)
						if time.time()-start > 10:
							print('Connect to "'+ ssid +'" timeout!')
							break
					
					if wlan.isconnected():
						print('Network "'+ ssid +'" config:\n', wlan.ifconfig(),'\n')
						break
	
		if not wlan.isconnected():
			print('Network ERROR\n')	
	
	webrepl.start()
	utelnetserver.start()
	print("\nHello Sparkle\n")
	gc.collect()
