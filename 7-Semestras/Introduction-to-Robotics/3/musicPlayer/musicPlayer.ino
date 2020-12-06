#include "pitches.h"
#include "songs.h"
#include "BluetoothSerial.h"
#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "PC_Nets"; 
const char* password = "qumd-6f6o-s7i4";  

IPAddress local_IP(192, 168, 1, 2);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 0, 0);

WebServer server(80);

BluetoothSerial ESP_BT;

#define buzzerPin 25

#define CLed 26
#define DLed 18
#define ELed 19
#define FLed 33
#define GLed 22
#define ALed 21
#define BLed 27

int incoming;
int song_playing = 0;
int BTinput;
int new_BTinput;

void setup() {

  Serial.begin(115200);

  //config and connect to wifi
  WiFi.config(local_IP, gateway, subnet);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  //now config the server
  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);
  server.begin();

  //we will need this for random playing of music
  randomSeed(analogRead(0));
  
  //setup bluetooth
  ESP_BT.begin("ESP32-Music_Box");
  
  //set buzzer output pins
  pinMode(buzzerPin, OUTPUT);

  //set led output pins
  pinMode(CLed, OUTPUT);
  pinMode(DLed, OUTPUT);
  pinMode(ELed, OUTPUT);
  pinMode(FLed, OUTPUT);
  pinMode(GLed, OUTPUT);
  pinMode(ALed, OUTPUT);
  pinMode(BLed, OUTPUT);

  //sing(6);
  
}

void loop() {

  //handle the client on needed steps
  server.handleClient();
  
  //if bluetooth is available, read the signals
  if (ESP_BT.available()) {
    incoming = ESP_BT.read();
    //ESP_BT.print("Input:");ESP_BT.println(incoming);
    int songNo = incoming - 48;

    //if the number is more than 0 and less than song_count
    if (songNo > 0 && songNo <= song_count) {

      String song_name = "";
      if (songNo < 1 || songNo > song_count)
        song_name = "None";
      else 
        song_name = song_names[songNo - 1];
      

      ESP_BT.print("Playing song: ");
      ESP_BT.println(song_name);

      //set the global variable
      song_playing = songNo;
      
      //sing the song =]
      sing(songNo);
    }
    
    // ignore them as they are random inputs from bluetooth
    else if (incoming == 10 || incoming == 13)
      delay(1);


    else if (incoming == 33) {
      //for every song print the name of it
      for (int song_id = 0; song_id < song_count; song_id++) { 
        ESP_BT.print(song_id+1);
        ESP_BT.print(": ");
        ESP_BT.println(song_names[song_id]);
      }
    }

    else if (incoming == 112) 
      play_all_songs();
      
    else {
      ESP_BT.print("Enter ! for list of available songs and then enter a corresponding number. ");
      ESP_BT.println("Or enter p to play all songs in shuffle mode");
    }
  }

  //wait for a bit
  delay(20);

  

}

void play_all_songs() {

  ESP_BT.println("Started playing all songs in shuffle mode");
  while (true) {
    int song_playing = random(song_count);
    ESP_BT.print("Playing Song: ");ESP_BT.println(song_names[song_playing-1]);
    
    sing(song_playing);
    
    if (ESP_BT.available()) {
      int new_BTinput = ESP_BT.read();
      if (new_BTinput != 13 && new_BTinput != 10)
        int BTinput = new_BTinput;
      //ESP_BT.print("BTInput:");ESP_BT.println(new_BTinput);

      if (BTinput == 112) {
        ESP_BT.println("Exiting playing all songs in shuffle mode");
        return;
      }
    }

    delay(100);
  }
}

void handle_OnConnect() {

  server.send(200, "text/html", sendHTML(song_playing)); 
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}

