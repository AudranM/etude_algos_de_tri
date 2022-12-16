from numpy import *
from random import *

import random_table as R
import checktab as C
import algo_Z as Z
import algo_Y as Y
import algo_X as X

tab1 = R.random_table(50,1,100)
print("avant tri : ",C.checktab(tab1))
Y.algo_main(tab1)
print (tab1)
print("après tri : ", C.checktab(tab1))


