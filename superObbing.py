#!/usr/bin/env python

"""
SUPEROBBING 
pablohe@gmail.com
24/01/2014
"""
DIST=0.5


def averageObs(nearData, target):  
  """
  Make averageObs obs:
  targetTimeStamp, TargetLat, TargetLon, meanOfWU, meanOfWV, targetRMS
  
  """
  import numpy as np

#  target==np.array(target) 
#  nearData=np.array(nearData)
  
#  print "target"
#  print target
#  print "---------"
#  print "near"
#  print nearData
#  
  nearData=np.array(nearData)

  if len(nearData) == 0: ret = target
  else: ret=[target[0], target[1],target[2],np.mean(nearData[:,3]),np.mean(nearData[:,4]), target[5]]

  
  return ret 



def superObbing(obs):
  """
  Make superObbing:
  
    take one observation (target)
    split obs into two subsets: near and far
    call newTarget=averageObs(near, target)
    add target to result Set of Observations 
    repeat while obs set is not empy
  
  """
  import numpy as np
  obs=obs.tolist()  
  ret=[]
  
  while len(obs) > 0:
#  for target in obs:
#    nearData = [row for row in obs if       np.sqrt( (row[1] - target[1])**2 + (row[2]-target[2])**2) <= DIST ]
#    obs      = [row for row in obs if  not (np.sqrt( (row[1] - target[1])**2 + (row[2]-target[2])**2) <= DIST)]
    target=obs.pop()

    nearData = filter( lambda row :     np.sqrt( (row[1]-target[1])**2 + (row[2]-target[2])**2 ) <= DIST , obs)
    obs      = filter( lambda row : not np.sqrt( (row[1]-target[1])**2 + (row[2]-target[2])**2 ) <= DIST , obs)

    nearDataAverage = averageObs( nearData, target )  
#    print nearDataAverage
    ret.append(nearDataAverage)
       
#    print len(nearDataAverage)
#    print len(obs)
#    print len(ret) 
#    print "ret"
#    print ret
  
  return np.array(ret)
  





