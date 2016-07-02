class Satellite:

#  def __init__(self):
  
  
  def get_obs():  
    raise NotImplementedError( "Should have implemented this" )
    
  def get_name():  
    raise NotImplementedError( "Should have implemented this" )
    
  def decod_obs():  
    raise NotImplementedError( "Should have implemented this" )

  def prepara_obs():  
    raise NotImplementedError( "Should have implemented this" )
    
#  def parser(archivo):
#  """Parsea un arvhivo de observaciones
#  devuelve una lista de listas( una lista por registro ( fecha, lat, lon, obs, rms ) )

#  """
#  obsFile=open(archivo)  
#  obsMatrix=obsFile.readlines()

#  ret=[]
#  for filaP in obsMatrix:
#  
#      filaRet=[]
#      fila       = re.split(':', filaP)    
#      filaRet.append (datetime(2000+int(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4])))

#      fila[8]=re.split('\n', fila[8])[0]

#      fila[6] = float(fila[6])
#      fila[6] =  (fila[6]-360) if fila[6] > 180.0 else fila[6] # lon -180 a 180

#      for i in (5,6,7,8):   #lat lon obs rms 
#        filaRet.append (float(fila[i]))
#     
#      ret.append(filaRet)

#  return ret
