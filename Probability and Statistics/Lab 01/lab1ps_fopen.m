% fopen
% -----
% fid = fopen('read.m', 'a+')
% fprintf(fid, '..., ...);
% fclose(fid)

fid = fopen('lab1ps_fprintf.m', 'a+');
fprintf(fid, '%...');
fclose(fid);

% cleaning:
% ---------
% clear
% clear all
% clf clear figure
% clc clear command Window