a = input('a = ');
b = input('b (>a) = ');
n = input('n = ');

ind = 1:n;            	% length n

line = a:(b-a)/n:b;     % length n + 1
leftlim = line(1:n);    % length n      line(ind)
rightlim = line(2:n+1); % length n      line(int + 1)
midp = (leftlim + rightlim)./2; % --//--
results = [ind;leftlim;rightlim;midp];

fprintf(' Nr\t|\t\tSubint.\t\t| Midp\n')
fprintf('----|-------------------|--------\n')
fprintf('%3d\t| [%3.4f, %3.4f]\t| %3.4f\n', results)