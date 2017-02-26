clf;

x = 0:0.01:3;
y1 = x.^2/10;
y2 = x.*sin(x);
y3 = cos(x);

% in acelasi sistem de axe de coordonate

% plot(x,y1,'go:',x,y2,'r*:',x,y3,'mv:')
% title('This is my graph')
% legend('y1', 'y2', 'y3', 'Location', 'Best')

subplot(3,1,1);
plot(x,y1,'r*:')
title('Graph 1')
legend('y1', 'Location', 'Best')
subplot(3,1,2);
plot(x,y2,'go:')
title('Graph 2')
legend('y2', 'Location', 'Best')
subplot(3,1,3);
plot(x,y3,'mv:');
title('This is my graph')
legend('y3', 'Location', 'Best')