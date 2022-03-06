

function [W,w,w_0] = disc_params_calculator(priories,means,covariances)

    n_classes = size(priories);

    inv_covariances = zeros(62,62,10);
   % mecs = max_ent_cov_estimator(covariances);
    
    %-------------Inverting covariance matrices-------
    for i=1:n_classes
        inv_covariances(:,:,i) = inv(covariances(:,:,i));
    end
    %-------------------------------------------------

    %----------------------------------------------------------------------
    %------------Computing Bayes Discriminator parameters------------------
    %----------------------------------------------------------------------
    W = (-0.5) .* inv_covariances;

    for i=1:n_classes
        w(:,i) = inv_covariances(:,:,i) * means(i,:)';
    end
    
    %-------Thresholds(or biases)----
    for i=1:n_classes
        w_0(i) = (-0.5)*means(i,:)*w(:,i)-(0.5)*log(det(inv_covariances(:,:,i)))+log(priories(i));
    end
    

end
