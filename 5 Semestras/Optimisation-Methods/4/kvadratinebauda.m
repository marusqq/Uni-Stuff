function kvadratinebauda
  
  %my function
  f=@(X) -X(1).*X(2).*X(3);
  
  g=@(X) 2*X(1).*X(2)+2*X(1).*X(3)+2*X(2).*X(3)-1;
  h1=@(X) X(1);
  h2=@(X) X(2);
  h3=@(X) X(3);
 
  %penalty function
  b=@(X) (min(0,h1(X))).^2+(min(0,h2(X))).^2+(min(0,h3(X))).^2+(g(X)).^2;
  
  %penalty function
  B=@(X,r) f(X)+(1/r)*b(X);
  
  epsilon = 10^(-4);
  
  kmax=100;
  k=1;
  i=1;
  
  %X0 = [0,0,0];
  %X0 = [1,1,1];
  X0 = [0.3,0.6,0.9];
  
  r=1;
  
  %number of coords
  n=3;
  
  %we will lower this distance later
  check=Inf;
  format short
  
  disp(['r                         X                    B(X,r)     k       (function called #), volume']);
  disp('-----------------------------------------------------------------------------------------------'); 
  
  while check>=epsilon
    
    ats=Simplex(B,X0,r);
    %get back B, X0, r from simplex
    
    X1=ats(1:n);
    %new points
    
    i=i+ats(n+1);
    %calculate function call times
    
    check=norm(X0-X1);
	  %check distance between x0 and x1
	
    fprintf('%f      %f %f %f     %f       %d          %d    %f\n', r, X1(1), X1(2), X1(3), B(X1,r), k,i,abs(f(X1)));
    
    if k==kmax
     format short
     disp(['Iteration reached max k=',num2str(kmax)]);
     break
   end
   
   k=k+1;
   X0=X1;
   r=r/5;
   
end

end
