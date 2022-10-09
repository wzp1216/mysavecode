%% test my file
disp('this is start...')
%% open xlsx
tx=xlsread('/home/wzp/Downloads/battery_low_current_test.xlsx');

time=tx(:,1);
vol=tx(:,3);
i=tx(:,4);
subplot(2,1,1)
plot(time,vol)
subplot(2,1,2)
plot(time,i)



