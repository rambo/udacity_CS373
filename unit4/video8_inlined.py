# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid[0])-1,len(grid)-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # checked = [[0] * len(grid[0])] * len(grid) # arghs, this will create references...
    checked = []
    for i in range(len(grid)):
        checked.append([0] * len(grid[0]))

    expand_table = []
    for i in range(len(grid)):
        expand_table.append([-1] * len(grid[0]))
        
    expand_counter = 0

    def show_array(a):
        for i in range(len(a)):
            print a[i]

    x = init[0]
    y = init[1]
    g = 0 # cost
    
    to_check = [[g,x,y]] # Sebastian calls this open but that's a reserved word
    
    while(True):
        if len(to_check) == 0:
            print 'fail'
            return 'fail'
        
        to_check.sort()
        next_check = to_check.pop(0) # Sebastian calls this next but it too is a reserved word
        x = next_check[1]
        y = next_check[2]
        g = next_check[0]
        
        if (    x == goal[0]
            and y == goal[1]):
            print "solution"
            print next_check
            return next_check

        checked[y][x] = 1

        new_cost = g + cost
        for i in range(len(delta)):
            new_x = x + delta[i][0]
            new_y = y + delta[i][1]
            if (   new_x < 0 # Skip values outside of the grid
                or new_y < 0
                or new_y > len(grid)-1
                or new_x > len(grid[0])-1):
                #print "(%d,%d) is outside the grid" % (new_x, new_y)
                continue
            if (grid[new_y][new_x] == 1): #Occupied space, we cannot expand here
                #print "(%d,%d) is occupied" % (new_x, new_y)
                checked[new_y][new_x] = 1 # Mark it as checked while at it
                continue
            if (checked[new_y][new_x]): # Already checked, do not expand here
                #print "(%d,%d) is already checked" % (new_x, new_y)
                continue
            to_check.append([new_cost,new_x,new_y])
            expand_table[new_y][new_x] = expand_counter
            expand_counter += 1
        
        print "Checked"
        show_array(checked)
        print "To check"
        show_array(to_check)

search()        
        
        
    