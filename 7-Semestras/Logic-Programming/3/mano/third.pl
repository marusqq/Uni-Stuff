/* studento nr 1711369
 * Marius Pozniakovas
 * 4 kursas, 1 grupė
 * uzduotys: 1.13; 2.1; 3.2; 4.5
*/

/* 1.13
    sulieti(S1,S2,R) - duoti išrūšiuoti didėjimo tvarka sąrašai S1 ir S2. 
    Sąrašas R gaunamas suliejus šiuos du sąrašus taip, kad jo elementai 
    eitų didėjimo tvarka. Pavyzdžiui:
    ?- sulieti([1,4,11],[2,5,7],R).
    R = [1,2,4,5,7,11].
*/

sulieti([],R,R).
sulieti(R,[],R).
sulieti([H1|T1], [H2|T2], R) :- 
    H1 < H2 -> R = [H1|Other], sulieti(T1,[H2|T2],Other), !;
    H1 > H2 -> R = [H2|Other], sulieti([H1|T1],T2,Other), !;
    R = [H1,H2|Other], sulieti(T1,T2,Other), !.

/* 2.1
	nr(S,K,E) - E yra K-asis sąrašo S elementas. Pavyzdžiui:
	?- nr([a,b,c,d,e],3,E).
	E = c.
*/

nr([H|_],1,H) :-
    !.
nr([_|T],N,H) :-
    N > 0, N1 is N-1, nr(T,N1,H).
	
/* 3.2
	bendri(S1,S2,R) - sąrašas R susideda iš bendrų duotųjų sąrašų S1 ir S2 elementų. 
	Pavyzdžiui:
	?- bendri([a,b,c,d],[d,b,e],R).
	R = [b,d].
*/

is_member(X,[X|_]).
is_member(X,[_|T]) :- is_member(X,T).


bendri([], _, []).
bendri(_, [], []).
bendri([H1|T1], L2, [H1|Res]) :-
    is_member(H1, L2), bendri(T1, L2, Res), !.
bendri([_|T1], L2, Res) :-
    bendri(T1, L2, Res).

/* 4.5 
    des_skaitm(Skaic,Sar) - Sar - duotojo skaičiaus Skaic dešimtainių skaitmenų sąrašas. 
    Pavyzdžiui:
    ?- des_skaitm(1456,Sar).
    Sar = [1,4,5,6]. 
*/

des_skaitm(Skaic, Sar) :-
    skaic(Skaic, ReversedSar),
    reverse_cus(Sar, [], ReversedSar), !.

reverse_cus(A, [], A). 
reverse_cus([H|T],A,R):- reverse_cus(T,[H|A],R).

skaic(0,[]).
skaic(N,[A|As]) :- !, N1 is floor(N/10), A is N mod 10, skaic(N1,As).























