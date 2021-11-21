# Teleprompter-Footswitch
Arduino controlled footswitch for the Imaginary Teleprompter App

![demo](./gif/footswitch.gif)

Author: Kai
Version: 0.1 - 21.11.2021

Connects an arduino controlled footswitch to the Imaginary Teleprompter App (https://github.com/ImaginarySense/Imaginary-Teleprompter). 

Works only with the standalone app and the external prompter, not the in-frame one.
Make sure the you have the "Footswitch_Arduino.ino" sketch loaded onto the Arduino and the footswitch connected between pin 4 and GND. I am using the foot pedal from my keyboard.

## Operation:
- Run this script.
- Load your script in the Imaginary Teleprompter and start the external prompter by clicking "Prompt It!".
- Pause the prompter with the space key.
- A short press of the footswitch sends "Page Down" to the teleprompter, scrolling half a page down.
- A long press (>300ms) starts the automatic scrolling as long as the footswitch is depressed (and stops it when released).
