function tiesinissimplex

%gauso/lenteliu metodu
%-x1 + x2 - x3 - x4  <=8
%-x1 + x2 - x3 - x4 + s1 =8

%visi skaiciai teigiami

%2x1 - 3x2 - 0x3 - 5x4 + 0s1 + 0s2 + 0s3
%c yra kas virsuj, duota funkcija
C = [2,-3,0,-5,0,0,0];

A = [-1, 1, -1, -1,	  1,0,0;
	    2, 4, 0,  0,	  0,1,0;
	    0, 0, 1,  1,	  0,0,1];

B=[3;6;9];

%dydis A matricos 
[eilSk,stulpSk] = size(A);

minC = 0;

%stulpeliai kurie yra vienetiniai
beta = [5,6,7];

%maziausia reiskme is virsaus ir jos indeksas
[m,nr] = min(C);


%1 ar yra neigiamu reiskmiu virsuj (jei neranda, tada nepadaro nieko)
%2 iesko pacios maziausios neigiamos reiksmes
%3 vykdo pertvarkymus kol sutvarko
%4 atsiras skaicius * -1.0 ir tada gaunam minimuma kampe

while m<0
  lamda = B./A(:,nr);
  %8 / -1, 10/0, 3/1

  for x=1:length(lamda)
  
    if lamda(x)<0
      lamda(x)=Inf;
    endif
  endfor

  %paima pacia maziausia reiksme
  [lamdaK,k]=min(lamda);
  %3,3 (3/1 ir 3index)
  

  beta(k)=nr;
  %beta[3] = 4 index
  
%tikslas padaryt kad liktu vienas 1 (arba dalina is saves eilute) ir kiti nuliai

  B(k) =B(k)./A(k,nr);
  %padalina stulpelio numeri 

  A(k,:)=A(k,:)./A(k,nr);
  % padalina eilute kur yra sitas
  fprintf('%g | %g | %g | %g | %g | %g | %g |%g\n',C(1:7), minC);
  for i=1:eilSk
   
   fprintf('%g | %g | %g | %g | %g | %g | %g |%g\n',A(i,:),B(i));
   
  endfor
fprintf('\n');
  
  minC = minC - B(k)*C(nr);
  %paskaiciuoja minimuma kampe

  C = C - A(k,:)*C(nr);
  %virsu irgi skaiciuoja
  

	
	fprintf('%g | %g | %g | %g | %g | %g | %g |%g\n',C(1:7), minC);

  %pertvarko eilutes kad butu nuliai
  for i=1:eilSk
   
   fprintf('%g | %g | %g | %g | %g | %g | %g |%g\n',A(i,:),B(i));
   
    A(i,:);
    if i~=k
      B(i) = B(i) - B(k)*A(i,nr);
      A(i,:) = A(i,:) - A(k,:)*A(i,nr);
    endif
  endfor
  fprintf('\n');
   %kad taptu 0 ^ algoritmas

%suranda min kampe , atsakymas 
[m,nr] = min(C);



endwhile

%pradine baze, atsakymas
X=[0,0,0,0,0,0,0];
%x1,x2, x3, x4, s1, s2, s3

%tai x1 = 0, nes nesigauna vienetine matrica
%x2 = 5/2 (5/2 * 1),
%kadangi mes jau turejom indeksa sita, todel neskaiciuojam
% 		sito stulpelio, x3 = 0
% x4 = 1 * 3

% s1 = 17/2
% s2 = 0
% s3, s2 nuliai, nes nera nulinio vektoriaus

%visada gausis trys nenuliai
%cia yra baze apskaiciuota
%optimalus sprendinys: be s1, s2, s3
% x = optimalus sprendinys


%kai virsuj nebera neigiamu, tai 
for y=1:length(beta)
  X(beta(y))=B(y);
endfor

%spausdina optimalu, pridet %g x 3, bazej atspausdint
%
fprintf('\nX = (%g %g %g %g)\nmin = %g \n', X(1:4), -minC);
fprintf('baze = %g %g %g\n', beta);


endfunction 
