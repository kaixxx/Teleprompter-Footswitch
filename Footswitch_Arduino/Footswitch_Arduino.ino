/* 
 * Arduino Footswitch
 * 
 * 21.11.2021
 *  
 * Connect footswitch betqween pin 4 an GND
 * No pullup resistor needed, using the Arduino's (Atmega's) internal pullup resistor
 *  
 * Commands:
 *  "SP" = short press (<300ms)
 *  "LP_START" = long press start (>300ms)
 *  "LP_STOP" = long press stop/release
*/

#include "ClickButton.h"

// the footswitch
const int buttonPin1 = 4;
ClickButton button1(buttonPin1, LOW, CLICKBTN_PULLUP);

// long press
boolean longPress = false;
int function = 0;


void setup()
{
  Serial.begin(115200); 
  Serial.println("Arduino Footswitch");
  
  pinMode(LED_BUILTIN, OUTPUT);

  // Setup button timers (all in milliseconds / ms)
  // (These are default if not set, but changeable for convenience)
  button1.debounceTime   = 20;   // Debounce timer in ms
  button1.multiclickTime = 0;  // Time limit for multi clicks (default: 250. "0" disables doubleclicks but speeds up single click response)
  button1.longClickTime  = 300; // time until "held-down clicks" register (default: 1000)
}


void loop()
{
  button1.Update();

  if(button1.depressed) {
    digitalWrite(LED_BUILTIN, HIGH);
    /*
    if(longPress == false) {      // start longPress
      longPress = true;
      Serial.println("START");
    }
    */
  } else {
    digitalWrite(LED_BUILTIN, LOW);
    /*
    if(longPress) {      // stop longPress
      longPress = false;
      Serial.println("STOP");
    }
    */
  }

  if (button1.clicks != 0) {
    function = button1.clicks;
  }
  
  // Short Press
  if(button1.clicks == 1) {
    Serial.println("SP");
  }

  // scroll if button is held down during single-click
  if(function == -1 && button1.depressed == true)
  {
    if(longPress == false) {      // start longPress
      longPress = true;
      Serial.println("LP_START");
    }
  } else if(longPress) {         // long press released
    longPress = false;
    Serial.println("LP_STOP");
    // Reset function
    function = 0;
  }
}
