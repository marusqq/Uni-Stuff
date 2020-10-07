/*
2.6. Duomenų bazėje saugomi duomenys apie studentus faktais: studentas(Vardas, Kursas); yraVyresnis(StudentoVardas1, StudentoVardas2). Sąryšis „būti vyresniu“ yra tranzityvus, todėl į faktų aibę neįtraukiami tie faktai, kurie seka iš tranzityvumo sąryšio. Apibrėžkite predikatą:
    jaunesnisStudentas(A, B) „studentas A yra jaunesnis už aukštesnio kurso studentą B“.
*/

studentas(rokas, 1).
studentas(jonas, 1).
studentas(martynas, 2).
studentas(alina, 2).
studentas(gabija, 3).
studentas(joana, 3).
studentas(sarunas, 4).
studentas(guoste, 4).
yraVyresnis(martynas, jonas).
yraVyresnis(martynas, rokas).
yraVyresnis(alina, jonas).
yraVyresnis(alina, rokas).
yraVyresnis(gabija, martynas).
yraVyresnis(gabija, alina).
yraVyresnis(joana, martynas).
yraVyresnis(joana, alina).
yraVyresnis(sarunas, gabija).
yraVyresnis(sarunas, joana).
yraVyresnis(guoste, gabija).
yraVyresnis(guoste, joana).

jaunesnisStudentas(Jaunesnis, Vyresnis) :- arJaunesnis(Jaunesnis, Vyresnis), studentas(Jaunesnis, JaunesnioKursas), studentas(Vyresnis, VyresnioKursas), JaunesnioKursas < VyresnioKursas.

arJaunesnis(Jaunesnis, Vyresnis) :- yraVyresnis(Vyresnis, Jaunesnis).
arJaunesnis(Jaunesnis, Vyresnis) :- yraVyresnis(Vyresnis, Kazkuris),jaunesnisStudentas(Jaunesnis, Kazkuris).



/*
6.1. Natūralieji skaičiai yra modeliuojami termais nul, s(nul), s(s(nul)),… (žr. paskaitos medžiagą). Apibrėžkite predikatus:
    „dviejų skaičių suma lygi trečiajam skaičiui.“
*/

suma(nul,A,A).
suma(s(A),B,s(C)):- suma(A,B,C).
