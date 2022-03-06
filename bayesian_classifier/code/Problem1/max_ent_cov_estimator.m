%----------Maximum Entropy Covariance Estimator---------------
function [mecs] = max_ent_cov_estimator(covariances)
    
    sz = size(covariances);
    cov_p = zeros(sz(1));
    
    for i=1:sz(3)
       cov_p = cov_p + covariances(:,:,i); 
    end
    cov_p = cov_p ./ sz(3); %mixture covariance matrix (covariances pool)
    
    mecs = zeros(62,62,10);
    for i=1:10
       [evec,eval] = eig(covariances(:,:,i) + cov_p);
       d_i = evec' * covariances(:,:,i) * evec * eye(62,62);
       d_p = evec' * cov_p * evec * eye(62,62);
       mecs(:,:,i) = evec * max(d_i,d_p) * evec';
    end

end