void sing(int song) {

    if (song == 1) {
        
        Serial.println("Playing song 1");
        
        int size = sizeof(song1_melody) / sizeof(int);
        
        for (int thisNote = 0; thisNote < size; thisNote++) {
          //calculate note's length
          int noteDuration = 1000 / song1_tempo[thisNote];
          //buzz for note's length
          buzz(buzzerPin, song1_melody[thisNote], noteDuration);

          //wait for the same time
          delay(noteDuration * 1.3);
          
          //stop the tone
          buzz(buzzerPin, 0, noteDuration);

        }
    }

    else if (song == 2) {
        //Serial.println("Playing song 2");
        int size = sizeof(song2_melody) / sizeof(int);
        
        for (int thisNote = 0; thisNote < size; thisNote++) {
          //calculate note's length
          int noteDuration = 1000 / song2_tempo[thisNote];
          //buzz for note's length
          buzz(buzzerPin, song2_melody[thisNote], noteDuration);

          //wait for the same time
          delay(noteDuration * 1.3);
          
          //stop the tone
          buzz(buzzerPin, 0, noteDuration);
        }
    }

    else if (song == 3) {
        //Serial.println("Playing song 3");
        int size = sizeof(song3_melody) / sizeof(int);
        
        for (int thisNote = 0; thisNote < size; thisNote++) {
          //calculate note's length
          int noteDuration = 1000 / song3_tempo[thisNote];
          //buzz for note's length
          buzz(buzzerPin, song3_melody[thisNote], noteDuration);

          //wait for the same time
          delay(noteDuration * 1.3);
          
          //stop the tone
          buzz(buzzerPin, 0, noteDuration);
        }
    }

    else if (song == 4) {
        //Serial.println("Playing song 4");
        int size = sizeof(song4_melody) / sizeof(int);
        
        for (int thisNote = 0; thisNote < size; thisNote++) {
          int noteDuration = 1000 / song4_tempo[thisNote];
          buzz(buzzerPin, song4_melody[thisNote], noteDuration);
          delay(noteDuration * 1.3);
          buzz(buzzerPin, 0, noteDuration);
        }
    }

    else if (song == 5) {
        int size = sizeof(song5_melody) / sizeof(int);
        
        for (int thisNote = 0; thisNote < size; thisNote++) {
          int noteDuration = 1000 / song5_tempo[thisNote];
          buzz(buzzerPin, song5_melody[thisNote], noteDuration);
          delay(noteDuration * 1.3);
          buzz(buzzerPin, 0, noteDuration);
        }
    }

    else if (song == 6) {
        int size = sizeof(song6_melody) / sizeof(int);
        
        for (int thisNote = 0; thisNote < size; thisNote++) {
          int noteDuration = 1000 / song6_tempo[thisNote];
          buzz(buzzerPin, song6_melody[thisNote], noteDuration);
          delay(noteDuration * 1.3);
          buzz(buzzerPin, 0, noteDuration);
        }
    }

    else if (song == 7) {
        int size = sizeof(song7_melody) / sizeof(int);
        
        for (int thisNote = 0; thisNote < size; thisNote++) {
          int noteDuration = 1000 / song7_tempo[thisNote];
          buzz(buzzerPin, song7_melody[thisNote], noteDuration);
          delay(noteDuration * 1.3);
          buzz(buzzerPin, 0, noteDuration);
        }
    }

    else {
      delay(1);
    }
}

void buzz(int targetPin, long frequency, long length) {
  

  leds(frequency, true);

  //calculate the delay between transitions
  //two halfs and freq
  long delayValue = 1000000/ (frequency + 0.01) / 2;

  //cycles per second by the number of seconds
  long numCycles = frequency * length / 1000;

  for (long i = 0; i < numCycles; i++) {
    digitalWrite(targetPin, HIGH);
    delayMicroseconds(delayValue);
    digitalWrite(targetPin, LOW);
    delayMicroseconds(delayValue);
  }

  //turn off leds
  leds(frequency, false);
  

}

