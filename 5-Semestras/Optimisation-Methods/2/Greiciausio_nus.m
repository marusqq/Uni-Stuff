function Greiciausio_nus

%duota funkcija
f=@(X) (1 / 8) * (X(1)^2.*X(2)+X(1)*X(2)^2-X(1)*X(2));

%gradientine funkcija
gradient = @(X) [2 * X(1) * X(2) + X(2) .^ 2 - X(2), X(1) ^ 2 + 2 * X(1) * X(2) - X(1)];

% pradiniai taskai
X_0 = [0, 0];
X_1 = [1, 1];
X_my = [9/10, 5/10];
X0 = X_my;

epsilon = 10 ^ (- 4);

i=0; 
k=1;
kmax=100; 


format short;

%priskiriame kad praeitu nors karta cikla
dist = Inf;

while dist>=epsilon
      grad=gradient(X0);
      res=Auksinio_pjuvio(f,X0,grad);
      gamma=res(1);
   %   fprintf("%f", gamma);
      i=i+res(2)+1;
      X0 = X0 - gamma .* grad; % naujas artinys
      dist = norm(grad);

      
      fprintf('X0= %f %f f(X0)= %f k= %d i= %d\n', X0, f(X0), k, i);
    
      
   
      title(['Artiniai']);
      plot(X0(1), X0(2), 'blao');
      hold on;
      if k==kmax
          disp(['Pasiektas maksimalus iteraciju skaicius k=', num2str(kmax)]);
          break
      end
      k=k+1;
end
end