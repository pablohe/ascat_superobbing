import makeObs
import modelWRF
import datetime
import Metop_a

satellites=set([])
satellites.add(Metop_a.Metop_a())

dateANL=datetime.datetime(2014,01,01,12)
model=modelWRF.ModelWRF()

success, obs=makeObs.prepararObs(dateANL, satellites, model)

import random
import numpy as np
numbers=range(20)
random.shuffle(numbers)
print "/////////"
print numbers
print "/////////"

while len(numbers) > 0:
    
    target = numbers.pop()
    major = filter( lambda n : n>=target   , numbers)   
    minor = filter( lambda n : n<target     , numbers)
    print target
    print major
    print minor
    numbers=major[:]
    print "-----------------"

