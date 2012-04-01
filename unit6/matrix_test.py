from video22 import matrix

num_landmarks = 2

m1 = matrix()
m1.zero(6,6)
row = 0
for i in range(m1.dimx**2):
    column = i % m1.dimx
    m1.value[row][column] = i+1
    if column == m1.dimx-1:
        row += 1

print "m1 initialized"
m1.show()

new_dimx = m1.dimx+2
first_lm_idx = m1.dimx-(num_landmarks*2)
keep_indices = range(0, first_lm_idx)
keep_indices += range(first_lm_idx+2,new_dimx)

print "keep_indices=%s" % repr(keep_indices)

m1 = m1.expand(new_dimx, new_dimx, keep_indices, keep_indices)


print "m1 expanded"
m1.show()
