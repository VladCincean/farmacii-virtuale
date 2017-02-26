fprintf('H0: sigma1 = sigma2\n')  % sigma1^2/sigma2^2 = 1
fprintf('H1: sigma1 != sigma2\n') % sigma1^2/sigma2^2 != 1

alpha = input('sign level = ');
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
 
[h, p, ci, stats] = vartest2(X1, X2, alpha, 'both'); % defaults: alpha = 0.05, tail = 'both'

if h == 0
    fprintf('H0 is NOT rejected, i.e. population variances are EQUAL.\n');
else
    fprintf('H0 is rejected, i.e. population variances are NOT equal.\n');
end

fprintf('Observed value of the Test Statistic: %3.5f\n', stats.fstat);
fprintf('P-value P = %3.5f\n', p);

q1 = finv(alpha / 2, stats.df1, stats.df2); % F(n1 - 1, n2 - 1)
q2 = finv(1 - alpha / 2, stats.df1, stats.df2);

fprintf('Rejection Region = (-inf, %3.5f) U (%3.5f, inf)\n', q1, q2);

% b)------------------------------------
fprintf('H0: mu1 = mu2\n') % H0: mu1 - mu2 = 0
fprintf('H1: mu1 > mu2\n') % H1: mu1 - mu2 > 0 (right-tailed test)

if h == 0
    [hB, pB, ciB, statsB] = ttest2(X1, X2, alpha, 'right', 'equal');
else
    [hB, pB, ciB, statsB] = ttest2(X1, X2, alpha, 'right', 'unequal');
end

if hB == 0
    fprintf('H0 is NOT rejected, i.e. gas mileage seem to be LOWER, on average, when premium gasoline is used.\n')
else
    fprintf('H0 is rejected, i.e. gas mileage seem to be HIGHER, on average, when premium gasoline is used.\n')
end

fprintf('Observed value of the test statistics: %3.5f\n', statsB.tstat)
fprintf('P-value P = %e\n', pB)

q1B = tinv(1 - alpha, statsB.df);

fprintf('Rejection Region = (%3.5f, inf)\n', q1B);