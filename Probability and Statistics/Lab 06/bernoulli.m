% Generate Bern(p), p in (0,1)
% ----------------------------
p = input('p = ');
U = rand;
X = (U < p); % X=1 if U<p. succes

% Generate a sample of variables
N = input('Nr. of simulations (sample size) = ');
for i = 1:N
    U = rand;
    X(i) = (U < p);
end
% X

UX = unique(X) % distinct values
freq = hist(X, length(UX));
rel_freq = freq ./ N