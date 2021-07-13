import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BOARD)  
GPIO.setwarnings(False)

FILTER = 31
RUN_FILTER = 36

# Setup FILTER 
#GPIO.setup(FILTER, GPIO.OUT) # This line is only for demo if no real 3,3v input will be used.
GPIO.setup(FILTER, GPIO.IN) # Comment this line in case the demo ones wants to be used.
GPIO.setup(RUN_FILTER, GPIO.OUT)
#GPIO.output(FILTER, GPIO.LOW) # This is also for demo. Set to HIGH to set input ON.
GPIO.output(RUN_FILTER,GPIO.LOW)

FILTER_IS_ON = GPIO.input(FILTER)

if not FILTER_IS_ON:
	# print("Filter is OFF! 31")
	GPIO.output(36,GPIO.LOW)
	# print("Relais 1 ON! 36")
	time.sleep(0.5)
	GPIO.output(36,GPIO.HIGH)
	# print("Relais 1 OFF! 36")
	GPIO.cleanup()
	f = open("/opt/Poolboy/cronActions/poolboy.log","a")
	f.write(datetime.now().__str__())
	#f.write(datetime.now().__str__() + "\n")
	f.write(" filter_on - Filter is OFF! Relais 2 / Filter on!")
	f.write("\n")
	f.close()

if FILTER_IS_ON:
	# print("Filter is already ON! 31")
	GPIO.cleanup()
        f = open("poolboy.log","a")
	f.write(datetime.now().__str__())
        f.write(" filter_on - Filter is already ON! Relais 2 / Filter will not be touched!")
	f.write("\n")
        f.close()


