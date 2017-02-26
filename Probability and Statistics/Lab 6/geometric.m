% Generate Geo(p) distr
clear all

p = input('Probability of success = ');
% X is nr. of failures before 1st success
X = 0; % initial value
while (rand >= p) % while failure
    X = X + 1;
end % stop at first success

clear X

% Generate N
N = input('Nr. of simulations (sample size) = ');
for i = 1:N
    X(i) = 0;
    while (rand >= p) % while failure
    	X(i) = X(i) + 1;
    end % stop at first success
end

UX = unique(X); % distinct values
freq = hist(X, length(UX));
rel_freq = freq ./ N;

% Compare graphically with Geo(p) distr.
clf % clear figure
xpdf = 0:20;
ypdf = geopdf(xpdf, p);
plot(xpdf, ypdf, 'm*', UX, rel_freq, 'go', 'MarkerSize', 10)
legend('geometric pdf', 'simulation', 0)
