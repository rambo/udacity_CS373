import hw2

import matplotlib
import matplotlib.pyplot as plot

def add_plot(path, plot, label_txt):
    plot.plot(map(lambda x: x[0], path), map(lambda x: x[1], path), label="%s points" % label_text, linestyle='None')
    smoothed = hw2.smooth(path)
    plot.plot(map(lambda x: x[0], smoothed), map(lambda x: x[1], smoothed), label="%s smoothed" % label_text)
    
add_plot(hw2.testpath1, plot, "path 1")
add_plot(hw2.testpath2, plot, "path 2")

plot.legend(loc='upper right')
plot.show()







