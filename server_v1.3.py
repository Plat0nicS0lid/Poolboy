import RPi.GPIO as GPIO
import os
import time
import sys
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

#app.run(host='0.0.0.0')

sys.stdout = open('/opt/Poolboy/poolboy_web.log', 'w')
print ('Poolboy webapp started')

GPIO.setmode(GPIO.BOARD)

	
@app.route('/')
def index():
  GPIO.setmode(GPIO.BOARD)
  filterstat = 31
  buttonSts = GPIO.LOW
  # Read Sensors Status
  GPIO.setup(filterstat, GPIO.IN)   
  buttonSts = GPIO.input(filterstat)
  templateData = {
    'filterbutton'  : buttonSts,
  }
  return render_template('index.html', **templateData)
  GPIO.cleanup()

@app.route('/my-link1/')
def my_link1():
  print ('Main Power got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(38,GPIO.OUT)
  GPIO.output(38,GPIO.LOW)
  print("Relais 1 ON !")
  time.sleep(0.5)
  GPIO.output(38,GPIO.HIGH)
  print("Relais 1 OFF !")
  filterstat = 31
  buttonSts = GPIO.LOW
  # Read Sensors Status
  GPIO.setup(filterstat, GPIO.IN)
  buttonSts = GPIO.input(filterstat)
  templateData = {
  'filterbutton'  : buttonSts,
  }
  return render_template('index.html', **templateData)
  GPIO.cleanup()


@app.route('/my-link2/')
def my_link2():
  print ('Filtern got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(36,GPIO.OUT)
  GPIO.output(36,GPIO.LOW)
  print("Relais 2 ON !")
  time.sleep(0.5)
  GPIO.output(36,GPIO.HIGH)
  print("Relais 2 OFF !")
  filterstat = 31
  buttonSts = GPIO.LOW
  # Read Sensors Status
  GPIO.setup(filterstat, GPIO.IN)
  buttonSts = GPIO.input(filterstat)
  templateData = {
  'filterbutton'  : buttonSts,
  }
  return render_template('index.html', **templateData)
  GPIO.cleanup()

@app.route('/my-link3/')
def my_link3():
  print ('Heizen got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(32,GPIO.OUT)
  GPIO.output(32,GPIO.LOW)
  print("Relais 3 ON !")
  time.sleep(0.5)
  GPIO.output(32,GPIO.HIGH)
  print("Relais 3 OFF !")
  filterstat = 31
  buttonSts = GPIO.LOW
  # Read Sensors Status
  GPIO.setup(filterstat, GPIO.IN)
  buttonSts = GPIO.input(filterstat)
  templateData = {
  'filterbutton'  : buttonSts,
  }
  return render_template('index.html', **templateData)
  GPIO.cleanup()

@app.route('/my-link4/')
def my_link4():
  print ('Bubbles got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(40,GPIO.OUT)
  GPIO.output(40,GPIO.LOW)
  print("Relais 4 ON !")
  time.sleep(0.5)
  GPIO.output(40,GPIO.HIGH)
  print("Relais 4 OFF !")
  filterstat = 31
  buttonSts = GPIO.LOW
  # Read Sensors Status
  GPIO.setup(filterstat, GPIO.IN)
  buttonSts = GPIO.input(filterstat)
  templateData = {
  'filterbutton'  : buttonSts,
  }
  return render_template('index.html', **templateData)
  GPIO.cleanup()

@app.route('/my-link5/')
def my_link5():
  print ('Temp high got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(35,GPIO.OUT)
  GPIO.output(35,GPIO.LOW)
  print("Relais 5 ON !")
  time.sleep(0.5)
  GPIO.output(35,GPIO.HIGH)
  print("Relais 5 OFF !")
  filterstat = 31
  buttonSts = GPIO.LOW
  # Read Sensors Status
  GPIO.setup(filterstat, GPIO.IN)
  buttonSts = GPIO.input(filterstat)
  templateData = {
  'filterbutton'  : buttonSts,
  }
  return render_template('index.html', **templateData)
  GPIO.cleanup()

@app.route('/my-link6/')
def my_link6():
  print ('Temp low got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(37,GPIO.OUT)
  GPIO.output(37,GPIO.LOW)
  print("Relais 6 ON !")
  time.sleep(0.5)
  GPIO.output(37,GPIO.HIGH)
  print("Relais 6 OFF !")
  filterstat = 31
  buttonSts = GPIO.LOW
  # Read Sensors Status
  GPIO.setup(filterstat, GPIO.IN)
  buttonSts = GPIO.input(filterstat)
  templateData = {
  'filterbutton'  : buttonSts,
  }
  return render_template('index.html', **templateData)
  GPIO.cleanup()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
