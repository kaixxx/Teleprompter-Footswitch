#!/usr/bin/python
# footswitch_cmd.py
# Author: Kai
# Version: 0.1 - 21.11.2021
# Description: 
# Connects an arduino controlled footswitch to the Imaginary Teleprompter App
# (https://github.com/ImaginarySense/Imaginary-Teleprompter). 
# Works only with the standalone app and the external prompter, not the in-frame one.
# Make sure the you have the "Footswitch_Arduino.ino" sketch loaded onto the Arduino und the 
# footswitch connected between pin 4 and GND.
# Operation:
# - Run this script
# - Load your script in the Imaginary Teleprompter and start the external prompter by clicking "Prompt It!"
# - Pause the prompter with the space key.
# - A short press of the footswitch sends "Page Down" to the teleprompter, scrolling half a page down.
# - A long press (>300ms) starts the automatic scrolling as long as the footswitch is depressed (and stops it when released).

import serial
import time
import pywinauto
from pywinauto.application import Application

arduino_port = 'COM4' # <<<=== Edit this for your setup!

arduino = serial.Serial(arduino_port, baudrate=115200, timeout=.1)

def arduino_read():
    data = arduino.readline()
    return data
    
def teleprompter_cmd(key):
    # Connect to running teleprompter:
    try:
        app = Application(backend="uia").connect(title="Teleprompter Instance")
        win = app.window(title="Teleprompter Instance")
        # send key:
        win.type_keys(key)
    except:
        print("Error: No running Teleprompter instance found.")
        return 0
    return 1
    
while True:
    value = arduino_read()
    if value:
        value = str(value, encoding='utf-8', errors='strict').strip()
        # value = value.strip()
        # print(value) # printing the value
        if value == "Arduino Footswitch":
            print("Footswitch connected")
        elif value == 'SP':
            print("> PgDwn Cmd")
            teleprompter_cmd(u'{PGDN}')
        elif value == 'LP_START':
            print("> Start Cmd")
            teleprompter_cmd(u'{SPACE}')
        elif value == 'LP_STOP':
            print("> Stop Cmd")
            teleprompter_cmd(u'{SPACE}')
        else:
            print("Unknown command: " + value)
            