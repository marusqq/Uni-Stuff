/* studento nr 1711369
 * Marius Pozniakovas
 * 4 kursas, 1 grupė
 * uzduotys: 2.2, 3  
*/

/* 2.2 
    Duomenų bazėje saugomi duomenys apie studentus faktais: 
    studentas(Vardas, Kursas); yraVyresnis(StudentoVardas1, StudentoVardas2). 
    Sąryšis „būti vyresniu“ yra tranzityvus, 
    todėl į faktų aibę neįtraukiami tie faktai, 
    kurie seka iš tranzityvumo sąryšio. 
    Apibrėžkite predikatą:
    
    „studentas A yra jaunesnis už to paties kurso studentą B“.*/

studentas(sarune, 4).
studentas(gedvardas, 4).
studentas(gintautas, 3).
studentas(julius, 3).
studentas(martyna, 2).
studentas(alius, 2).
studentas(deimante, 1).
studentas(paulina, 1).

/* sarune */
yraVyresnis(gedvardas, gintautas).
yraVyresnis(gedvardas, julius).
yraVyresnis(gedvardas, sarune).

/* sarune */
yraVyresnis(sarune, gintautas).
yraVyresnis(sarune, julius).

/* julius */
yraVyresnis(julius, martyna).
yraVyresnis(julius, alius).
yraVyresnis(julius, gintautas).

/* gintautas */
yraVyresnis(gintautas, martyna).
yraVyresnis(gintautas, alius).


/* martyna */
yraVyresnis(martyna, deimante).
yraVyresnis(martyna, paulina).

/* alius */
yraVyresnis(alius, deimante).
yraVyresnis(alius, paulina).

/* paulina */
yraVyresnis(paulina, deimante).


/*predikatas*/
jaunesnisStudentas(Jaunesnis, Vyresnis) :- arJaunesnis(Jaunesnis, Vyresnis), studentas(Jaunesnis, JaunesnioKursas), studentas(Vyresnis, VyresnioKursas), JaunesnioKursas = VyresnioKursas.

arJaunesnis(Jaunesnis, Vyresnis) :- yraVyresnis(Vyresnis, Jaunesnis).
arJaunesnis(Jaunesnis, Vyresnis) :- yraVyresnis(Vyresnis, Kazkuris),jaunesnisStudentas(Jaunesnis, Kazkuris).



/* 3. Duoti du natūriniai skaičiai. Raskite jų bendrą didžiausią daliklį pagal Euklido algoritmą. */

bdd(A, B, Z) :- euklid(A, B, Z).

euklid(A, 0, Z) :- Z is A.
euklid(A, B, Z) :- B > A, euklid(B, A, Z).
euklid(A, B, Z) :- X is A mod B, euklid(B, X, Z).