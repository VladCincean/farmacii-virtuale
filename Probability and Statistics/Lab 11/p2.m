% population mean, mu; sigma known
% H0: mu = 99.4 ( <
% H1: mu > 99.4 (right-tailed)

alpha = input('sign. level = ');
fprintf('H0: mu = 99.4\nH1: mu > 99.4\n');
mu0 = 99.4;
% sigma UNKNOWN
X = [99.8 * ones(1,2), 99.9 * ones(1,5), 98.0 * ones(1,3), ...
    100.1 * ones(1,4), 100.5 * ones(1,2), 100.0 * ones(1, 2), ...
    100.2 * ones(1, 2)];

[h, p, ci, stats] = ttest(X, mu0, alpha, 'right');

if h == 0
    fprintf('Do not reject H0, i.e. the center will accept these energy bars\n');
else
    fprintf('Reject H0, i.e. he center will NOT accept these energy bars\n');
end

fprintf('Observed value of the TS: %3.4f\n', stats.tstat);
fprintf('The P-value: %3.4f\n', p);

q2 = tinv(1 - alpha, stats.df); % tinv(1 - alpha, n - 1);

fprintf('Rejection region, RR: (%3.4f, inf)\n', q2);