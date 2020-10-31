/* Magiskasis kvadratas*/

:- use_module(library(clpfd)).

magiskasis_kvadratas(N, Matrica) :-
	Nmax is N * N,
	Suma is N * (N * N + 1) / 2,
	patikrinti_matrica(N, N, Matrica),
	flatten(Matrica, Elementai),
	Elementai ins 1..Nmax,
	eilutes_suma(Matrica, Suma),
	transpose(Matrica, TransponuotaMat),
	eilutes_suma(TransponuotaMat, Suma),
	istrizai(Matrica, N, -1, D1),
	sum(D1, #=, Suma),
	istrizai(Matrica, 1, +1, D2),
	sum(D2, #=, Suma),
	all_different(Elementai), 
	label(Elementai).

patikrinti_matrica(0, _, []).
patikrinti_matrica(N0, N, [X|Matrica]) :-
	N0 > 0,
	N1 is N0 - 1,
	length(X, N),
	patikrinti_matrica(N1, N, Matrica).

eilutes_suma([], _).
eilutes_suma([Eilute|Matrica], Suma) :-
	sum(Eilute, #=, Suma),
	eilutes_suma(Matrica, Suma).

istrizai([], _, _, []).
istrizai([Eilute|Matrica], Idx, P, [X|ListoElem]) :-
	nth1(Idx, Eilute, X),
	Idx1 is Idx+P,
	istrizai(Matrica, Idx1, P, ListoElem).

/*
Eilutes = [A, B, C, D, E], 
magiskasis_kvadratas(5, Eilutes), 
maplist(label,Eilutes).
*/
/*Eilutes = [A, B, C], 
magiskasis_kvadratas(3, Eilutes), 
maplist(label,Eilutes).*/
