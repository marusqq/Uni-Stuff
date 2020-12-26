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
studentas(gedvardas, 1).
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
arJaunesnis(Stud1, Stud2):-
	yraVyresnis(Stud2, Stud1).

arJaunesnis(Stud1, Stud2):-
	yraVyresnis(Kazkoks, Stud1),
	arJaunesnis(Kazkoks, Stud2).

arJaunesnisUzToPacioKurso(Stud1, Stud2):- 
	arJaunesnis(Stud1, Stud2),

	studentas(Stud1, Stud1Kursas),
	studentas(Stud2, Stud2Kursas),
	Stud1Kursas = Stud2Kursas.

/*arJaunesnisUzToPacioKurso(gintautas, julius)*/
/*arJaunesnisUzToPacioKurso(paulina, gedvardas)*/


/* 3. Duoti du natūriniai skaičiai. Raskite jų bendrą didžiausią daliklį pagal Euklido algoritmą. */

bdd(A, B, Z) :- euklid(A, B, Z).

euklid(A, 0, A) :- !.
euklid(0, B, B) :- !.
euklid(A, 0, Z) :- Z is A.
euklid(A, B, Z) :- B > A, euklid(B, A, Z).
euklid(A, B, Z) :- X is A mod B, euklid(B, X, Z).

/*bdd(2,4,X)*/
/*bdd(24,9,X)*/



