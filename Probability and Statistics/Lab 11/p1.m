% population mean, mu; sigma known
% H0: mu = 9 ( >
% H1: mu < 9 (left-tailed)

alpha = input('sign. level = ');
fprintf('H0: mu = 9\nH1: mu < 9\n');
mu0 = 9; % test value
sigma = 5; % sigma known
X = [7 7 4 5 9 9 ...
    4 12 8 1 8 7 ...
    3 13 2 1 17 7 ...
    12 5 6 2 1 13 ...
    14 10 2 4 9 11 ...
    3 5 12 6 10 7]; % sample data (datele de selectie)

% TS = Z in N(0, 1) -> ztest

[h, p, ci, zval] = ztest(X, mu0, sigma, alpha, 'left');

% h = 0 -> reject H0
%     1 -> do not reject H0
% p - P-value
% zval: obs. val. of the TS, Z0

if h == 0
    fprintf('Do not reject H0, i.e. the computer system meets the efficiency standard.\n');
else
    fprintf('Reject H0, i.e. the computer system does NOT meet the efficiency standard.\n');
end

fprintf('Observed value of the TS: %3.4f\n', zval);
fprintf('The P-value: %3.4f\n', p);

q1 = norminv(alpha, 0, 1);

fprintf('Rejection region, RR: (-inf, %3.4f)\n', q1);

