case 'closeness'
        
    [distSum, nrReachable] = closenessCentrality(g.Underlying, wc);
    
    nrReachable = nrReachable - 1; % do not count starting node
    c = (nrReachable/(numnodes(g) - 1)).^2 ./ distSum;
    c(nrReachable==0) = 0;
