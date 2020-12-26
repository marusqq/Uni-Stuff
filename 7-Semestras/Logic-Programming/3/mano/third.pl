/* studento nr 1711369
 * Marius Pozniakovas
 * 4 kursas, 1 grupė
 * uzduotys: 1.13; 2.1; 3.2; 4.5
 * https://swish.swi-prolog.org/p/3-prolog.pl
*/

/* 1.13
    sulieti(S1,S2,R) - duoti išrūšiuoti didėjimo tvarka sąrašai S1 ir S2. 
    Sąrašas R gaunamas suliejus šiuos du sąrašus taip, kad jo elementai 
    eitų didėjimo tvarka. Pavyzdžiui:
    ?- sulieti([1,4,11],[2,5,7],R).
    R = [1,2,4,5,7,11].
*/

sulieti([],[],[]).
sulieti([X],[],[X]):-!.
sulieti([],[Y],[Y]).
sulieti([X|List1],[Y|List2],[X|List]) :- X < Y, !, 
    sulieti(List1,[Y|List2],List).
sulieti([X|List1],[Y|List2],[Y|List]) :- 
    sulieti([X|List1],List2,List).

/* 2.1
	nr(S,K,E) - E yra K-asis sąrašo S elementas. Pavyzdžiui:
	?- nr([a,b,c,d,e],3,E).
	E = c.
*/

nr([H|_],1,H) :-
    !.
nr([_|T],N,H) :-
    N > 0, %loop prevention
    N1 is N-1,
    nr(T,N1,H).
	
/* 3.2
	bendri(S1,S2,R) - sąrašas R susideda iš bendrų duotųjų sąrašų S1 ir S2 elementų. 
	Pavyzdžiui:
	?- bendri([a,b,c,d],[d,b,e],R).
	R = [b,d].
*/


bendri([], _, []).
bendri([H1|T1], L2, [H1|Res]) :-
    member(H1, L2),
    bendri(T1, L2, Res),!.
bendri([_|T1], L2, Res) :-
    bendri(T1, L2, Res).

/* 4.5 
    des_skaitm(Skaic,Sar) - Sar - duotojo skaičiaus Skaic dešimtainių skaitmenų sąrašas. 
    Pavyzdžiui:
    ?- des_skaitm(1456,Sar).
    Sar = [1,4,5,6]. 
*/

splitRev(0,[]).
splitRev(N,[A|As]) :- !, N1 is floor(N/10), A is N mod 10, splitRev(N1,As).

des_skaitm(Skaic, Sar) :-
    splitRev(Skaic, ReversedSar),
    reverse(Sar, ReversedSar), !.
    






















