#Modify the empty list, p, so that it becomes a UNIFORM probability
#distribution over five grid cells, as expressed in a list of 
#five probabilities.

n=5
world_size = n
p = []
for i in range(0,world_size):
    p.append(1.0/world_size)
print p
sense = [0.2, 0.6, 0.6, 0.2, 0.2]
post = []
for i in range(len(sense)):
    post.append(p[i] * sense[i])
print post
