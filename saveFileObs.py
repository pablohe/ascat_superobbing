
def saveFileAscci( obs, filename, model ):
  """
  save a Asccii file
  """
  fileOut = open( filename, 'w')

  for row in obs:
    model.writeAscciRow(row, fileOut)

  fileOut.close()



def saveSlots(obs, destinaton, model):
  """
  observations are stored according to the slot to which belong
  """
  import os

  if not os.path.isdir(destinaton): os.mkdir(destinaton)

  for i in range(0,len(obs)): 
    fileOut="obsMA"+str(i).zfill(2)+".dat"
    saveFileAscci( obs[i], destinaton+"/"+fileOut, model)

