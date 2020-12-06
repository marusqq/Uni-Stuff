#include "pitches.h"

String song_names[] = {
  "Cypis - Gdzie jest bialy wegorz", 
  "Jeremy Soule - Dragonborn", 
  "Jingle Bells",
  "Nikolai Korsakov - Flight of the Bumblebee",
  "Billy Joel - Piano Man",
  "Linkin Park - Numb",
  "Ludwig van Beethoven - Fur Elise"
  };

int song_count = 7;

//Song1:
//Cypis - Gdzie jest bialy wegorz
int song1_melody[] = {
    _E4,
    _E4, _A4, _A4, _E4, _E4, _C4,
    _E4, _E4, _E4, _E4,
    _D4, _D4, _D4, _D4,
    _E4, _A4, _A4, _E4, _E4, _C4, _E4,
    _E4, _A4, _A4, _E4, _E4, _C4,
    _E4, _E4, _E4, _E4,
    _D4, _D4, _D4, _D4,
    _E4, _A4, _A4, _E4, _E4, _C4
};

int song1_tempo[] = {
    8,
    8, 8, 8, 8, 8, 3,
    4, 8, 4, 3,
    4, 8, 4, 3,
    8, 8, 8, 8, 8, 4, 8,
    8, 8, 8, 8, 8, 3,
    4, 8, 4, 3,
    4, 8, 4, 3,
    8, 8, 8, 8, 8, 4
};

//Song2:
//Jeremy Soule - Dragonborn
//F#: F->FS
//D#: D->DS
int song2_melody[] = {
  _B4,_B4,_B4,  _B4,_B4,_B4,
  _B4,_B4,_B4,  _B4,_B4,_C5,_DS5,
  _B4,_B4,_B4,  _B4,_B4,_B4,
  _B4,_B4,_B4,  _B4,_B4,_C5,_DS5,
  _B4,_B4,_B4,  _B4,_B4,_B4,
  _B4,_B4,_B4,  _B4,_B4,_C5,_DS5,
  _B4,_B4,_B4,  _B4,_B4,_B4,
  _B4,_B4,_B4,  _C5,_DS5,_B4,_C5,_DS5,

  _B3,
  _E4,
  _B4,
  _A4,
  _B4,
  _E5,
  _B5,

  _E5,_E5,  _DS5,_C5,
  _DS5,  _PAUSE,  _DS5,_C5,  _DS5,  _PAUSE, _C5, _DS5,
  _E5,_DS5,_C5,  _B4,  _PAUSE,  _B4,_A4,
  _B4,  _PAUSE,  _B4,_A4,  _B4,  _PAUSE,  _A4, _B4,
  _C5,_DS5,_A4,  _B4,  _DS5,_C5,
  _DS5,_DS5,_C5,  _DS5,  _C5,_DS5,
  _E5,_DS5,_C5,  _B4,  _B4,_A4,
  _B4,  _B4,_A4,  _B4, _A4,_B4,
  _C5,_DS5,_A4, _B4
};

int song2_tempo[] = {
  8,8,8,  8,8,8,
  8,8,8,  8,8,16,16,
  8,8,8,  8,8,8,
  8,8,8,  8,8,16,16,
  8,8,8,  8,8,8,
  8,8,8,  8,8,16,16,
  8,8,8,  8,8,8,
  8,8,8,  16,16,8,16,16,

  2,
  2,
  2,
  2,
  2,
  2,
  2,

  4,4,  16,16,
  8,  8,  16,16,  8,  8,  16,16,
  8,8,8,  8,  8, 16,16,
  8,  8,  16,16,  8,  8,  16,16,
  8,8,8,  4,  16,16,
  8,8,8,  4,  16,16,
  8,8,8,  4,  16,16,
  4,  16,16,  4,  16,16,
  8,8,8, 3
};

//Song3:
//Jingle Bells
int song3_melody[] = {
  _E5, _E5, _E5,
  _E5, _E5, _E5,
  _E5, _G5, _C5, _D5,
  _E5,
  _F5, _F5, _F5, _F5,
  _F5, _E5, _E5, _E5, _E5,
  _E5, _D5, _D5, _E5,
  _D5, _G5,
  _E5, _E5, _E5,
  _E5, _E5, _E5,
  _E5, _G5, _C5, _D5,
  _E5,
  _F5, _F5, _F5, _F5,
  _F5, _E5, _E5, _E5, _E5,
  _E5, _D5, _D5, _E5,
  _D5, _G5
};

