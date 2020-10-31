function Gradientinio_nus

%duota funkcija
f = @(x1, x2) (1 / 8) * ((x1 .^ 2) .* x2 + x1 .* (x2 .^ 2) - x1 .* x2);

%gradientine funkcija
gradient = @(X) [2 * X(1) * X(2) + X(2) .^ 2 - X(2), X(1) ^ 2 + 2 * X(1) * X(2) - X(1)];

%pradiniai taskai
X_0 = [0, 0];
X_1 = [1, 1];
X_my = [9/10, 5/ 10];


%braizymas
%[x1, x2] = meshgrid(0:0.01:1, 0:0.01:1);
%y = f(x1, x2);
%surf(x1, x2, y);
%title(['Funkcijos grafikas']);

%pasirenku gamma
gamma = 0.33; 

epsilon = 10 ^ (- 4);

k = 1;
kmax = 100; 

format long;

%pasirenkame kad praeitu nors karta per cikla
dist = Inf;

X0 = X_my;
while dist >= epsilon
 
    grad = gradient(X0);
    X0 = X0 - gamma .* grad;
    dist = norm(grad);
 
    fprintf('X0= %f %f f(x0)= %f k= %d\n', X0, f(X0(1), X0(2)), k);
 
   % subplot(1, 2, 2);
    title(['Artiniai']);
    plot(X0(1), X0(2), 'blao');
    hold on;
 
    if k == kmax
        format short;
        disp(['Pasiektas maksimalus iteraciju skaicius k=', num2str(kmax)]);
        break
    end
    k = k + 1;
 
end
grid on;
hold off;