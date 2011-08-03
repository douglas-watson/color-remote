/*
  Serial RGB controller
 
 Reads a serial input string looking for three comma-separated
 integers with a newline at the end. Values should be between 
 0 and 255. The sketch uses those values to set the color 
 of an RGB LED attached to pins 9 - 11.
 
 The circuit:
 * Common-anode RGB LED cathodes attached to pins 9 - 11
 * LED anode connected to pin 13
 
 To turn on any given channel, set the pin LOW.  
 To turn off, set the pin HIGH. The higher the analogWrite level,
 the lower the brightness.
 
 created 29 Nov 2010
 by Tom Igoe
 
 This example code is in the public domain. 

 modified 4th Aug 2011
 by Douglas Watson
 */

String inString = "";    // string to hold input
int currentColor = 0;
int red, green, blue = 0;

void setup() {
  // Initialize serial communications:
  Serial.begin(9600);
  // set LED cathode pins as outputs:
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  int inChar;

  // Read serial input:
  if (Serial.available() > 0) {
    inChar = Serial.read();
  }

  if (isDigit(inChar)) {
    // convert the incoming byte to a char 
    // and add it to the string:
    inString += (char)inChar; 
  }

  // if you get a comma, convert to a number,
  // set the appropriate color, and increment
  // the color counter:
  if (inChar == ',') {
    // do something different for each value of currentColor:
    switch (currentColor) {
    case 0:    // 0 = red
      red = inString.toInt();
      // clear the string for new input:
      inString = ""; 
      break;
    case 1:    // 1 = green:
      green = inString.toInt();
      // clear the string for new input:
      inString = ""; 
      break;
    }
    currentColor++;
  }
  // if you get a newline, you know you've got
  // the last color, i.e. blue:
  if (inChar == '\n') {
    blue = inString.toInt();

    // set the levels of the LED.
    // subtract value from 255 because a higher
    // analogWrite level means a dimmer LED, since
    // you're raising the level on the anode:
    analogWrite(10,  red);
    analogWrite(9, green);
    analogWrite(11, blue);

    // clear the string for new input:
    inString = ""; 
    // reset the color counter:
    currentColor = 0;

  }

}
