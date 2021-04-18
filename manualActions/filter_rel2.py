
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(36,GPIO.OUT)
GPIO.output(36,GPIO.HIGH)

try:
	GPIO.output(36,GPIO.LOW)
	print("Relais 1 ON !")
	time.sleep(0.5)
	GPIO.output(36,GPIO.HIGH)
	print("Relais 1 OFF !")
	GPIO.cleanup()

except KeyboardInterrupt:
	print("QUIT")
	GPIO.cleanup()
