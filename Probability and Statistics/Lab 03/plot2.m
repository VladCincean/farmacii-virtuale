% Binomial Distr
% n = input('nr of trials =');
% p = input('prob. of success =');
% 
% xpdf = 0:n;
% ypdf = binopdf(xpdf, n, p);
% subplot(2,1,1);
% plot(xpdf, ypdf, 'b+', 'MarkerSize', 12);
% title('pdf');
% 
% xcdf = 0:0.01:n;
% ycdf = binocdf(xcdf, n, p);
% subplot(2,1,2);
% plot(xcdf, ycdf, 'r*');
% title('cdf');


N = input('nr of simulations = ');
U = rand(3, N);
X = (U < 0.5);
Y = sum(X);
hist(Y); % histogram -> face cate un dreptunghi pentru fiecare valoare