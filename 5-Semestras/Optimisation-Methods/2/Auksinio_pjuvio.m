function res=Auksinio_pjuvio(f, X0, gradientas)

f1=@(x) f(X0-x*gradientas);


l=0;  
r=0.5; 

epsilon=10^(-4);

k=1; 
kmax=100;

fi = (sqrt(5) - 1) / 2;

L = r-l; % intervalo ilgis
x1 = r-fi*L;
y1 = f1(x1);
x2 = l + fi*L;
y2 = f1(x2);
format short;

while L>= epsilon
  
      if y2 < y1
          l = x1;
          L = r - l;
          x1 = x2;
          y1=y2;
          x2 = l + fi*L;
          y2 = f1(x2);
      else
          r = x2;
          L = r - l;
          x2 = x1;
          y2=y1;
          x1 = r - fi*L;
          y1 = f1(x1);
      end 
          
      if k==kmax
          format short
          disp(['Pasiektas maksimalus iteraciju skaicius k=', num2str(kmax)]);
          break
      end   
      
      k=k+1;
      L=r-l;

end
res=[x1, k+2];
end