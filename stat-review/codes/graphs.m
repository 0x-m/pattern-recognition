
%----------------------------------------
%--------------GENERALS------------------
%----------------------------------------
x = (-30:0.1:30);
p_x_w1 =  (1/pi) * 1./(1+(x-3).^2); %likelihood of x while state of nature is w1
p_x_w2 =  (1/pi) * 1./(1+(x-5).^2); %likelihood of x while state of nature is w2

p_w1 = 1/2; %priori probability of class w1
p_w2 = 1/2; %priori probability of class w2

p_x = p_w1 .* p_x_w1 + p_w2 .* p_x_w2; %evidence

p_w1_x = (p_x_w1 .* p_w1) ./ p_x ; %posteriori probability of class w1
p_w2_x = (p_x_w2 .* p_w2) ./ p_x; %posteriori probability of class w2
%----------------------------------------

%----------------------------------------
%--------------#1.b----------------------
%----------------------------------------
figure()
xlim([-30,30]);
ylim([0,1]);
plot(x,p_w1_x,'r');

hold on 
plot(x,p_w2_x,'b');
legend('p(w_1|x)','p(w_2|x)')

%----------------------------------------
%--------------#1.e----------------------
%----------------------------------------
figure()
xlim([-30,30]);
ylim([0,1]);
plot(x,p_w1_x,'r');
hold on 
plot(x,p_w2_x,'b');
th = (3 + 5)/2;
plot([th,th],[0,1],'g--');
legend('p(w_1|x)','p(w_2|x)','Decision boundary')
%-----------------------------------------

%----------------------------------------
%--------------#1.f----------------------
%----------------------------------------

figure()
xlim([-30,30]);
ylim([0,1]);
plot(x,p_w1_x,'r');
hold on 
plot(x,p_w2_x,'b');
th1 = 4.35;
th2 = 9.65;
plot([th1,th1],[0,1],'g--');
plot([th2,th2],[0,1],'g--');
legend('p(w_1|x)','p(w_2|x)','Decision boundary')
%------------------------------------------------------------------

