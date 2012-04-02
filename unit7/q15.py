# not correct
#print [0.14285714285714285, 0.14285714285714285, 0.5714285714285714, 0.14285714285714285]
# also not correct
#print [0.14285714285714285*3, 0.14285714285714285*3, 0.5714285714285714*3, 0.14285714285714285*3]

# From the robot class
def Gaussian(self, mu, sigma, x):
    # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
    return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))

# Not this either
#q = [0.2,0.2,2.4,0.2]
#qsum = sum(q)
#for i in range(len(q)):
#    q[i] = q[i] / qsum 
#    
#print q

