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

v1 = var(X1); % sigma_1 squared
v2 = var(X2); % sigma_2 squared

f1 = finv(1 - alpha / 2, n1 - 1, n2 - 1);
f2 = finv(    alpha / 2, n1 - 1, n2 - 1);

ci1 = 1 / f1 * v1 / v2;
ci2 = 1 / f2 * v1 / v2;

fprintf('C.I. for the ratio of pop. variances: ')
fprintf('(%3.4f, %3.4f)\n', ci1, ci2)

fprintf('C.I. for the ratio of std. deviations: ')
fprintf('(%3.4f, %3.4f)\n', sqrt(ci1), sqrt(ci2))