N = input('sample size = ');
a = input('a = ');
b = input('b = ');
x = unifrnd(a, b, 1, N); % SAMPLE
n = 1 + 10 ./ 3 .* log10(N); % nr of classes
lim = min(x) : (max(x) - min(x)) / n : max(x);
id = 1 : n;
leftlim = lim(id);
rightlim = lim(id + 1);
[fr, mark] = hist(x, n);
relfr = fr / N;

res = [id; leftlim; rightlim; fr; mark; relfr];

fprintf(' Nr\t|\t\tClass\t\t\t\t| Freq\t| Mark\t\t| Rel.freq\t|\n')
fprintf('----|---------------------------|-------|-----------|-----------|\n')
fprintf('%3d |\t[%3.4f, %3.4f]\t\t| %3d\t| %3.4f\t| %3.4f\t|\n', res)
fprintf('----|---------------------------|-------|-----------|-----------|\n')

clf
hist(x, n)
hold on
plot(mark, fr, 'r.-', 'lineWidth', 3)

fprintf('Mean = %3.4f\n', mean(x))
fprintf('Mode:\n')

idm = find(fr == max(fr)); % the classes with highest frequencies
resm = [idm; leftlim(idm); rightlim(idm); fr(idm); mark(idm); relfr(idm)];
fprintf('%3d |\t[%3.4f, %3.4f]\t\t| %3d\t| %3.4f\t| %3.4f\t|\n', resm)
fprintf('----|---------------------------|-------|-----------|-----------|\n')

Q = prctile(x, [25, 50, 75]);
fprintf('Quartiles: Q1 = %3.4f, Q2 = % 3.4f, Q3 = %3.4f.\n', Q)