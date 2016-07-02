#!/usr/bin/env python

import unittest

import superObbing

import datetime

class TestsuperObbing(unittest.TestCase):

  def test_soloWU(self):
    obsIn=[
    [datetime.datetime(2014,1,1,12),2.0,2.24,6.0,1.0,2.0], 
    [datetime.datetime(2014,1,1,12),2.0,2.22,4.0,1.0,2.0]
    ]
    
    obsOutEsperado=[[datetime.datetime(2014,1,1,12),2.0,2.22,5.0,1.0,2.0]]
    
    obsOut = superObbing.superObbing(obsIn)
    self.assertEquals(obsOut,obsOutEsperado)

#  def test_soloWV(self):

#    obsIn=[
#    [datetime.datetime(2014,1,1,18),2.0,2.24,6.0,1.0,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.1 ,5.0,1.0,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.22,4.0,1.0,2.0]
#    ]
#    
#    obsOutEsperado=[ [datetime.datetime(2014,1,1,18),2.0,2.22,5.0,1.0,2.0]]
#    
#    
#    obsOut = superObbing.superObbing(obsIn)
#    self.assertEquals(obsOut,obsOutEsperado)


#      

#  def test_WU3CERCA(self):
#    OBSIN_OBSOUT = [
#    ( [
#    [datetime.datetime(2014,1,1,18),2.0,2.24,1., 6.0,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,1., 5.0,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,1., 4.0,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,6.  ,1., 4.0,2.0]
#    ],[
#    [datetime.datetime(2014,1,1,18),2.0,2. ,1.,5.0,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,6. ,1.,4.0,2.0]
#    ])
#    ]
#    for obsIn, obsOutEsperado in OBSIN_OBSOUT:
#      obsOut = superObbing.superObbing(obsIn)
#      self.assertEquals(obsOut,obsOutEsperado)
#      
#      
#  def test_WUWV3CERCA(self):
#    OBSIN_OBSOUT = [
#    ( [
#    [datetime.datetime(2014,1,1,18),2.0,2.24,1.,6.0,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,1.,5.0,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,1.,4.0,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,6.  ,1.,4.0,2.0]
#    ],[
#    [datetime.datetime(2014,1,1,18),2.0,2. ,1.,5.0,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,6. ,1.,4.0,2.0]
#    ])
#    ]
#    for obsIn, obsOutEsperado in OBSIN_OBSOUT:
#      obsOut = superObbing.superObbing(obsIn)
#      self.assertEquals(obsOut,obsOutEsperado)

#  def test_WU3CERCAWV3CERCA(self):
#    OBSIN_OBSOUT = [
#    ( [
#    [datetime.datetime(2014,1,1,18),2.0,2.24,6.0,1.,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,5.0,1.,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,4.0,1.,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,6.  ,4.0,1.,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,6.1 ,4.0,1.,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,5.9 ,4.0,1.,2.0]    
#    ],[
#    [datetime.datetime(2014,1,1,18),2.0,2. ,5.0,1.,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,5.9,4.0,1.,2.0]
#    ])
#    ]
#    for obsIn, obsOutEsperado in OBSIN_OBSOUT:
#      obsOut = superObbing.superObbing(obsIn)
#      self.assertEquals(obsOut,obsOutEsperado)

#  def test_WU3CERCAWV3CERCAHS(self):
#    OBSIN_OBSOUT = [
#    ( [
#    [datetime.datetime(2014,1,1,18),2.0,2.24,6.0,1.,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,5.0,1.,2.0],
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,4.0,1.,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,6.  ,4.0,1.,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,6.1 ,4.0,1.,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,5.9 ,4.0,1.,2.0],
#    ],[
#    [datetime.datetime(2014,1,1,18),2.0,2.  ,5.0,1.,2.0],
#    [datetime.datetime(2014,1,1,12),2.0,5.9 ,4.0,1.,2.0],
#    ])
#    ]
#    for obsIn, obsOutEsperado in OBSIN_OBSOUT:
#      obsOut = superObbing.superObbing(obsIn)
#      self.assertEquals(obsOut,obsOutEsperado)

    

if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
