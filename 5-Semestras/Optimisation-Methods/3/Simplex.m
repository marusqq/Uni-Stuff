function ats=Simplex(B,X0,r)
f = @(X) B(X,r);
 
%choose parameters
  %initial simplex vertex
  alpha= 1/2;
 
  %initial value for looking for point
  teta = 1;
 
%parameters for simplex deformation
  %stretch
  gamma = 2; %gamma > 1
 
  %suspension of simplex
  beta = 0.5; % 0<beta<1
  eta = - 0.5;% -1<eta<0
 
 
  epsilon = 10 ^ (- 5); %accuracy
 
 
 
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%initial simplex creation, we will be using n=3 then
 
n = 3;
 
delta1 = alpha * (sqrt(n + 1) + n - 1) / (n * sqrt(2));
delta2 = alpha * (sqrt(n + 1) - 1) / (n * sqrt(2));
 
%other apexes calculation
X1 = [X0(1) + delta2, X0(2) + delta1, X0(3)+delta1];
X2 = [X0(1) + delta1, X0(2) + delta2, X0(3)+delta1];
X3 = [X0(1) + delta1, X0(2) + delta1, X0(3)+delta2];
 
%y meanings in apexes
y0 = f(X0);
y1 = f(X1);
y2 = f(X2);
y3 = f(X3);
 
%array of simplex
X = [X0; X1; X2; X3];
y = [y0, y1, y2, y3];
 
k = 1; %iterations
i = 3; %function calls
kmax = 100;
imax = 100;
 
 
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
done = false;
 
% Calculate Xh, Xg, Xl, yh, yg, yl
while ~ done
 
    [~, nr] = sort(y); %sort
 
 
    %yhigh > yi > yg > ylow
 
    yhigh = y(nr(4));
    Xhigh = X(nr(4), :);
 
    ylow = y(nr(1));
    Xlow = X(nr(1), :);
     
    yg = y(nr(2));
    Xg = X(nr(2), :);
   
    yi = y(nr(3));
    Xi = X(nr(3), :);
   
    % Viduriu tasko Xc ir naujo artinio Xnew apskaiciavimas
    Xc = (Xg + Xlow+Xi) / 3;
   
 
    X_naujas = Xhigh + (1 + teta) * (Xc - Xhigh);
    y_naujas= f(X_naujas);
    i = i + 1;
     
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Creation of a new simplex
    if (ylow < y_naujas) && (y_naujas < yg)
        teta = 1;
       
    elseif y_naujas < ylow %stretch
        teta = gamma;
        Z = Xhigh + (1 + teta) * (Xc - Xhigh);
        yz = f(Z);
        i = i + 1;
        if yz < y_naujas
            y_naujas = yz;
            X_naujas = Z;
        endif
       
    elseif y_naujas > yhigh %turn over
        teta = eta;
        Z = Xhigh + (1 + teta) * (Xc - Xhigh);
        X_naujas = Z;
        y_naujas = f(Z);
        i = i + 1;
       
    elseif (yg < y_naujas) && (y_naujas < yhigh) %suspend
        teta = beta;
        Z = Xhigh + (1 + teta) * (Xc - Xhigh);
        X_naujas = Z;
        y_naujas = f(Z);
        i = i + 1;
    endif
   
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    check = 3;
   
    %check if the points are good for confirming the next simplex
    if max([norm(Xlow - Xg), norm(Xlow - Xhigh), norm(Xg - Xhigh),norm(Xlow - Xi),norm(Xg - Xi),norm(Xi - Xhigh)]) < epsilon
        check = check - 1;
 
    endif
 
    if max([abs(ylow - yg), abs(ylow - yhigh), abs(yg - yhigh),abs(ylow - yi),abs(yg - yi),abs(yi - yhigh)]) < epsilon
        check = check - 1;
    endif
 
    if i >= imax
        check = check - 1;
 
        if check == 0
            done = true;
        endif
    endif
 
    k = k + 1;
    
    %confirm new points
    X = [Xlow; Xg; Xi; X_naujas];
 
    %also calculate y
    y = [ylow, yg, yi, y_naujas];
   
endwhile
 
ats=[X_naujas,i];