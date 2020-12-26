/* studento nr 1711369
 * Marius Pozniakovas
 * 4 kursas, 1 grupė
 * uzduotys: 1.13; 2.1; 3.2; 4.5
*/

/* 1.13 
    sulieti(S1,S2,R) - duoti išrūšiuoti didėjimo tvarka sąrašai S1 ir S2. Sąrašas 
    R gaunamas suliejus šiuos du sąrašus taip, kad jo elementai eitų didėjimo tvarka. 
    Pavyzdžiui:
    ?- sulieti([1,4,11],[2,5,7],R).
    R = [1,2,4,5,7,11].
*/

sulieti([],L,L).
sulieti(L,[],L).
sulieti([Head1|Tail1], [Head2|Tail2], L) :- 
    Head1 < Head2 -> L = [Head1|R], sulieti(Tail1,[Head2|Tail2],R) ;
    Head1 > Head2 -> L = [Head2|R], sulieti([Head1|Tail1],Tail2,R) ;
    L = [Head1,Head2|R], sulieti(Tail1,Tail2,R).

/* 2.1 
    nr(S,K,E) - E yra K-asis sąrašo S elementas. Pavyzdžiui:
    ?- nr([a,b,c,d,e],3,E).
    E = c.

*/




/* 3.2
    bendri(S1,S2,R) - sąrašas R susideda iš bendrų duotųjų sąrašų S1 ir S2 elementų. 
    Pavyzdžiui:
    ?- bendri([a,b,c,d],[d,b,e],R).
    R = [b,d].

*/

/* 4.5 
    des_skaitm(Skaic,Sar) - Sar - duotojo skaičiaus Skaic dešimtainių skaitmenų sąrašas. 
    Pavyzdžiui:
    ?- des_skaitm(1456,Sar).
    Sar = [1,4,5,6].
*/


# splitRev(0,0).
# splitRev(N,[A|As]) :- N1 is floor(N/10), A is N mod 10, splitRev(N1,As).

number_chars(123456,X),format('~s',[X]).
