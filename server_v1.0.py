import RPi.GPIO as GPIO
import os
import time
import sys
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

#app.run(host='0.0.0.0')

sys.stdout = open('logfile', 'w')
print('Poolboy started')

@app.route('/')

@app.route('/my-link0/')
def my_link0():
  return render_template('index.html')

@app.route('/my-link1/')
def my_link1():
  print ('Main Power got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(32,GPIO.OUT)
  GPIO.output(32,GPIO.LOW)
  print("Relais 1 ON !")
  time.sleep(0.5)
  GPIO.output(32,GPIO.HIGH)
  print("Relais 1 OFF !")
  GPIO.cleanup()
  return render_template('index.html')

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
  GPIO.cleanup()
  return render_template('index.html')

@app.route('/my-link3/')
def my_link3():
  print ('Heizen got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(38,GPIO.OUT)
  GPIO.output(38,GPIO.LOW)
  print("Relais 3 ON !")
  time.sleep(0.5)
  GPIO.output(38,GPIO.HIGH)
  print("Relais 3 OFF !")
  GPIO.cleanup()
  return render_template('index.html')

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
  GPIO.cleanup()
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
