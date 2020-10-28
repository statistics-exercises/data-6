import matplotlib.pyplot as plt
import numpy as np

# This loads the data that we are going to investigate
x = np.loadtxt("data.dat")

# Your code will go here



# This will produce the final graph
plt.plot( x, y, 'k-' )
plt.savefig("cumulative-pdf.png")
