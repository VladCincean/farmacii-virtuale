% For a population variance, sigma^2, for a normal underlying population
conflevel = input('conf. level = '); % 1 - alpha
alpha = 1 - conflevel;

X = [1.48 1.26 1.52 1.56 1.48 1.46 ...
     1.30 1.28 1.43 1.43 1.55 1.57 ...
     1.51 1.53 1.68 1.37 1.47 1.61 ...
     1.49 1.43 1.64 1.51 1.60 1.65 ...
     1.60 1.64 1.51 1.51 1.53 1.74];

s_squared = var(X);

n = length(X);

c1 = chi2inv(1 - alpha / 2, n - 1);
c2 = chi2inv(alpha / 2, n - 1);

ci1 = (n - 1) * s_squared / c1;
ci2 = (n - 1) * s_squared / c2;

fprintf('C.I. for the population variance is (%3.4f, %3.4f)\n', ci1, ci2)
fprintf('C.I. for the std. dev. is (%3.4f, %3.4f)\n', sqrt(ci1), sqrt(ci2))

% pr3
% conf. level = 0.95
% C.I. for the population variance is (0.0082, 0.0233)
% C.I. for the std.dev. is (0.0905, 0.1528)
% pr3
% conf. level = 0.99
% C.I. for the population variance is (0.0072, 0.0285)
% C.I. for the std.dev. is (0.0846, 0.1690)
% pr3
% conf. level = 0.999
% C.I. for the population variance is (0.0062, 0.0366)
% C.I. for the std.dev. is (0.0785, 0.1914)