void leds(int freq, boolean mode) {

    //C note
    
    if (
      freq == _C1 || freq == _CS1 || 
      freq == _C2 || freq == _CS2 || 
      freq == _C3 || freq == _CS3 || 
      freq == _C4 || freq == _CS4 || 
      freq == _C5 || freq == _CS5 || 
      freq == _C6 || freq == _CS6 ||  
      freq == _C7 || freq == _CS7 ||
      freq == _C8 || freq == _CS8) {
        
      if (mode)
        digitalWrite(CLed, HIGH);
      else
        digitalWrite(CLed, LOW);
    }
        
    // D note
    if (
      freq == _D1 || freq == _DS1 || 
      freq == _D2 || freq == _DS2 || 
      freq == _D3 || freq == _DS3 || 
      freq == _D4 || freq == _DS4 || 
      freq == _D5 || freq == _DS5 || 
      freq == _D6 || freq == _DS6 ||  
      freq == _D7 || freq == _DS7 ||
      freq == _D8 || freq == _DS8) {
        
      if (mode)
        digitalWrite(DLed, HIGH);
      else
        digitalWrite(DLed, LOW);
    }

    //E note
    if (
      freq == _E1 || 
      freq == _E2 ||
      freq == _E3 ||
      freq == _E4 ||
      freq == _E5 ||
      freq == _E6 || 
      freq == _E7) {
        
      if (mode)
        digitalWrite(ELed, HIGH);
      else
        digitalWrite(ELed, LOW);
      }
      
    //F note
    if (
      freq == _F1 || freq == _FS1 || 
      freq == _F2 || freq == _FS2 || 
      freq == _F3 || freq == _FS3 || 
      freq == _F4 || freq == _FS4 || 
      freq == _F5 || freq == _FS5 || 
      freq == _F6 || freq == _FS6 ||  
      freq == _F7 || freq == _FS7) {
        
      if (mode)
        digitalWrite(FLed, HIGH);
      else
        digitalWrite(FLed, LOW);
    }

    //G note
    if (
      freq == _G1 || freq == _GS1 || 
      freq == _G2 || freq == _GS2 || 
      freq == _G3 || freq == _GS3 || 
      freq == _G4 || freq == _GS4 || 
      freq == _G5 || freq == _GS5 || 
      freq == _G6 || freq == _GS6 ||  
      freq == _G7 || freq == _GS7) {
        
      if (mode)
        digitalWrite(GLed, HIGH);
      else
        digitalWrite(GLed, LOW);
    }

    //A note
    if (
      freq == _A1 || freq == _AS1 || 
      freq == _A2 || freq == _AS2 || 
      freq == _A3 || freq == _AS3 || 
      freq == _A4 || freq == _AS4 || 
      freq == _A5 || freq == _AS5 || 
      freq == _A6 || freq == _AS6 ||  
      freq == _A7 || freq == _AS7) {
        
      if (mode)
        digitalWrite(ALed, HIGH);
      else
        digitalWrite(ALed, LOW);
    }

    //B note
    if (
      freq == _B0 ||
      freq == _B1 ||
      freq == _B2 || 
      freq == _B3 ||
      freq == _B4 ||
      freq == _B5 ||
      freq == _B6 ||  
      freq == _B7) {
        
      if (mode)
        digitalWrite(BLed, HIGH);
      else
        digitalWrite(BLed, LOW);
    }
}

