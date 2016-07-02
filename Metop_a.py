import Satellite

import subprocess
import sys
from datetime import datetime, timedelta
import os
import numpy as np
import re
import glob


class Metop_a:



  def __init__(self):

    self.__path_scripts="superObbingWRF/"
    self.__path_data   ="superObbingWRF/data/metop_a"



  def getName(self):  
    return "MetOp A"

  
  def getObs(self, date, model):  

    # necesary to get day before
       
    print "Getting... "+date.strftime('%Y%m%d-%H')
    os.system(self.__path_scripts+"/metop_a/get-podaac.sh "+date.strftime('%Y %m %d'))



  def readFileNC(self,filename):
    return self.__read_file(filename)

  def __read_file(self,filename):

    import numpy as np
    from datetime import datetime, timedelta
    import os
    try:
        from netCDF4 import Dataset
    except:
        from Scientific.IO.NetCDF import NetCDFFile as Dataset

    file = Dataset(filename)

  # time
    times = file.variables['time'][:][:]
    registros=(times.shape[0]*times.shape[1]) 
    times =np.resize(times,(times.shape[0]*times.shape[1])) # aplana el vector
    base  = datetime(1990,01,01)    
    times=[ base + timedelta(seconds=int(times[i])) for i in range (times.size) ]


    lats        =self.__read_var(file, 'lat' )
    lons        =self.__read_var(file, 'lon' ) 
    wind_speeds =self.__read_var(file, 'wind_speed')
    wind_dirs   =self.__read_var(file, 'wind_dir')
    
    wvc_quality_flags = file.variables['wvc_quality_flag'][:][:]
    wvc_quality_flagsVector = np.resize(wvc_quality_flags,(wvc_quality_flags.shape[0]*wvc_quality_flags.shape[1])) 

    ret = []
    
    u = np.zeros(lats.size, np.float32)
    v = np.zeros(lats.size, np.float32)

    for i in range(lats.size):    
    # oceanographic convension
      u[i] = wind_speeds[i] *np.sin(wind_dirs[i]*3.14159/180.)
      v[i] = wind_speeds[i] *np.cos(wind_dirs[i]*3.14159/180.)

      
  #  13:01:02:00:27:  -52.50:  137.42:   -6.25

    latMax= 90.
    latMin=-90.

    lonMin=360.
    lonMax=0.


    for i in range(registros):
      
#      if wvc_quality_flagsVector[i]==0 : #and latMin < lats[i] and lats[i] < latMax and lonMin < lons[i] and lons[i] < lonMax  :
#        if ((-80.0 < lats[i]) and (lats[i] < 66.0)):
      fila = []
      fila.append(int( times[i].strftime("%y") ))
      fila.append(int( times[i].strftime("%m") ))
      fila.append(int( times[i].strftime("%d") ))
      fila.append(int( times[i].strftime("%H") ))
      fila.append(int( times[i].strftime("%m") ))
      fila.append(lats[i])
      fila.append(lons[i])
      fila.append(u[i])
      fila.append(v[i])
      fila.append(2.0) # el RMS es fijo, ver pagina 18 ASCAT_Product_Manual
      fila.append(wvc_quality_flagsVector[i])
      ret.append(fila)

    return ret
    
  def __read_var(self,afile, variable):

    import numpy as np
    
    valores       = afile.variables[variable][:][:]
    valoresVector = np.resize(valores,(valores.shape[0]*valores.shape[1]))  
  #  valoresVector = np.array(valores.T)[0]
    
    escala=afile.variables[variable].scale_factor 
 #  maximo =file.variables[variable].valid_max
  #  minimo =file.variables[variable].valid_min
  #  flags=file.variables['wvc_quality_flag']

    valoresVector=valoresVector*escala
     
    
    return  valoresVector #, maximo, minimo, flags

  def decod_file(self,filename):
    """open filename and save txt file.
      output: date, lat, lon, wu, wv, rms"""
    import sys

    ret=self.__read_file(filename)

#    bashCommand=" rm -f "+self.__path_data+"/"+filename+".decod"
#    os.system(bashCommand)

    fileObs = open(self.__path_data+"/"+filename+".decod", 'w')

    for fila in ret:
      date= datetime(2000+int(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4]))
      
      fileObs.write("%s:"%date.strftime("%Y%m%d%H%M") ) #0
      fileObs.write("%5.8f:"%fila[5])                   #1
      fileObs.write("%5.8f:"%fila[6])                   #2
      fileObs.write("%5.5f:"%fila[7])                   #3
      fileObs.write("%5.5f:"%fila[8])                   #4
      fileObs.write("%1.0f \n"%fila[9])                 #5
      

    fileObs.close()
    


    
  def __md5(self,fileName):
    import hashlib
    """Compute md5 hash of the specified file"""
    try:
      fileHandle = open(fileName, "rb")
    except IOError:
      print ("Unable to open the file in readmode: [0]", fileName)
      return
    m5Hash = hashlib.md5()
    while True:
      data = fileHandle.read(8192)
      if not data: break
      m5Hash.update(data)
    fileHandle.close()
    
    return m5Hash.hexdigest()

  def __checkMd5(self, myFile):
    import numpy as np
    import re
    """Check file"""  
   
    fileHash = self.__md5(myFile)
    hashFile = myFile+".md5"
    fileHandle = open(hashFile, "rb")
    fileHandleData = np.array(re.split(' ', fileHandle.read()))[0]
    return  fileHash == fileHandleData



  def decodObs(self,dateANL,model):
    
    dateStart=dateANL-model.timeDeltaMinus
    dateEnd=  dateANL+model.timeDeltaPlus
    
    print "Decoding... "+dateANL.strftime('%Y%m%d-%H')
    self.__decodObsOneDate( dateANL)

    if  dateANL.day  <> dateStart.day :  
      print "Decoding... "+dateStart.strftime('%Y%m%d-%H')
      self.__decodObsOneDate(dateStart)
  
    if dateANL.day <> dateEnd.day  :  
        print "Decoding... "+dateEnd.strftime('%Y%m%d-%H')
        self.__decodObsOneDate(dateEnd)
        




  def __decodObsOneDate(self, date):  
    import glob
    import os 
   
    os.chdir(self.__path_data)

    
    
