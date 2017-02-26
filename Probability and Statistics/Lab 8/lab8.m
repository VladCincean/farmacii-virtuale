X = [20*ones(1,2), 21, 22*ones(1,3), 23*ones(1,6), 24*ones(1,5), 25*ones(1,9), 26*ones(1,2), 27*ones(1,2)];
Y = [75*ones(1,3), 76*ones(1,2), 77*ones(1,2), 78*ones(1,5), 79*ones(1,8), 80*ones(1,8), 81, 82];

% a) the means
mX = mean(X);
fprintf('Mean of X = %3.4f\n', mX)
mY = mean(Y);
fprintf('Mean of Y = %3.4f\n', mY)

% b) the variances
vX = var(X, 1); % population variance, i.e. imparte la N
vY = var(Y, 1); % --//--
fprintf('Variance of X = %3.4f\n', vX)
fprintf('Variance of Y = %3.4f\n', vY)

% c) covariance cov(X, Y)
covXY = cov(X, Y, 1); % e o matrice
fprintf('cov(X, Y) = %3.4f\n', covXY(1, 2))

% d) correlation coefficient
my_corr_coeff = corrcoef(X, Y); % e o matrice
fprintf('the correlation coefficient = %3.4f\n', my_corr_coeff(1, 2))

% e)
clf
scatter(X, Y) % like plot(X, Y, ...)
hold on
x_regr = 20:27; % X, dar fara repetitii
y_regr = mY + my_corr_coeff(1, 2) * (sqrt(vY) / sqrt(vX)) * (x_regr - mX);
plot(x_regr, y_regr, 'r')