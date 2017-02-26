% sigma1 = sigma2

conflevel = input('conf. level = '); % 1 - alpha
alpha = 1 - conflevel;

% Premium
X1 = [22.4 21.7 ...
      24.5 23.4 ...
      21.6 23.3 ...
      22.4 21.6 ...
      24.8 20.0];
% Regular
X2 = [17.7 14.8 ...
      19.6 19.6 ...
      12.1 14.8 ...
      15.4 12.6 ...
      14.0 12.2];
    
n1 = length(X1);
n2 = length(X2);

mX1 = mean(X1);
mX2 = mean(X2);

v1 = var(X1); % sigma_1 squared
v2 = var(X2); % sigma_2 squared

sp2 = ((n1 - 1) * v1 + (n2 - 1) * v2) / (n1 + n2 - 2);

t1 = tinv(1 - alpha / 2, n1 + n2 - 2);
t2 = tinv(    alpha / 2, n1 + n2 - 2);

ci1  = mX1 - mX2 - t1 * sqrt(sp2) * sqrt(1 / n1 + 1 / n2);
ci2  = mX1 - mX2 + t1 * sqrt(sp2) * sqrt(1 / n1 + 1 / n2);

fprintf('C.I. for the difference of pop. means (sigma1 = sigma2): ')
fprintf('(%3.4f, %3.4f)\n', ci1, ci2)
