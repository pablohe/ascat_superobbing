
class ModelWRF:
  from datetime import datetime, timedelta
  """
  Model define properties and model constants
  """
  IDWU=2820
  IDWV=2821
  nSlots=3
  
  timeDeltaMinus=timedelta(hours=2,minutes=30)
  timeDeltaPlus =timedelta(hours=0,minutes=30) 
  
  
  def domain(self, obs):
    """ return obs on domain lon [260,340] and lat [-58,-8]"""
    import numpy as np
    
    return np.array(filter( lambda row: -58<=row[1]<=-8 and 260<= row[2] <=340 , obs))



  def anlInterval(self, date, obs):
    """ return obs on time interval """
    from datetime import datetime, timedelta
    import numpy as np
    
    dateI=date-self.timeDeltaMinus
    dateF=date+self.timeDeltaPlus
  
    return np.array(filter( lambda data : dateI <= data[0] <= dateF, obs))
    
  
  def formatObs(self,obs):
  
    """ in date, lat,lon, data wu, data wv,rms
    define format: [date, id, lat,lon, 1013., data, 20.0 ,rms  ] """

    wu=[[ row[0], self.IDWU, row[1],row[2],1013., row[3], 20.0 , row[5]] for row in obs ]
    wv=[[ row[0], self.IDWV, row[1],row[2],1013., row[4], 20.0 , row[5]] for row in obs ]
    
    return wu+wv
    
    
    
  def writeAscciRow(self, row, fileOut): 
    fileOut.write("%d "%row[1])    # id_obs
    fileOut.write("%4.8f "%row[2]) # lat
    fileOut.write("%4.8f "%row[3]) # lon
    fileOut.write("%4.8f "%row[4]) # 1013
    fileOut.write("%4.8f "%row[5]) # dato
    fileOut.write("%4.8f "%row[6]) # rms
    fileOut.write("%4.8f \n"%row[7]) # 20
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
