import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_sorting(self) : 
       fx = x[0]
       for i in range(1,len(x)) :
          self.assertFalse( x[i]<fx, "You did not sort x" )
          fx = x[i]
          
    def test_plotting(self) : 
       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       myx = np.loadtxt("data.dat")
       myx.sort()
       myy = range(1,len(myx)+1)
       myy = [ a / len(myx) for a in myy ]
       for i in range( len(myx) ) :
          self.assertTrue( np.abs(myx[i] - this_x[i])<1e-7, "the x-coordinates of the points in your graph are incorrect" )
          self.assertTrue( np.abs(myy[i]-this_y[i])<1e-7, "the y-coordinates of the points in your graph are incorrect" )
