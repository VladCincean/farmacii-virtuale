% b)
% H0: sigma  = 5 ... sigma^2  = 25
% H1: sigma != 5 ... sigma^2 != 25 (two-tailed)

alpha = input('sign. level = ');
fprintf('H0: sigma = 5\nH1: sigma != 5\n');
v0 = 25; % test value
X = [7 7 4 5 9 9 ...
    4 12 8 1 8 7 ...
    3 13 2 1 17 7 ...
    12 5 6 2 1 13 ...
    14 10 2 4 9 11 ...
    3 5 12 6 10 7]; % sample data (datele de selectie)

[h, p, ci, stats] = vartest(X, v0, alpha, 'both');

if h == 0
    fprintf('Do not reject H0, i.e. sigma = 5\n');
else
    fprintf('Reject H0, i.e. sigma != 5\n');
end

fprintf('Observed value of the TS: %3.4f\n', stats.chisqstat);
fprintf('The P-value: %3.4f\n', p);

q1 = chi2inv(alpha / 2, stats.df); % chi2inv(alpha / 2, n - 1);
q2 = chi2inv(1 - alpha / 2, stats.df);

fprintf('Rejection region, RR: (-inf, %3.4f) U (%3.4f, inf)\n', q1, q2);