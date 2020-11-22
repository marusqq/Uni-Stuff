// author: Marius Pozniakovas
// project: Fake Bomb
// equipment used: 2x button, ultrasound distance detector, 2x buzzer, 2x led

#include <Reactduino.h>

//ultrasound
#define echoPin 7
#define trigPin 6

//buzzers
#define buzz1Pin 4
#define buzz2Pin 5

//leds
#define ledGreenPin 12
#define ledRedPin 18

//button variables
#define buttonPin1 2
#define buttonPin2 3

boolean SOUND = true;

void check_for_defusal() {

  Serial.println("Checking for defusal...");
  int button1State, button2State;
  button1State = digitalRead(buttonPin1);
  button2State = digitalRead(buttonPin2);

  if (button1State == 0 && button2State == 0) {
    start_defusal();
  }
    
}

void defused() {
  
  Serial.println("You have defused the bomb");
  while(true) {
    delay(5000);
  }
}

void boom() {
  Serial.println("You died");
  while(true) {
    delay(5000);
  }
}

void explosion() {

  Serial.println("Bomb Case Opened! Boom boom soon!");
  int run_away = 30;
  while (run_away) {
    noTone(buzz1Pin);
    if (SOUND)
      tone(buzz1Pin, 2500);
    digitalWrite(ledRedPin, true);
    digitalWrite(ledGreenPin, true);
    delay(50);
    
    noTone(buzz2Pin);
    if (SOUND)
      tone(buzz2Pin, 1500);
    digitalWrite(ledRedPin, false);
    digitalWrite(ledGreenPin, false);
    delay(100);

    run_away--; 
  }
  
  if (SOUND)
    tone(buzz2Pin, 1500);
  if (SOUND)
    tone(buzz1Pin, 2500);
  digitalWrite(ledRedPin, true);
  digitalWrite(ledGreenPin, true);
  boom();
}

void calculate_distance_in_box() {
  
  int duration;
  int distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); //returns the sound wave travel time
  distance = duration * 0.034 / 2;   // Calculating the distance

  if (distance > 15) {
    explosion();
  }
  
}

void start_defusal() {
  int button1State, button2State;
  int time_now;
  boolean first_part = true;
  boolean second_part = false;
  boolean third_part = false;
  
  Serial.println("Starting bomb defusal..");
  //start defusing...
  time_now = millis() + 5000;
  noTone(buzz1Pin);
  if (SOUND)
    tone(buzz2Pin, 2500);
  while (millis() <= time_now) {
    delay(20);
    digitalWrite(ledGreenPin, true);
    digitalWrite(ledRedPin, true);
    delay(20);
    noTone(buzz2Pin);
    digitalWrite(ledGreenPin, false);
    digitalWrite(ledRedPin, false);

    button1State = digitalRead(buttonPin1);
    button2State = digitalRead(buttonPin2);
    
    if (first_part) {
      if (button1State == 1 && button2State == 0){
        second_part = true;
        first_part = false;
        delay(500);
        Serial.println("First part done");
      }
    }

    else if (second_part) {
      if (button1State == 0 && button2State == 0){
        third_part = true;
        second_part = false;
        delay(500);
        Serial.println("Second part done");
      }
    }
    
    if (third_part) {
      if (button1State == 0 && button2State == 1){
        noTone(buzz2Pin);
        noTone(buzz1Pin);
        digitalWrite(ledGreenPin, false);
        digitalWrite(ledRedPin, false);
        Serial.println("Third part done");
        defused();
      }
    }
  }
  
  noTone(buzz2Pin);
  if (SOUND)
    tone(buzz1Pin, 2500);
  explosion();
}

void blink_other() {
  static bool state = false;
  digitalWrite(ledGreenPin, state = !state);
}

void blink_red_and_buzz() {
  
  digitalWrite(ledRedPin, true);
  if (SOUND)
    tone(buzz2Pin, 2500);
  
  delay(200);

  noTone(buzz2Pin);
  digitalWrite(ledRedPin, false);
  
}

void app_main() {

  //setup pins
  //------------------------------
  pinMode(ledRedPin, OUTPUT);
  pinMode(ledGreenPin, OUTPUT);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);

  //setup variables
  //------------------------------
  int freq_red_buzz = 1600;
     
  reaction other_blink;
  reaction timer_blink;
  


  //setup objects
  //------------------------------
  Serial.begin(9600);
  
  
  //registrating synch steps
  //-------------------------------
  
  //blinking yellow for bomb defusal
  other_blink = app.repeat(freq_red_buzz * 2, blink_other);

  //blinking red and buzzer buzzing for timer
  timer_blink = app.repeat(freq_red_buzz, blink_red_and_buzz);

  //check if the bomb is not stolen
  app.repeat(10, calculate_distance_in_box);
  
  //check for double button clicks
  app.repeat(10, check_for_defusal);
  
}

Reactduino app(app_main);
