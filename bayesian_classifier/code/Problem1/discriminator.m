function [g] = discriminator(W,w,w_0,x)

    g = zeros(10,1);
    for i=1:10
        g(i) = x * W(:,:,i) * x' + w(:,i)'*x' + w_0(i);
    end

end