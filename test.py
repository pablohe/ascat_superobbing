import makeObs
import modelWRF
import datetime
import Metop_a

satellites=set([])
satellites.add(Metop_a.Metop_a())

dateANL=datetime.datetime(2014,01,01,12)
model=modelWRF.ModelWRF()
success, obs=makeObs.prepareObs(dateANL, satellites, model)

