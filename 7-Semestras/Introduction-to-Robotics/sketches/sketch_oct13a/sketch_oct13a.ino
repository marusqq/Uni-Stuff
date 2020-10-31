#include <LiquidCrystal.h>
// Create an LCD object. Parameters: (RS, E, D4, D5, D6, D7):
LiquidCrystal lcd(5, 6, 7, 8, 9, 10);


// SET PINS
const int first_button_pin = 2;
const int second_button_pin = 3;
const int third_button_pin = 4;

// variables for button
int current_first_button_state;
int current_second_button_state;
int current_third_button_state;

String card;

void setup() {
  
  //init console
  Serial.begin(9600);

  //lcd starting text
  lcd.begin(16, 2);

  //set pin modes
  pinMode(first_button_pin, INPUT_PULLUP);
  pinMode(second_button_pin, INPUT_PULLUP);
  pinMode(third_button_pin, INPUT_PULLUP);

  //print game name
  print_game_name();
}

void loop() {

  current_first_button_state = digitalRead(first_button_pin);
  if (current_first_button_state == 0) {
    //start the game 
    start_blackjack();
    print_game_name();
  }
  
  current_second_button_state = digitalRead(second_button_pin);
  if (current_second_button_state == 0)
    //Serial.println("Second button pressed");

  current_third_button_state = digitalRead(third_button_pin);
  if (current_third_button_state == 0)
    //Serial.println("Third button pressed");
  
  delay(1);
}

void print_game_name() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Blackjack Game");
  lcd.setCursor(0, 1);
  lcd.print("Button 1 to play");
}

void start_blackjack() {

   //set defaults
  String hand[2][6] = {};
  int player_card_index = 2;
  int player_card_value = 0;
  int dealer_card_index = 2;
  int dealer_card_value = 0;

  boolean bust = false;
  boolean blackjack = false;
  boolean hit_and_stand_player = false;
  boolean getting_input = false;

  

  //deal card to gamers
  lcd.clear();
  lcd.print("Game loading...");
  loading(1);
  
  //two cards for player
  hand[1][0] = get_card();
  hand[1][1] = get_card();
  player_card_index = 2;
  player_card_value = calculate_hand_value(hand[1], player_card_index);

  
  //Serial.println("Dealer Cards: " + hand[0][0] + hand[0][1]);
  //Serial.println("Value: " + String(calculate_hand_value(hand[0], dealer_card_index)));


  hit_and_stand_player = true;
  while (hit_and_stand_player) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(generate_hand_string(hand[1], player_card_index) + ":" + String(player_card_value));
    lcd.setCursor(0, 1);
    lcd.print("Hit  Stand  Exit");
    Serial.println("P: " + generate_hand_string(hand[1], player_card_index));
    Serial.println("V: " + String(player_card_value));
    //now ask if the player wants to hit or stand
    //Serial.println("press 1 to hit, press 2 to stand, press 3 to go back to main menu");

    getting_input = true;
    while (getting_input) {
      
      current_first_button_state = digitalRead(first_button_pin);    
      //start the game
      if (current_first_button_state == 0) {
        getting_input = false;

         //if BUST
        if (player_card_value > 21) {
          lcd.setCursor(0, 1);
          lcd.print("Bust! Dealer Win");
          bust = true;
          hit_and_stand_player = false;
        }
  
        //if PLAYER BLACKJACK
        else if (player_card_value == 21) {
          blackjack = true;
          hit_and_stand_player = false;
          lcd.setCursor(0, 1);
          lcd.print("Player BlackJack");
        }
        
        hand[1][player_card_index] = get_card();
        player_card_index += 1;
        player_card_value = calculate_hand_value(hand[1], player_card_index);

        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Hit me!");
        loading(1);

        lcd.clear();
        //display_hand(hand[1], player_card_index, 0);
        lcd.print(generate_hand_string(hand[1], player_card_index) + ":" + String(player_card_value));

        
        Serial.println("Player: Hit!" + hand[1][player_card_index]);

       
      }
  
      current_second_button_state = digitalRead(second_button_pin);
      if (current_second_button_state == 0) {
        getting_input = false;
        Serial.println("Player: Stand");
        hit_and_stand_player = false;

        //now get cards for dealer
        //player_card_value <- value to win versus for the dealer
        
        //two cards for dealer
        hand[0][0] = get_card();
        hand[0][1] = get_card();
        dealer_card_index = 2;
        dealer_card_value = calculate_hand_value(hand[0], dealer_card_index);
        
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(generate_hand_string(hand[1], player_card_index) + ":" + String(player_card_value));
        lcd.setCursor(0, 1);
        lcd.print(generate_hand_string(hand[0], dealer_card_index) + ":" + String(dealer_card_value));
        
        Serial.println("Dealer Cards: " + generate_hand_string(hand[0], dealer_card_index));
        
        

        //hit until 18, more than 18 or bust
        while(dealer_card_value < 18) {

          delay(2000);
          hand[0][dealer_card_index] = get_card();
          dealer_card_index += 1;
          dealer_card_value = calculate_hand_value(hand[0], dealer_card_index);
          loading(1);

          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print(generate_hand_string(hand[1], player_card_index) + ":" + String(player_card_value));
          lcd.setCursor(0, 1);
          lcd.print(generate_hand_string(hand[0], dealer_card_index) + ":" + String(dealer_card_value));
          
          Serial.println("Dealer: Hit! " + hand[0][dealer_card_index-1]);
        }

        if (dealer_card_value > 21) {
          delay(2000);
          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print("D:" + generate_hand_string(hand[0], dealer_card_index) + ":" + String(dealer_card_value));
          lcd.setCursor(0, 1);
          lcd.print("D: Bust, P: W");
          Serial.println("D: Bust, Player Wins! Cards: " + generate_hand_string(hand[0], dealer_card_index));
          Serial.println("------------------------------------------------------------");
          delay(3000);
        }

        else if (dealer_card_value == 21) {
          delay(2000);
          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print("D:" + generate_hand_string(hand[0], dealer_card_index) + ":" + String(dealer_card_value));
          lcd.setCursor(0, 1);
          lcd.print("Dealer BlackJack");
          Serial.println("Dealer: Blackjack! Cards: " + generate_hand_string(hand[0], dealer_card_index));
          Serial.println("------------------------------------------------------------");
          delay(3000);
        }

        else {
          
          delay(3000);
          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print("D:" + String(dealer_card_value) + ", P: " + String(player_card_value));
          lcd.setCursor(0, 1);
          
          if (dealer_card_value >= player_card_value) {
            lcd.print("Dealer Wins");
            delay(3000);
            return;
          }
          else {
            lcd.print("Player Wins");
            delay(3000);
            return;
          }
        }
        
        
      }
        
  
      current_third_button_state = digitalRead(third_button_pin);
      if (current_third_button_state == 0) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Returning.....");
        loading(1);
        Serial.println("Returning....");
        return;
        }
      
    }
    
  }

  if (bust == true) {
    Serial.println("Bust! Player loses with card value of " + String(player_card_value));
    Serial.println("------------------------------------------------------------");
    delay(1000);
    return;
  }

  else if(blackjack == true) {
    Serial.println("Player blackjack!!!!!!!!!");
    Serial.println("------------------------------------------------------------");
    delay(1000);
    return;
  }
  
}

