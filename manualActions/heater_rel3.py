
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(38,GPIO.OUT)
GPIO.output(38,GPIO.HIGH)

try:
	GPIO.output(38,GPIO.LOW)
	print("Relais 1 ON !")
	time.sleep(0.5)
	GPIO.output(38,GPIO.HIGH)
	print("Relais 1 OFF !")
	GPIO.cleanup()

except KeyboardInterrupt:
	print("QUIT")
	GPIO.cleanup()