String sendHTML(int songNo){
  String song_name = "";
  if (songNo < 1 || songNo > song_count) {
    song_name = "None";
  }
  else {
    song_name = song_names[songNo - 1];
  }
  
  
  String ptr = R"rawliteral(<!DOCTYPE html> 
<html>
    <head>
        <meta 
            name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"
            http-equiv="Content-Type" content="text/html; charset=utf-8">

        <title>Music Box</title>
        <style type="text/css">

    html { 
        font-family: Helvetica; 
        display: inline-block; 
        margin: 0px auto; 
        text-align: center;
    }

      main {
    position: fixed;
    top: 50px; /* Set this to the height of the header */
    bottom: 50px; /* Set this to the height of the footer */
    left: 200px; 
    right: 200px;
    overflow: auto; 
    background: #fff;
    }

      body {
    margin: 0;
    padding: 0;
    overflow: hidden;
    height: 100%; 
    max-height: 100%; 
    font-family:Sans-serif;
    line-height: 1.5em;
    }

      #header {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 50px; 
    overflow: hidden; /* Disables scrollbars on the header frame. To enable scrollbars, change "hidden" to "scroll" */
    background: #BCCE98;
    }

      #footer {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 50px; 
    overflow: hidden; /* Disables scrollbars on the footer frame. To enable scrollbars, change "hidden" to "scroll" */
    background: #BCCE98;
    }

      #left {
    position: absolute; 
    top: 50px; /* Set this to the height of the header */
    bottom: 50px; /* Set this to the height of the footer */
    left: 0; 
    width: 400px;
    overflow: auto; /* Scrollbars will appear on this frame only when there's enough content to require scrolling. To disable scrollbars, change to "hidden", or use "scroll" to enable permanent scrollbars */
    background: #DAE9BC;    
    }

    #right {
      position: absolute; 
      top: 50px; /* Set this to the height of the header */
      bottom: 50px; /* Set this to the height of the footer */
      right: 0; 
      width: 200px;
      overflow: auto; /* Scrollbars will appear on this frame only when there's enough content to require scrolling. To disable scrollbars, change to "hidden", or use "scroll" to enable permanent scrollbars */
      background: #F7FDEB;    
    }
        
    .innertube {
      margin: 15px; /* Provides padding for the content */
    }
    
    p {
      color: #555;
    }

    nav ul {
      margin: 0;
      padding: 0;
      color: darkgreen;
      text-decoration: none;
    }
        
    /*IE6 fix*/
    * html body{
      padding: 50px 200px 50px 200px; /* Set the first value to the height of the header, the second value to the width of the right column, third value to the height of the footer, and last value to the width of the left column */
    }
    
    * html main{ 
      height: 100%; 
      width: 100%; 
    }

        </style>
    </head>

    <!-- <body>
        <div id="webpage">
            <h1>Music Box</h1>
            <h2>You can also connect via Bluetooth to ESP32-Music_Box</h2>
            <button class="button" name="play_pause" value="ON" type="submit">Play / Pause</button>
            <button class="button" name="next_song" value="ON" type="submit">Next</button>
            <button class="button" name="play_music" value="ON" type="submit">Previous</button>

        </div>
    </body> -->

    <body>    

    <header id="header">
      <div class="innertube">
                <p>Music Box</p>
      </div>
    </header>
        
    <main>
      <div class="innertube">
        
        <h1>Last played song:</h1>
        <h2>)rawliteral";
    //-------------------------------------------------
    // ADD SONG NAME
    ptr += (String)song_name;
    //-------------------------------------------------
    ptr += R"rawliteral(
    
        </h2>
        
      </div>
    </main>

    <nav id="left">
      <div class="innertube">
        <h1>Songs</h1>
        <ol>
          <li>Cypis - Gdzie jest bialy wegorz</li>
          <li>Jeremy Soule - Dragonborn</li>
          <li>Jingle Bells</li>
          <li>Nikolai Korsakov - Flight of the Bumblebee</li>
          <li>Billy Joel - Piano Man</li>
          <li>Linkin Park - Numb</li>
          <li>Ludwig van Beethoven - Fur Elise</li>
        </ol>

      </div>
    </nav>  
    
    
    <footer id="footer">
      <div class="innertube">
        <p>You can play music by connecting via Bluetooth to ESP32-Music_Box</p>
      </div>
    </footer> 
      
  </body>

</html>)rawliteral";

  
  return ptr;
}
