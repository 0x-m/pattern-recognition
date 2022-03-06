


function [priories,means,covariances] = params_estimator(x_train,y_train,n_classes)
    
    %---------Specs----------------
    sz = size(x_train);
    n_features = sz(2); %input dimension (or number of input features)
    n_samples = sz(1); %number of samples
    %------------------------------
    
    
    %-----------Declaration--------
    frequencies = zeros(n_classes,1); %frequency of occurrence for each class
    means = zeros(n_classes,n_features); 
    covariances = zeros(62,62,10);
    priories = zeros(n_classes,1); 
    %------------------------------
    
    
    %-------Calculate Priories and means--------------------------
    
    %MATLAB arrays indexed from 1 (Not 0). In order to map class labels 
    %to arrays indices, one added to each sample's label!
    %thus, frequencies(1) is the number of samples of class 0 and so on
    
    for i=1:n_samples    
        
        c = y_train(i,1) + 1; %corresponding class(label) of i'th sample + 1
        frequencies(c) = frequencies(c) + 1;
        means(c,:) = means(c,:) + x_train(i,:); 
        
    end
    
    priories =  frequencies ./ n_samples;
    means = means ./ frequencies;
    %----------------------------------------------------------------
    
    %-------------------Calculate covariance matricies---------------
    
    for i=1:n_samples
        c = y_train(i,1)+1;
        covariances(:,:,c) = covariances(:,:,c) +...
            (x_train(i,:)-means(c))'*(x_train(i,:) - means(c));
    end

    for i =1:10
        covariances(:,:,i) = covariances(:,:,i) ./ (frequencies(i) - 1);
    end
    %-----------------------------------------------------------------

end