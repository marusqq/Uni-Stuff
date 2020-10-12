/* studento nr 1711369
  * uzduotys: 19; 24; 30; 31:
  * 
  * uosvis(Uosvis, Zentas) - Pirmasis asmuo (Uosvis) yra antrojo (Zentas) uošvis (žmonos tėvas); 
  * pusbrolis(Pusbrolis, PusbrolisPussesere) - Pirmasis asmuo (Pusbrolis) yra antrojo (PusbrolisPussesere) pusbrolis;
  * nepilnametis(Nepilnametis) - Asmuo Nepilnametis yra jaunesnis, nei 18 metų;
  * vpjz(Vyras) - Asmuo Vyras yra „vyras pačiame jėgų žydėjime“: jo amžius yra iš tam tikro intervalo (nuspręskite patys, kokio);
 */

/* 1st gen */
asmuo(pranas, vyras, 64, zvejyba).
asmuo(joana, moteris, 69, krepsinis).
asmuo(dovakinas, vyras, 68, kalvyste).
asmuo(alina, moteris, 61, peiliai).
asmuo(pio, vyras, 81, laivyba).
asmuo(andzelika, moteris, 73, baletas).
asmuo(renatas, vyras, 60, beisbolas).
asmuo(aureja, moteris, 67, katinai).

/* 2nd gen */
asmuo(fiona, moteris, 43, filmai).
asmuo(gabrielius, vyras, 40, knygos).
asmuo(teresa, moteris, 39, sokiai).
asmuo(jonas, vyras, 37, begimas).
asmuo(katarina, moteris, 44, apsipirkinejimas).
asmuo(erikas, vyras, 45, medziokle).
asmuo(egle, moteris, 53, tinklinis).
asmuo(aurimas, vyras, 44, masinos).

/* 3rd gen */
asmuo(kristas, vyras, 18, xbox).
asmuo(pieva, moteris, 16, kosmetika).
asmuo(giedre, moteris, 19, perukai).
asmuo(domas, vyras, 8, lego).

/* 1st gen */
pora(pranas, joana).
pora(dovakinas, alina).
pora(pio, andzelika).
pora(renatas, aureja).

/* 2nd gen */
pora(gabrielius, fiona).
pora(jonas, teresa).
pora(erikas, katarina).
pora(aurimas, egle).

/* 2nd gen */
mama(joana, fiona).
mama(andzelika, jonas).
mama(andzelika, erikas).
mama(andzelika, egle).

/* 3rd gen */
mama(fiona, kristas).
mama(teresa, pieva).
mama(katarina, giedre).
mama(egle, domas).

/* taisykles */
/* 19: */
uosvis(Uosvis, Zentas) :- pora(Zentas, Jo_mergina), mama(Merginos_mama, Jo_mergina), pora(Uosvis, Merginos_mama).
/* testai: 
	uosvis(pranas, gabrielius)    -- true
    uosvis(gabrielius, pranas)    -- false
    uosvis(pio, aurimas)          -- true
    uosvis(pio, jonas)            -- false
*/

tevas_arba_mama(Suauges, Vaikas) :- mama(Suauges, Vaikas) ; (pora(Suauges, Mama), mama(Mama, Vaikas)).
brolis_arba_sese(Vaikas1, Vaikas2) :- mama(Mama, Vaikas1), mama(Mama, Vaikas2).

/* 24: */
pusbrolis(Pusbrolis, PusbrolisPussesere) :-
    asmuo(Pusbrolis, vyras, _, _),
    tevas_arba_mama(PirmasTevas, Pusbrolis), 
    tevas_arba_mama(AntrasTevas, PusbrolisPussesere),
    brolis_arba_sese(PirmasTevas, AntrasTevas).
/* testai: 
	pusbrolis(domas, pieva)       -- true
    pusbrolis(pieva, domas)		  -- false
    pusbrolis(giedre, pieva)      -- false
    pusbrolis(domas, giedre)      -- true
*/
    

/* 30: */
nepilnametis(Nepilnametis)  :- asmuo(Nepilnametis, _, Amzius, _), Amzius < 18.
/* testai: 
	nepilnametis(domas)           -- true
    nepilnametis(kristas)         -- false
    nepilnametis(giedre)          -- false
    nepilnametis(egle)			  -- false
*/

/* 31: */
vpjz(Vyras)  :- asmuo(Vyras, vyras, Amzius, _), Amzius < 40, Amzius >= 18.
/* testai: 
	vpjz(giedre)                  -- false
    vpjz(jonas)                   -- true
    vpjz(pranas)                  -- false
    vpjz(kristas)                 -- true
*/