String get_card() {

  //possible cards:
  //Hearts, Spades, Diamonds, Clubs
  //2,3,4,5,6,7,8,9,10,11,12,13,14
 
  String random_card_type;
  String string_card_number;
  int random_card_number;
  int random_card_type_num;
  
  random_card_number = random(2, 15);
  random_card_type_num = random(1, 5);

  if (random_card_number == 2)
    string_card_number = "2";
  else if (random_card_number == 3)
    string_card_number = "3";
  else if (random_card_number == 4)
    string_card_number = "4";
  else if (random_card_number == 5)
    string_card_number = "5";
  else if (random_card_number == 6)
    string_card_number = "6";
  else if (random_card_number == 7)
    string_card_number = "7";
  else if (random_card_number == 8)
    string_card_number = "8";
  else if (random_card_number == 9)
    string_card_number = "9";
  else if (random_card_number == 10)
    string_card_number = "0";
  else if (random_card_number == 11)
    string_card_number = "J";
  else if (random_card_number == 12)
    string_card_number = "Q";
  else if (random_card_number == 13)
    string_card_number = "K";
  else if (random_card_number == 14)
    string_card_number = "A";
  
  if (random_card_type_num == 1)
    random_card_type = "H";
  else if (random_card_type_num == 2)
    random_card_type = "S";
  else if (random_card_type_num == 3)
    random_card_type = "D";
  else if (random_card_type_num == 4)
    random_card_type = "C";

  String card = random_card_type + string_card_number;
  return card;
}

int calculate_hand_value(String hand[], int cards_in_hand) {
  
  int value = 0;
  
  for (int i = 0; i <= cards_in_hand; i++) {
    
    if (hand[i].indexOf("A") > 0)
      value += 11;
    else if (hand[i].indexOf("K") > 0 || hand[i].indexOf("Q") > 0 || hand[i].indexOf("J") > 0 || hand[i].indexOf("0") > 0)
      value += 10;
    else if (hand[i].indexOf("9") > 0)
      value += 9;
    else if (hand[i].indexOf("8") > 0)
      value += 8;
    else if (hand[i].indexOf("7") > 0)
      value += 7;
    else if (hand[i].indexOf("6") > 0)
      value += 6;
    else if (hand[i].indexOf("5") > 0)
      value += 5;
    else if (hand[i].indexOf("4") > 0)
      value += 4;
    else if (hand[i].indexOf("3") > 0)
      value += 3;
    else if (hand[i].indexOf("2") > 0)
      value += 2;
      
  }

  return value;
}


String generate_hand_string(String hand[], int cards_in_hand) {
  
  String generated_string = "";
  
  for (int i = 0; i <= cards_in_hand; i++) {
    generated_string = generated_string + hand[i] + " ";
  }
  
  return generated_string;
}


void loading(int line) {
    for (int i = 0; i <= 16; i++) {
    lcd.setCursor(i, line);
    lcd.write(255);
    delay(100);
  }
}
