
world = ['fair', 'not_fair']
p = [0.5, 0.5]

pHit = 0.5
pMiss = 0.1


def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


print sense(p, 'fair')
