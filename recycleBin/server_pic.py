import RPi.GPIO as GPIO
import os
import time
import sys
from flask import Flask, render_template
app = Flask(__name__)

PEOPLE_FOLDER = os.patch.join('templates')

app.config['UPLOAD_FOLDER'] = PICTURE_FOLDER

#app.run(host='0.0.0.0')

sys.stdout = open('logfile', 'w')
print('Poolboy started')


@app.route('/')
def index():
  full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'poolboy.png')
  return render_template('index.html'), poolboy_image = full_filename

@app.route('/my-link1/')
def my_link1():
  print ('I got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(32,GPIO.OUT)
  GPIO.output(32,GPIO.HIGH)
  GPIO.output(32,GPIO.LOW)
  print("Relais 1 ON !")
  time.sleep(0.5)
  GPIO.output(32,GPIO.HIGH)
  print("Relais 1 OFF !")
  GPIO.cleanup()
  return render_template('index.html')

@app.route('/my-link2/')
def my_link2():
  print ('I got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(36,GPIO.OUT)
  GPIO.output(36,GPIO.HIGH)
  GPIO.output(36,GPIO.LOW)
  print("Relais 2 ON !")
  time.sleep(0.5)
  GPIO.output(36,GPIO.HIGH)
  print("Relais 2 OFF !")
  GPIO.cleanup()
  return render_template('index.html')


@app.route('/my-link3/')
def my_link3():
  print ('I got clicked!')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(38,GPIO.OUT)
  GPIO.output(38,GPIO.HIGH)
  GPIO.output(38,GPIO.LOW)
  print("Relais 3 ON !")
  time.sleep(0.5)
  GPIO.output(38,GPIO.HIGH)
  print("Relais 3 OFF !")
  GPIO.cleanup()
  return render_template('index.html')



if __name__ == '__main__':
  app.run(debug=True)
