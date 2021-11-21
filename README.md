# Teleprompter-Footswitch
Arduino controlled footswitch for the Imaginary Teleprompter App

![demo](./gif/footswitch.gif)

Author: Kai
Version: 0.1 - 21.11.2021

Imaginary Teleprompter App: https://github.com/ImaginarySense/Imaginary-Teleprompter 

Works only with the standalone app and the external prompter, not the in-frame one. Windows only, sorry.
Make sure the you have the "Footswitch_Arduino.ino" sketch loaded onto the Arduino and the footswitch connected between pin 4 and GND. I am using the foot pedal from my keyboard.
The script "footswitch_cmd.py" is written for Python 3 and needs pyserial and pywinauto to be installed. Adjust the COM-Port in the script to your system. 

## Operation:
- Run footswitch_cmd.py and watch the output: It should say "Footswitch connected". Otherwise check the serial port in the script.
- Load your text in Imaginary Teleprompter and start the external prompter by clicking "Prompt It!".
- Pause the prompter with the space key on your keyboard.
- A short press of the footswitch sends "Page Down" to the teleprompter, scrolling half a page down.
- A long press (>300ms) starts the automatic scrolling as long as the footswitch is depressed (and stops it when released).
