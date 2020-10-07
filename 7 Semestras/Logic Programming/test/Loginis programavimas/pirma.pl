asmuo(angele, moteris, 65, gaminimas).
asmuo(leonardas, vyras, 67, ukininkyste).
asmuo(romualdas, vyras, 67, sodininkyste).
asmuo(judita, moteris, 64, skaitymas).
asmuo(augustas, vyras, 8, informatika).
asmuo(laurita, moteris, 18, matematika).
asmuo(aurelija, moteris, 20, informatika).
asmuo(vaidas, vyras, 43, informatika).
asmuo(renata, moteris, 43, skaitymas).
asmuo(arunas, vyras, 30, zaidimai).
mama(eugenija, angele).
mama(angele, vaidas).
mama(angele, arunas).
mama(kazele, judita).
mama(judita, renata).
mama(terese, leonardas).
mama(valia, romualdas).
mama(renata, laurita).
mama(renata, aurelija).
mama(renata, augustas).
pora(antanas, eugenija).
pora(leonardinas, terese).
pora(leonardas, angele).
pora(kazys, kazele).
pora(jonas, valia).
pora(romualdas, judita).
pora(vaidas, renata).

/*2 vienas_is_tevu(TevasMama, Vaikas) - Pirmasis asmuo (TevasMama) yra antrojo (Vaikas) vienas iš tėvų (tėtis ar mama);*/
vienas_is_tevu(Mama, Vaikas):- mama(Mama, Vaikas).
vienas_is_tevu(Tevas, Vaikas):- pora(Tevas, Mama), mama(Mama, Vaikas).

/*6 broliai(Brolis1, Brolis2) - Asmenys Brolis1 ir Brolis2 yra broliai;*/
broliai(Brolis1, Brolis2) :- mama(Mama, Brolis1), mama(Mama, Brolis2), 
    asmuo(Brolis1, vyras, _, _), asmuo(Brolis2, vyras, _, _), not(Brolis1 = Brolis2).

/*34 paveldejo(Asmuo, Pomegis) - Asmuo Asmuo turi tokį patį pomėgį Pomegis kaip ir vienas iš tėvų; */
paveldejo(Asmuo, Pomegis) :- vienas_is_tevu(TetisMama, Asmuo), asmuo(TetisMama, _, _, Pomegis).

/*38 stos_i_informatika(Abiturientas) - Asmuo Abiturientas yra pakankamo (patys nuspręskite kokio) amžiaus ir domisi informatika; */
stos_i_informatika(Abiturientas) :- asmuo(Abiturientas, _, Amzius, informatika), Amzius >= 18.

/* GALIMI TIKSLAI:
*	(2)
*	vienas_is_tevu(eugenija, angele). (ats.: true)
*	vienas_is_tevu(MamaTetis, augustas). (ats.: renata; vaidas)
*	(6)
*	broliai(vaidas, arunas). (ats.: true)
*	broliai(laurita, augustas). (ats.: false)
*	(34)
*	paveldejo(aurelija, informatika). (ats.: true)
*	paveldejo(renata, Pomegis). (ats.: skaitymas; sodininkyste)
*	(38)
*	stos_i_informatika(augustas).	(ats.: false)
*	stos_i_informatika(Abiturientas). (ats.: aurelija; vaidas)
*/