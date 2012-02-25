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
n_cells = len(colors) * len(colors[0])
p_per_cell = 1.0 / n_cells
print "%d cells, %f p of each cell" % (n_cells, p_per_cell)
# initialize uniform distribution
for i in range(len(colors)):
    subp = []
    for i in range(len(colors[0])):
        subp.append(p_per_cell)
    p.append(subp)

# Helper to calculate the sum of 2d array
def array_sum_2d(p):
    tsum = 0 
    for i in range(len(p)):
        tsum = tsum + sum(p[i])
    return tsum


    
print array_sum_2d(p)





#Your probability array must be printed 
#with the following code.

show(p)




