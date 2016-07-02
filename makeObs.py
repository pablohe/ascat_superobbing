#!/usr/bin/env python


path_work="./"
path_scripts="./"


def getObs(dateANL, satellites, model):
  """
  get observactions of all satellites in set for dateANL

  """
  success = False
  
  dateStart=dateANL-model.timeDeltaMinus
  dateEnd  =dateANL+model.timeDeltaPlus
  
  for satellite in satellites:
    satellite.getObs(dateANL, model)   
    if dateANL.day <> dateStart.day  : satellite.getObs(dateStart, model)
    if dateANL.day <> dateEnd.day    : satellite.getObs(dateEnd, model)

  

def decodObs(dateANL, satellites, model):
  """
  decod observactions of all satellites in set for dateANL

  """
  dateStart=dateANL-model.timeDeltaMinus
  dateEnd  =dateANL+model.timeDeltaPlus

  for satellite in satellites:
    satellite.decodObs(dateANL, model)
    if dateANL.day <> dateStart.day  : satellite.decodObs(dateANL, model) 
    if dateANL.day <> dateEnd.day    : satellite.decodObs(dateANL, model) 
    


def prepareObs(dateANL, satellites, model):
  """
  Prepare* observactions of all satellites in set
  *call satellite.prepararObs()
  """
  import numpy as np
  res=[]
  success = False
  
  for satellite in satellites:
    success, data = satellite.prepareObs(dateANL, model)
    if success: res = res+data

  return success, np.array(res)




def splitObsInSlots(obs, dateANL, model):
  """  split Obs in slot files """
  from datetime import datetime, timedelta
  import numpy as np
  ret=[]
  obsTotal=0

  for i in range(1,model.nSlots+1): 

    dateI=dateANL-model.timeDeltaMinus                   +timedelta(hours=i-1)
    dateF=dateANL-model.timeDeltaMinus+timedelta(hours=1)+timedelta(hours=i-1)-timedelta(minutes=1)

    obs_i=np.array(filter( lambda data : dateI <= data[0] <= dateF, obs))
    
    obsTotal+=len(obs_i)

    print "slot "+str(i)+": "+str(len(obs_i))
    print dateI
    print dateF
    
    print " "
    ret.append(obs_i)

  print "obs total: "+str(obsTotal)
  
  return ret



def main(args):


  import Metop_a
  import modelWRF
  import datetime
  import saveFileObs
  
  satellites=[]
  model=modelWRF.ModelWRF()

  dateANL=args.dateANL
  if args.metop_a : satellites.append(Metop_a.Metop_a())

  if args.get     : 
    success      = getObs(dateANL, satellites, model)    
    print "getting..."+str(success)

  if args.decod     :
    success      = decodObs(dateANL, satellites, model)    
    print "decoding..."+str(success)

  if args.prepare :  
    print "preparing..." 
    success, obs =prepareObs(dateANL, satellites, model)
    
    if not success: print "no hay observaciones"
    else: slotsObs=splitObsInSlots(obs, dateANL, model)
  
#  obs,aceptados, descartados, rmsValorChicas = testerObs(obs, args.debug)
    saveFileObs.saveSlots(slotsObs, args.destinaton, model)







if __name__ == "__main__":

  import argparse

  def mkdate(datestring):
      from datetime import datetime, timedelta

      return datetime.strptime(datestring, '%Y%m%d-%H')

  parser = argparse.ArgumentParser()
  
  parser.add_argument('dateANL', type=mkdate, help="Date [YYYYmmdd-hh] of analisis time")
                    
  parser.add_argument('--NoMetop_a', action='store_false', default=True,
                    dest='metop_a',
                    help='Don\'t make observations from metop a')                    

  parser.add_argument('--NoGet', action='store_false', default=True,
                      dest='get',
                      help='Don\'t get observations')                    

  parser.add_argument('--NoDecod', action='store_false', default=True,
                      dest='decod',
                      help='Don\'t get observations')                    

  parser.add_argument('--NoPrepare', action='store_false', default=True,
                      dest='prepare',
                      help='Don\'t prepare Observations')                    


  parser.add_argument('--debug', action='store_true', default=False,
                    dest='debug',
                    help='debug mode')              


  parser.add_argument('destinaton', help="folder to save slots files (obsXX.dat)")

  args = parser.parse_args()
  main(args)  
#    


  

  





#  
