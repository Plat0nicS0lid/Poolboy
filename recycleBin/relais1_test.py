
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)

try:
	channel_is_on = GPIO.input(32)
        if channel_is_on:
        	print("GPIO input is OFF !")
	GPIO.output(32,GPIO.LOW)
	print("Relais 1 ON !")
	time.sleep(0.5)
	channel_is_on = GPIO.input(32)
	if not channel_is_on:
    		print("GPIO input is ON !")
	GPIO.output(32,GPIO.HIGH)
	print("Relais 1 OFF !")
        channel_is_on = GPIO.input(32)
        if channel_is_on:
                print("GPIO input is OFF !")
	GPIO.cleanup()

except KeyboardInterrupt:
	print("QUIT")
	GPIO.cleanup()
