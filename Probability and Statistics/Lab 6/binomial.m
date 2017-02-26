% Generate Bino(n, p)
% -------------------
clear all

n = input('Nr. of trials = ');
p = input('Probability of success = ');

U = rand(n, 1);
X = sum(U < p);
clear X

% Gen. N var's
N = input('Nr. of simulations (sample size) = ');
for i = 1:N
    U = rand(n, 1);
    X(i) = sum(U < p);
end

UX = unique(X); % distinct values
freq = hist(X, length(UX));
rel_freq = freq ./ N;

% Compare graphically with Bino(n, p) distr.
clf % clear figure
xpdf = 0:n;
ypdf = binopdf(xpdf, n, p);
plot(xpdf, ypdf, 'm*', UX, rel_freq, 'go', 'MarkerSize', 10)
legend('bino pdf', 'simulation', 0)