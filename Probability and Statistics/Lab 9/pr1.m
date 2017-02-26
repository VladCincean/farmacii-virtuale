% PR1. sigma known
% confidence level
conflevel = input('conf. level = '); % 1 - alpha
alpha = 1 - conflevel;

X = [7 7 4 5 9 9 ...
    4 12 8 1 8 7 ...
    3 13 2 1 17 7 ...
    12 5 6 2 1 13 ...
    14 10 2 4 9 11 ...
    3 5 12 6 10 7]; % sample data (datele de selectie)
mX = mean(X);
sigma = 5; % sigma known
n = length(X); % lungimea VECTORULUI X
z1 = norminv(1 - alpha / 2, 0, 1);
z2 = - z1; % z2 = norminv(alpha / 2, 0, 1);

ci1 = mX - sigma / sqrt(n) * z1;
ci2 = mX - sigma / sqrt(n) * z2;

fprintf('C.I. for the mean (sigma known) is (%3.4f, %3.4f)\n', ci1, ci2)

% pr1
% conf. level = 0.95
% C.I. for the mean (sigma known) is (5.4778, 8.7444)
% pr1
% conf. level = 0.99
% C.I. for the mean (sigma known) is (4.9646, 9.2576)
% pr1
% conf. level = 0.999
% C.I. for the mean (sigma known) is (4.3690, 9.8532)
% pr1
% conf. level = 1
% C.I. for the mean (sigma known) is (-Inf, Inf)