%------------------------------------------------
%------PATTERN RECOGNITION------
%--------MINIPROJECT 2----------
%--------Std:HAmze ghaedi-------
%--------Stdn:9831419-----------
%------------------------------------------------

clear
%-----------Load data----------------------------
x_train = load('mnist\Train_Data.csv');
y_train = load('mnist\Train_labels.csv');
x_test = load('mnist\Test_Data.csv');
y_test = load('mnist\Test_labels.csv');
%------------------------------------------------


%----------------Specs---------------------------
sz = size(x_train);
n_training_samples = sz(1);
[n_test_samples,te] = size(y_test);
n_features = sz(2);
n_classes = 10;
%------------------------------------------------

%---------------Model Definition-----------------

%assuming Gaussian distribution for each class 
%We need to estimate mean(which is a vector) 
%and covaraince matrix for each of the 10 classes
%so we have 20 parameters
%and 10 priori probabilities corresponding to each class

priories = zeros(n_classes,1);
means = zeros(n_features,n_classes);
covariances = zeros(n_features,n_features,n_classes);

%--------------------------------------------------


%---------------Estimate Model Parameters--------------

%our parameter estimator is based on Maximum likelihood

[priories,means,covariances] = params_estimator(x_train,y_train,n_classes);

%------------------------------------------------------

%-----------------Define Discriminator-----------

W = zeros(n_features,n_features,n_classes);
w = zeros(n_features,n_classes);
w_0 = zeros(n_classes,1);

%Calculate Discriminator parameters--------------
covariances = max_ent_cov_estimator(covariances);
[W,w,w_0] = disc_params_calculator(priories,means,covariances);
%-------------------------------------------------

%--------------Testing----------------------------

predicted = zeros(2500,1);

for i=1:n_test_samples
    g = discriminator(W,w,w_0,x_test(i,:));
    predicted(i) = classifier(g) - 1;
end

%--------------------------evaluation-----------------
acc = length(find((predicted == y_test))) / n_test_samples;
acc_mat = zeros(10,10);
for i =1:n_test_samples
   acc_mat(y_test(i)+1,predicted(i)+1) =  acc_mat(y_test(i)+1,predicted(i)+1) + 1;
end
%------------------------------------------------------