#   check and uncompress
    for myFile in glob.glob("*.gz"):
      if date.strftime("%Y%m%d") in myFile:
        if not self.__checkMd5(myFile): 
          print "error en md5!" # TODO: usar try y cach ( bajarlo de nuevo si est'a mal )
          # self.get_obs_file(myFile)
        else:
          print myFile+" ok! uncompressing..."
          os.system("gzip -d -f "+myFile)

#    print glob.glob("*.nc")
    
    for myFile in glob.glob("*.nc"):
      if date.strftime("%Y%m%d") in myFile:
        print myFile
        self.decod_file(myFile)
        
#        os.system("rm "+myFile+".gz.md5")
#        os.system("rm "+myFile+".gz")  
#        TODO ver como borrar los archivos




  def readObs(self, dateANL,model):
  
    """
    Read decoded obs
    
    """
  
    path = self.__path_data
    obs = []
    
#    dateStart=dateANL-model.timeDeltaMinus
#    dateEnd=  dateANL+model.timeDeltaPlus
    
    for infile in glob.glob( os.path.join(path, '*'+dateANL.strftime("%Y%m%d")+'*nc.decod*') ):    
      print      infile
      obs=obs+self.parsear(infile)  

#    if dateANL.day <> dateStart.day  :   
#      for infile in glob.glob( os.path.join(path, '*'+dateStart.strftime("%Y%m%d")+'*nc.decod*') ):
#        print      infile
#        obs=obs+self.parsear(infile)

#    if dateANL.day <> dateEnd.day  :         
#      for infile in glob.glob( os.path.join(path, '*'+dateEnd.strftime("%Y%m%d")+'*nc.decod*') ):
#        print      infile
#        obs=obs+self.parsear(infile)

    return obs

  def prepareObs(self, dateANL, model):
    """
    
    """   
    import superObbing
    import matplotlib.pyplot as plt
    
    print self.getName()+" "+str(dateANL)

    dateStart=dateANL-model.timeDeltaMinus
    dateEnd=  dateANL+model.timeDeltaPlus

    obs=self.readObs(dateANL, model)

    dateStart=dateANL-model.timeDeltaMinus
    dateEnd  =dateANL+model.timeDeltaPlus

#    if dateANL.day <> dateStart.day  : obs=np.append(self.readObs(dateStart, model),obs,axis=0)
#    if dateANL.day <> dateEnd.day    : obs=np.append(self.readObs(dateEnd  , model),obs,axis=0)
    
    if dateANL.day <> dateStart.day  : 
      obs=obs+self.readObs(dateStart, model)
      
    if dateANL.day <> dateEnd.day    : 
      obs=obs+self.readObs(dateEnd  , model)


    obs=model.domain(obs)
    obs=model.anlInterval(dateANL, obs)
    
    plt.scatter(obs[:,2],obs[:,1], color="green", s=0.2)
    plt.savefig('sinSO.png', bbox_inches='tight',dpi=900)

    obs=superObbing.superObbing(obs)

    plt.scatter(obs[:,2],obs[:,1], color="blue",  s=0.4)
    plt.savefig('conSO.png', bbox_inches='tight', dpi=900)

    obs=model.formatObs(obs)

    return True, obs

  def getColumn(self, data, column):
    import numpy as np
  
    return np.array([data[:,column]]).reshape(data.shape[0],1)





  def parsear(self,file_):
    """
    Parse a observaron file 
    retur a list of lists ( one list for each record  ( date, lat, lon, datawu, datawv, rms))
    """
    obsFile=open(file_)
    obsMatrix=obsFile.readlines()
    ret=[]
    
    for filaP in obsMatrix:

        filaRet=[]
        
        fila       = re.split(':', filaP.strip())
        filaRet.append ( datetime.strptime(fila[0], '%Y%m%d%H%M'))
        fila[-1]=re.split('\n', fila[-1])[0]
        
        filaRet.append (float(fila[1])) #lat
        filaRet.append (float(fila[2])) #lon
        filaRet.append (float(fila[3])) #wu
        filaRet.append (float(fila[4])) #wv
        filaRet.append (float(fila[5])) #rms

        ret.append(filaRet)

    return ret
  
  
  

