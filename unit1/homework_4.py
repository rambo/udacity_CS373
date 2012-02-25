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

p = []

# Assume (know) all rows have same length
rows = len(colors)
cols = len(colors[0])
n_cells =  rows * cols
p_per_cell = 1.0 / n_cells
p = rows * [cols * [p_per_cell]]



# This will reference P by columns instead of rows
p_rotated = []
for col in range(cols):
    pass
    





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

def move_exact_2d(p, U):
    # Special case
    if (U == [0,0]):
        return p 
    
    
    return p

# Inexact moving
def move_2d(p, U):
    # Special case
    if (U == [0,0]):
        return p
    pM = array_mul_2d(move_exact_2d(p, U), p_move)
    pNM = array_mul_2d(move_exact_2d(p, [0,0]), 1.0-p_move)
    return array_add_2d(pM, pNM)
    
    
    


# my odl list-slicing move
#def move(p, U):
#    U = U % len(p) * -1
#    return p[U:] + p[:U]


# old inexact motion examples
#def move_exact(p, U):
#    q = []
#    for i in range(len(p)):
#        q.append(p[(i-U)%len(p)])
#    return q
#
#def sum_lists(p1, p2):
#    q = []
#    for i in range(len(p1)):
#        q.append(p1[i] + p2[i])
#    return q
#
#
#def move(p, U):
#    pE = [x * pExact for x in move_exact(p, U)]
#    pO = [x * pOvershoot for x in move_exact(p, U+1)]
#    pU = [x * pUndershoot for x in move_exact(p, U-1)]
#    q = sum_lists(sum_lists(pE, pU), pO)
#    return q



#Your probability array must be printed 
#with the following code.

show(p)




