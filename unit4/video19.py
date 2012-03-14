# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------


class position:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def clone(self):
        return position(self.x, self.y, self.heading)

    def move(self, action_idx):
        """Calculate new position when given an index from the action array"""
        action_val = action[action_idx]
        # Get the correct dimension vector based on current heading and action modifier
        move_val = forward[(self.heading + action_val) % len(forward)]
        # Calculate new x and y
        self.x += move_val[0]
        self.y += move_val[1]
        # update the heading
        self.heading = (self.heading + action_val) % len(forward)

def print_2d_array(a):
    for i in range(len(a)):
        print a[i]

def action_name2idx(aname):
    return action_name.index(aname)

def test_drive(actions):
    drive_grid = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    p = position(init[0], init[1], init[2])
    for a in actions:
        action_idx = action_name2idx(a)
        drive_grid[p.x][p.y] = a
        p.move(action_idx)
    print_2d_array(drive_grid)

test_drive(['#','L', 'R', '#', 'L', 'L', '#'])

def optimum_policy2D():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    h = init[2]
    g = 0

    open = [[g, x, y, []]]

    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            next = open.pop(0) # we can pop the zeroeth element, no need to reverse
#            open.reverse()
#            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    actions = next[3][:] # Create a copy by slicing
                    actions.append(i)
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2, actions])
                            closed[x2][y2] = 1
    path = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))] # init empty path
    path[x][y] = '*'
    actions = next[3]
    path_x = init[0]
    path_y = init[1]
    for i in range(len(actions)):
        path[path_x][path_y] = delta_name[actions[i]]
        path_x += delta[actions[i]][0]
        path_y += delta[actions[i]][1]
        
    for i in range(len(path)):
        print path[i]

    return policy2D # Make sure your function returns the expected grid.




