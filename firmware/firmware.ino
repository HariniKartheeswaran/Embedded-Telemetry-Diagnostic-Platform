int tempPin = A0;
int soundPin = A1;
int tiltPin = 8;

void setup() {
  Serial.begin(9600);
  pinMode(tiltPin, INPUT);
}

String detectState(int temp, int sound, int tilt) {
  if (tilt == 1) return "TILT_ALERT";
  if (sound > 300) return "NOISE_ALERT";
  if (temp > 500) return "TEMP_HIGH";
  return "NORMAL";
}

void loop() {
  int temp = analogRead(tempPin);
  int sound = analogRead(soundPin);
  int tilt = digitalRead(tiltPin);

  String state = detectState(temp, sound, tilt);

  Serial.print("TEMP:");
  Serial.print(temp);
  Serial.print(",SOUND:");
  Serial.print(sound);
  Serial.print(",TILT:");
  Serial.print(tilt);
  Serial.print(",STATE:");
  Serial.println(state);

  delay(1000);
}