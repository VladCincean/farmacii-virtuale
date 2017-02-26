% 2. sigma UNKNOWN
conflevel = input('conf. level = '); % 1 - alpha
alpha = 1 - conflevel;

X = [99.8 * ones(1,2), 99.9 * ones(1,5), 98.0 * ones(1,3), ...
    100.1 * ones(1,4), 100.5 * ones(1,2), 100.0 * ones(1, 2), ...
    100.2 * ones(1, 2)];

s = std(X);
mX = mean(X);

n = length(X);
t1 = tinv(1 - alpha / 2, n - 1);
t2 = tinv(alpha / 2, n - 1);

ci1 = mX - s / sqrt(n) * t1;
ci2 = mX - s / sqrt(n) * t2;

fprintf('C.I. for the mean (sigma unknown) is (%3.4f, %3.4f)\n', ci1, ci2)

% pr2
% conf. level = 0.95
% C.I. for the mean (sigma unknown) is (99.3817, 100.1083)
% pr2
% conf. level = 0.99
% C.I. for the mean (sigma unknown) is (99.2484, 100.2416)
% pr2
% conf. level = 0.999
% C.I. for the mean (sigma unknown) is (99.0709, 100.4191)