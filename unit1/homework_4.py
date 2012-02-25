colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT


# REMINDER: move first, sense then.


p = []

# Assume (know) all rows have same length
rows = len(colors)
cols = len(colors[0])
n_cells = rows * cols
p_per_cell = 1.0 / n_cells
# initialize uniform distribution (The list comprehensions caused funky issues due to pointers being created instead of objects)
for row in range(rows):
    subp = []
    for col in range(cols):
        subp.append(p_per_cell)
    p.append(subp)

# Helper to pivot an array (as in switch columns to rows and vice versa)
def pivot_array(p):
    p_rotated = []
    for col in range(len(p[0])):
        subp = []
        for row in range(len(p)):
            subp.append(p[row][col])
        p_rotated.append(subp)
    return p_rotated
#print "pre privot"
#show(p)
#print "after pivot"
#show(pivot_array(p))

# Helper to calculate the sum of 2d array
def array_sum_2d(p):
    tsum = 0 
    for row in range(len(p)):
        tsum = tsum + sum(p[row])
    return tsum
#print array_sum_2d(p)

# Helper to normalize the array
def normalize(p):
    s = array_sum_2d(p)
    # TODO: switch to map ?
    for row in range(len(p)):
        # "in-place" (not actually, there will be temp lists created in memory) divide each item of the row by s
        p[row][:] = [x / s for x in p[row]]
    return p
#show(normalize(p))

# Helper to do the multiplications on array
def array_mul_2d(p, mul_by):
    # TODO: switch to map ?
    for row in range(len(p)):
        # "in-place" (not actually, there will be temp lists created in memory) multiply each item of the row by given value
        p[row][:] = [x * mul_by for x in p[row]]
    return p

# helper to add two arrays to each other
def array_add_2d(p1, p2):
    q = []
    # TODO: switch to map ?
    for row in range(len(p1)):
        subq = []
        for col in range(len(p1[row])):
            subq.append(p1[row][col] + p2[row][col])
        q.append(subq)
    return q;
#show(array_add_2d(p,p))

# IMO the list-comprehensions are cleaner than the "official" example (and since we cannot import anything we can't use any optimized types like deque:s)
def move_exact_1d(p, U):
    U = U % len(p) * -1
    return p[U:] + p[:U]

# Exact moving in 2D array
def move_exact_2d(p, U):
    # Special case
    if (U == [0,0]):
        return p 
    if (U[0] != 0):
        p_pivot = pivot_array(p)
        for i in range(len(p_pivot)):
            p_pivot[i] = move_exact_1d(p_pivot[i], U[0])
        p = pivot_array(p_pivot)
    if (U[1] != 0):
        for i in range(len(p)):
            p[i] = move_exact_1d(p[i], U[1])
    return p
# Set a value we can track when moving
#p[1][1] = 1.0
#print "p before move"
#show(p)
#print "p after (exact) move"
#show(move_exact_2d(p, [0, 1]))

# Inexact moving
def move_2d(p, U):
    # Special case
    if (U == [0,0]):
        return p
    pM = array_mul_2d(move_exact_2d(p, U), p_move)
    pNM = array_mul_2d(move_exact_2d(p, [0,0]), 1.0-p_move)
    return array_add_2d(pM, pNM)
# Set a value we can track when moving
#p[1][1] = 1.0
#print "p before move"
#show(p)
#print "p after move"
#show(move_2d(p, [0, 1]))

# official sense example (in 1D)
#def sense(p, Z):
#    q=[]
#    for i in range(len(p)):
#        hit = (Z == world[i])
#        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
#    s = sum(q)
#    for i in range(len(q)):
#        q[i] = q[i] / s
#    return q

def sense_2d(p, Z):
    print "NOT IMPLEMENTED: sense"
    return p


# Test full (exact) motions
#p[0][1] = 1.0
#print "p before moves"
#show(p)
#for i in range(len(motions)):
#    p = move_exact_2d(p, motions[i])
#print "p after (exact) moves"
#show(p)

for i in range(len(motions)):
    p = move_2d(p, motions[i])
    p = sense_2d(p, measurements[i])

#Your probability array must be printed 
#with the following code.

print "The final show, do not forget this"
show(p)




