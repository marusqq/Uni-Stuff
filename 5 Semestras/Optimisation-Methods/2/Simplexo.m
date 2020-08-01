function Simplexo

f = @(X) (1 / 8) * ((X(1) .^ 2) .* X(2) + X(1) .* (X(2) .^ 2) - X(1) .* X(2));

X_0 = [0, 0];
X_1 = [1, 1];
X_m = [9 / 10, 5 / 10];

X0 = X_m;

alpha = 1/2; 
teta = 1; 

gamma = 1.6; 
beta = 0.5;
eta = - 0.5;

epsilon = 10 ^ (- 4); 

n = 2; 
delta1 = alpha * (sqrt(n + 1) + n - 1) / (n * sqrt(2));
delta2 = alpha * (sqrt(n + 1) - 1) / (n * sqrt(2));

X1 = [X0(1, 1) + delta2, X0(1, 2) + delta1];
X2 = [X0(1, 1) + delta1, X0(1, 2) + delta2];

y0 = f(X0);
y1 = f(X1);
y2 = f(X2);

X = [X0; X1; X2];

y = [y0, y1, y2];

deltax = [X0(1), X0(1), X1(1); X1(1), X2(1), X2(1)];
deltay = [X0(2), X0(2), X1(2); X1(2), X2(2), X2(2)];
plot(deltax, deltay, 'b');
grid on;
hold on;
plot(X(:, 1), X(:, 2), 'mo');
hold on;

k = 1; 
i = 3; 
kmax = 100;
imax = 100;

format short;

disp(['   x1   x2    f(x1,x2)    k    (f kv. sk.)']);

pasiekta = false;
%pradedame vykdyti iteracijas
while ~ pasiekta
    [~, nr] = sort(y);
 
    %didziausias y
    yhigh = y(nr(3));
    Xhigh = X(nr(3), :);
 
    %maziausias y
    ylow = y(nr(1));
    Xlow = X(nr(1), :);
    
    %vidurinis y
    yg = y(nr(2));
    Xg = X(nr(2), :);
 
    Xc = (Xg + Xlow) / 2;
 
    X_naujas = Xhigh + (1 + teta) * (Xc - Xhigh);
    y_naujas= f(X_naujas);
    i = i + 1;
 
    if X_naujas(1) <= 0 || X_naujas(2) <= 0
        teta = - 1 / 2;
        X_naujas = Xhigh + (1 + teta) * (Xc - Xhigh);
        y_naujas = f(X_naujas);
        i = i + 1;
    end
 
    if (ylow < y_naujas) && (y_naujas < yg)
        teta = 1;
    elseif y_naujas < ylow
        teta = gamma;
        Z = Xhigh + (1 + teta) * (Xc - Xhigh);
        yz = f(Z);
        i = i + 1;
        if yz < y_naujas
            y_naujas = yz;
            X_naujas = Z;
        end
    elseif y_naujas > yhigh
        teta = eta;
        Z = Xhigh + (1 + teta) * (Xc - Xhigh);
        X_naujas = Z;
        y_naujas = f(Z);
        i = i + 1;
    elseif (yg < y_naujas) && (y_naujas < yhigh)
        teta = beta;
        Z = Xhigh + (1 + teta) * (Xc - Xhigh);
        X_naujas = Z;
        y_naujas = f(Z);
        i = i + 1;
    end
 
    if X_naujas(1) <= 0 || X_naujas(2) <= 0
        teta = - 1 / 2;
        X_naujas = Xhigh + (1 + teta) * (Xc - Xhigh);
        y_naujas = f(X_naujas);
        i = i + 1;
    end
 
     fprintf('%f    %f   %f %d   %d', X_naujas, y_naujas, k, i);
 
    count = 0;
 
    if max([norm(Xlow - Xg), norm(Xlow - Xhigh), norm(Xg - Xhigh)]) < epsilon
        count = count + 1;
    end
 
    if max([abs(ylow - yg), abs(ylow - yhigh), abs(yg - yhigh)]) < epsilon
        if ~count
          disp(' ')
        end  
        count = count + 1;
    end
 
    if i >= imax
        count = count + 1;
        disp(['Pasiektas maksimalus funkciju kvietimu skaicius i=', num2str(imax)]);
        if count == 3
            pasiekta = true;
        end
    end
 
    if k == kmax
        format short;
        disp(['Pasiektas maksimalus iteraciju skaicius k=', num2str(kmax)]);
        break
    end
 
    k = k + 1;
    X = [Xlow; Xg; X_naujas];

    y = [ylow, yg, y_naujas];

 
    deltax = [Xlow(1), Xlow(1), Xg(1); Xg(1), X_naujas(1), X_naujas(1)];
    deltay = [Xlow(2), Xlow(2), Xg(2); Xg(2), X_naujas(2), X_naujas(2)];
    plot(deltax, deltay, 'b');
    hold on;
    plot(X(:, 1), X(:, 2), 'mo');
    hold on;

    if ~ count
        disp(' ');
    end
end
end