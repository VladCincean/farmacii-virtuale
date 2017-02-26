p = input('p = '); % p in [0.05, 0.95]
for n = 1:3:100
    xpdf = 0:n;
    ypdf = binopdf(xpdf, n, p);
    plot(xpdf, ypdf, 'rs--');
    pause(0.5);
end