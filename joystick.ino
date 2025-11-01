const int joyX = A0;
const int joyY = A1;
const int buttonPin = 7;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  int xVal = analogRead(joyX);
  int yVal = analogRead(joyY);
  int buttonState = digitalRead(buttonPin);

  Serial.print(xVal);
  Serial.print(",");
  Serial.print(yVal);
  Serial.print(",");
  Serial.println(buttonState);

  delay(100);
}
