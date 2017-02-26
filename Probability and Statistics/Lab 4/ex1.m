x0 = 0;
x1 = -1;
x2 = 1;
alpha = 0.5;
betta = 0.5;

option = input('norm, t, chi2, f', 's: ');

switch option
    case 'norm'
        % Normal Distr.
        mu = input('mu = ');
        sigma = input('sigma (>0) = ');
        
        % a) P(X <= x0) = F(x0)
        Pa = normcdf(x0, mu, sigma);

        % b) P(X >= x0) = 1 - F(x0)
        Pb = 1 - Pa;

        % c) P(0x1 <= X <= x2) = 
        Pc = normcdf(x2, mu, sigma) - normcdf(x1, mu, sigma);

        % d) P(X <= x1 or X >= x2)
        Pd = 1 - Pc;

        % e)
        % x_alpha = ? s.t. P(X <= x_alpha) = alpha
        %                  F(x_alpha) = alpha
        %                  x_alpha = F^-1(alpha)
        x_alpha = norminv(alpha, mu, sigma);
        % quantile of order alpha

        % f) x_betta = ? s.t. P(X >= x_betta) = betta
        %                     1 - F(x_betta) = betta
        %                         F(x_betta) = 1 - betta
        %                           x_betta = F^-1(1 - betta)
        x_betta = norminv(1 - betta, mu, sigma);
    case 't'
        n = input('n (>=0) = ');
        
        % a) P(X <= x0) = F(x0)
        Pa = tcdf(x0, n);

        % b) P(X >= x0) = 1 - F(x0)
        Pb = 1 - Pa;

        % c) P(0x1 <= X <= x2) = 
        Pc = tcdf(x2, n) - tcdf(x1, n);

        % d) P(X <= x1 or X >= x2)
        Pd = 1 - Pc;

        % e) x_alpha = ? s.t. P(X <= x_alpha) = alpha
        x_alpha = tinv(alpha, n);

        % f) x_betta = ? s.t. P(X >= x_betta) = betta
        x_betta = tinv(1 - betta, n);
    case 'chi2'
        n = input('n (>0) = ');
        
        % a) P(X <= x0) = F(x0)
        Pa = chi2cdf(x0, n);

        % b) P(X >= x0) = 1 - F(x0)
        Pb = 1 - Pa;

        % c) P(0x1 <= X <= x2) = 
        Pc = chi2cdf(x2, n) - chi2cdf(x1, n);

        % d) P(X <= x1 or X >= x2)
        Pd = 1 - Pc;

        % e) x_alpha = ? s.t. P(X <= x_alpha) = alpha
        x_alpha = chi2inv(alpha, n);

        % f) x_betta = ? s.t. P(X >= x_betta) = betta
        x_betta = chi2inv(1 - betta, n);
    case 'f'
        m = input('m (>0) = ');
        n = input('n (>0) = ');
        
        % a) P(X <= x0) = F(x0)
        Pa = fcdf(x0, m, n);

        % b) P(X >= x0) = 1 - F(x0)
        Pb = 1 - Pa;

        % c) P(0x1 <= X <= x2) = 
        Pc = fcdf(x2, m, n) - fcdf(x1, m, n);

        % d) P(X <= x1 or X >= x2)
        Pd = 1 - Pc;

        % e) x_alpha = ? s.t. P(X <= x_alpha) = alpha
        x_alpha = finv(alpha, m, n);

        % f) x_betta = ? s.t. P(X >= x_betta) = betta
        x_betta = finv(1 - betta, m, n);
    otherwise
        fprintf('Error! Available options: norm, t, chi2, f.');
end

% Tiparire:
fprintf('Answer in a: Pa = %3.5f\n', Pa);
fprintf('Answer in b: Pb = %3.5f\n', Pb);
fprintf('Answer in c: Pc = %3.5f\n', Pc);
fprintf('Answer in d: Pd = %3.5f\n', Pd);
fprintf('Answer in e: x_alpha = %3.5f\n', x_alpha);
fprintf('Answer in f: x_betta = %3.5f\n', x_betta);