int song3_tempo[] = {
  8, 8, 4,
  8, 8, 4,
  8, 8, 8, 8,
  2,
  8, 8, 8, 8,
  8, 8, 8, 16, 16,
  8, 8, 8, 8,
  4, 4,
  8, 8, 4,
  8, 8, 4,
  8, 8, 8, 8,
  2,
  8, 8, 8, 8,
  8, 8, 8, 16, 16,
  8, 8, 8, 8,
  4, 4
};

//Song4:
//Nikolai Korsakov - Flight of the Bumblebee
int song4_melody[] = {
  _E6, _DS6, _D6, _CS6, _D6, _CS6, _C6, _B5,
  _C6, _B5, _AS5, _A5, _GS5, _G5, _FS5, _F5,
  _E5, _DS5, _D5, _CS5, _D5, _CS5, _C5, _B4,
  _C5, _B4, _AS4, _A4, _GS4, _G4, _FS4, _F4,
  _E4, _PAUSE, _PAUSE, _PAUSE,
  _PAUSE
};

int song4_tempo[] = {
  16,16,16,16,16,16,16,16,
  16,16,16,16,16,16,16,16,
  16,16,16,16,16,16,16,16,
  16,16,16,16,16,16,16,16,
  16,16,8,4,
  2
};

//Song5:
//Billy Joel - Piano Man
int song5_melody[] = {
  _E4, _C4, _E4, _G4, _C5,
  _F4, _C4, _F4, _C5, _F4,
  _G4, _C4, _G4, _C5, _G4,
  
  _A4, _G4, _G4,
  _E4, _G4,
  _G4, _F4, _E4,
  _F4, _E4, _C4,

  _PAUSE, _PAUSE, _C4,
  _C4, _C4, _C4,
  _C4, _C4, _D4, _D4,
  _D4,

  _B4, _G4, _G4,
  _E4, _E4,
  _E4, _F4, _E4,
  _F4, _E4, _C4

};

int song5_tempo[] = {
  4, 8, 8, 8, 8,
  4, 8, 8, 8, 8,
  4, 8, 8, 8, 8,
  
  4, 4, 4,
  2, 1,
  4, 3, 8,
  8, 8, 2,
  
  4, 4, 4,
  4, 3, 8,
  4, 8, 8, 4,
  1,

  2, 8, 8,
  4, 2,
  2, 8, 8,
  8, 8, 2
};


//Song6:
//Linkin Park - Numb
//F# = F -> FS
//G# = G -> GS
//C# = C -> CS
int song6_melody[] = {
  _PAUSE, 
  _PAUSE, _CS5, _E5, _CS5,
  _FS5, _A5, _GS5,
  _PAUSE, _CS5, _E5, _CS5,
  _A5, _GS5, _E5, 
  _PAUSE, _CS5, _E5, _CS5,

  _FS5, _A5, _GS5,
  _PAUSE, _CS5, _E5, _CS5,
  _A5, _GS5, _E5,

  _PAUSE, _FS4, _CS5, _CS5, _CS5, _CS5, _E5, _CS5,
  _CS5, _CS5, _CS5, _B4, _A4,
  _CS5, _CS5, _B4, _A4, _B4, _E4,
  
  _CS5, _CS5, _B4, _A4, _B4,
  _PAUSE, _CS5, _CS5, _CS5, _CS5, _D5, _CS5,
  _CS5, _CS5, _B4, _A4  
};

int song6_tempo[] = {
  2, 
  8, 8, 8, 8,
  3, 3, 2,
  8, 8, 8, 8,
  3, 3, 2,
  8, 8, 8, 8,

  3, 3, 2,
  8, 8, 8, 8,
  3, 3, 1,

  8, 8, 8, 8, 8, 8, 8, 8,
  8, 8, 8, 3, 4,
  8, 8, 8, 4, 4, 8,

  8, 8, 8, 4, 3,
  4, 8, 8, 8, 8, 8, 8,
  8, 8, 8, 3
  
};

//Song7:
//Ludwig van Beethoven - Fur Elise
int song7_melody[] {
  _E5, _DS5,
  _E5, _DS5, _E5, _B4, _D5, _C5,
  _A4, _PAUSE, _C4, _E4, _A4,
  _B4, _PAUSE, _E4, _GS4, _B4,
  _C5, _PAUSE, _E4, _E5, _DS5,
  _E5, _DS5, _E5, _B4, _D5, _C5,
  _A5, _PAUSE, _C4, _E4, _A4,
  _B4, _PAUSE, _E4, _C5, _B4,
  _A4  
};

int song7_tempo[] {
  8,8,
  8,8,8,8,8,8,
  4, 8, 8, 8, 8,
  4, 8, 8, 8, 8,
  4, 8, 8, 8, 8,
  8,8,8,8,8,8,
  4, 8, 8, 8, 8,
  4, 8, 8, 8, 8,
  4
};
