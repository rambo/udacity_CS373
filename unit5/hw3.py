# -------------
# User Instructions
#
# Now you will be incorporating fixed points into
# your smoother. 
#
# You will need to use the equations from gradient
# descent AND the new equations presented in the
# previous lecture to implement smoothing with
# fixed points.
#
# Your function should return the newpath that it
# calculates. 
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#
# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

from math import *

# Do not modify path inside your function.
path=[[0, 0], #fix 
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0], #fix
      [6, 1],
      [6, 2],
      [6, 3], #fix
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3], #fix
      [0, 2],
      [0, 1]]

# Do not modify fix inside your function
fix = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

######################## ENTER CODE BELOW HERE #########################

def smooth(path, fix, weight_data = 0.0, weight_smooth = 0.1, tolerance = 0.00001):
    #
    # Enter code here. 
    # The weight for each of the two new equations should be 0.5 * weight_smooth
    #


    # Make a deep copy of path into newpath
    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    alpha = weight_data
    beta = weight_smooth
    gamma = 0.5 * weight_smooth
    # Seems these tolerances are way too high...
    #tolerance = 0.001 * (len(path)-2)
    tmppath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    last_total_change = 0.0
    while True:
        total_change = 0.0
        for i in range(len(path)):
            if fix[i]: # Fixed point
                continue
            for j in range(len(path[i])): # Update each term (we don't have the matrix class now...)
                # "official example (that in actually a bit wrong, see http://www.udacity-forums.com/cs373/questions/23361/unit5-5-gradient-descent-simultaneous-update)
                tmptmp = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j])
                newpath[i][j] += weight_smooth * (newpath[(i-1)%len(newpath)][j] + newpath[(i+1)%len(newpath)][j] - (2.0 * newpath[i][j]))
                #total_change += abs(tmptmp -  newpath[i][j])

                # The naive (as in not single update ["who cares"]) look-around equations
                newpath[i][j] += gamma * ((2.0*newpath[(i-1)%len(newpath)][j]) - newpath[(i-2)%len(newpath)][j] - newpath[i][j])
                newpath[i][j] += gamma * ((2.0*newpath[(i+1)%len(newpath)][j]) - newpath[(i+2)%len(newpath)][j] - newpath[i][j])

                total_change += abs(tmptmp -  newpath[i][j])

#                # Version doing it properly (from same URL)
#                alpha_value = alpha * (path[i][j] - newpath[i][j])
#                beta_value = beta * (newpath[(i+1)%len(newpath)][j] + newpath[(i-1)%len(newpath)][j] - 2 * newpath[i][j])
#                tmppath[i][j] += alpha_value + beta_value
#                
#                #print "alpha_value=%f beta_value=%f" % (alpha_value, beta_value)
#
#                total_change += abs(alpha_value+beta_value) # This produces a value approaching zero
#
#        newpath = tmppath

        #print "total_change %f (tolerance %f)" % (total_change, tolerance)
        if (   total_change < tolerance # Good enough
            or total_change == last_total_change): # Stops changing
            break
        
        last_total_change = total_change

#    # DEBUG: remove
#    for i in range(len(path)):
#        print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'

    return newpath



#thank you - EnTerr - for posting this on our discussion forum

##newpath = smooth(path)
##for i in range(len(path)):
##    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'

# --------------------------------------------------
# check if two numbers are 'close enough,'used in
# solution_check function.
#
def close_enough(user_answer, true_answer, epsilon = 0.03):
    if abs(user_answer - true_answer) > epsilon:
        return False
    return True

# --------------------------------------------------
# check your solution against our reference solution for
# a variety of test cases (given below)
#
def solution_check(newpath, answer):
    if type(newpath) != type(answer):
        print "Error. You do not return a list."
        return False
    if len(newpath) != len(answer):
        print 'Error. Your newpath is not the correct length.'
        return False
    if len(newpath[0]) != len(answer[0]):
        print 'Error. Your entries do not contain an (x, y) coordinate pair.'
        return False
    for i in range(len(newpath)): 
        for j in range(len(newpath[0])):
            if not close_enough(newpath[i][j], answer[i][j]):
                print 'Error, at least one of your entries is not correct.'
                return False
    print "Test case correct!"
    return True

# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

testpath1=[[0, 0], #fix
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0], #fix
      [6, 1],
      [6, 2],
      [6, 3], #fix
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3], #fix
      [0, 2],
      [0, 1]]
testfix1 = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
answer1 = [[0, 0],
           [0.7938620981547201, -0.8311168821106101],
           [1.8579052986461084, -1.3834788165869276],
           [3.053905318597796, -1.5745863173084],
           [4.23141390533387, -1.3784271816058231],
           [5.250184859723701, -0.8264215958231558],
           [6, 0],
           [6.415150091996651, 0.9836951698796843],
           [6.41942442687092, 2.019512290770163],
           [6, 3],
           [5.206131365604606, 3.831104483245191],
           [4.142082497497067, 4.383455704596517],
           [2.9460804122779813, 4.5745592975708105],
           [1.768574219397359, 4.378404668718541],
           [0.7498089205417316, 3.826409771585794],
           [0, 3],
           [-0.4151464728194156, 2.016311854977891],
           [-0.4194207879552198, 0.9804948340550833]]

testpath2 = [[0, 0], # fix
             [2, 0],
             [4, 0], # fix
             [4, 2],
             [4, 4], # fix
             [2, 4],
             [0, 4], # fix
             [0, 2]]
testfix2 = [1, 0, 1, 0, 1, 0, 1, 0]
answer2 = [[0, 0],
           [2.0116767115496095, -0.7015439080661671],
           [4, 0],
           [4.701543905420104, 2.0116768147460418],
           [4, 4],
           [1.9883231877640861, 4.701543807525115],
           [0, 4],
           [-0.7015438099112995, 1.9883232808252207]]


## My DEBUGs, comment out
#print "Test path 1"
#solution_check(smooth(testpath2, testfix2), answer2)
#print "Test path 1"
#solution_check(smooth(testpath2, testfix2), answer2)


