# This script runs the startup sequence in
# accordance with the ignition switch and
# wiring diagram for my vehicle (Jeep GC WJ)

import CHIP_IO.GPIO as GPIO
import time
import sys

sleepRunStart = 3
sleepRun = 4
sleepIgnitionStart = 1
gpioRunStart = "CSID0"
gpioRun = "CSID1"
gpioIgnitionStart = "CSID2"
gpioIDK = "CSID3"
gpio = [gpioRun, gpioRunStart, gpioIgnitionStart, gpioIDK]

def highlow(inGPIO):
  if GPIO.input(inGPIO):
    return "HIGH"
  else:
    return "LOW"

def initialize():
  for i in gpio:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)

def clear():
  for i in gpio:
    GPIO.output(i, GPIO.LOW)

def confirmation(inGPIO):
  print('confirmation: {}'.format(highlow(inGPIO)))

def flipOn(inGPIO):
  GPIO.output(inGPIO, GPIO.HIGH)

def final():
  print("Start sequence finished!!!")

def gotinput(message):
  try:
    input(message)
  except SyntaxError:
    pass

def Am_I_Serious():
  if len(sys.argv) == 2:
    if str(sys.argv[1]) == 'superdooperserial':
      return True

def sequence():
  # run-start position
  print("Run-Start Position")
  GPIO.output(gpioRunStart, GPIO.HIGH)
  confirmation(gpioRunStart)
  time.sleep(sleepRunStart)

  # run position 
  print("Run Position")
  GPIO.output(gpioRun, GPIO.HIGH)
  confirmation(gpioRun)
  time.sleep(sleepRun)

  # Start it!
  print("Start position")
  if Am_I_Serious():
    print("Cranking!!!")
    GPIO.output(gpioIgnitionStart, GPIO.HIGH)
    confirmation(gpioIgnitionStart)
    time.sleep(sleepIgnitionStart)
    GPIO.output(gpioIgnitionStart, GPIO.LOW)
    confirmation(gpioIgnitionStart)
  else:
    print("no balls, get some and try again later")

  # Press enter to stop car
  gotinput("Started! Press enter to stop the jeep....")
  
  clear()

def main():
  initialize()
  clear()
  sequence()
  final()

if __name__ == "__main__":
    main()
