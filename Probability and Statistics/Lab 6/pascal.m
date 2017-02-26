% Generate Nbin(n, p) distr.
clear all

n = input('Rank of success = ');
p = input('Probability of success = ');

for j = 1:n % generate n Geo(p) variables
    Y(j) = 0;
    while (rand >= p)
        Y(j) = Y(j) + 1;
    end
end

X = sum(Y); % Nbin(n, p) - suma a n variabile geometrice

clear X
clear Y

N = input('Nr. of simulations (sample size) = ');
for i = 1:N
    for j = 1:n % generate n Geo(p) variables
        Y(j) = 0;
        while (rand >= p)
            Y(j) = Y(j) + 1;
        end
    end
    X(i) = sum(Y);
end

UX = unique(X); % distinct values
freq = hist(X, length(UX));
rel_freq = freq ./ N;

% Compare graphically with Nbin(n, p) distr.
clf % clear figure
xpdf = 0:30;
ypdf = nbinpdf(xpdf, n, p);
plot(xpdf, ypdf, 'm*', UX, rel_freq, 'go', 'MarkerSize', 10)
legend('neg. bin. pdf', 'simulation', 0)
        