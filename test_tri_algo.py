from numpy import *
from random import *

import algo_perso as P
import random_table as R
import checktab as C
import algo_Z as Z
import algo_Y as Y
import algo_X as X
i=0
while i<100:
    tab1 = R.random_table(1000,1,100)
    print("avant tri : ",C.checktab(tab1))
    print (tab1)
    P.algo_main(tab1)
    print("après tri : ", C.checktab(tab1))
    print (tab1)
    i+=1