
world = ['no_burn', 'burn']
p = [0.999, 0.001]

pHit = 0.9
pMiss = 0.1


def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    print q
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


print sense(p, 'burn')
