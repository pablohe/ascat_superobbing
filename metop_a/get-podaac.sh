#!/bin/bash


############################## 1 DESTINO ###################################
if [ 1 -ge $# ] ; then
   echo "falta algun paramétro: uso get-podaac.sh yyyy mm dd" 
   exit 1
fi

year=$1
month=$2
day=$3

numeroDeDia=`cat <<EOF | python -
import sys
from datetime import datetime, timedelta

yyyy=int("$year")
mm=int("$month")
d=int("$day")

fecha=datetime(yyyy,mm,d)

print (fecha.strftime("%j") )

EOF`




#source ~/work/scripts/config.inc.sh

cd data/metop_a/

pass=etala@ara.mil.ar
user=anonymous

echo /$year/$numeroDeDia


ftp -iv podaac-ftp.jpl.nasa.gov << EOF_1
  USER $user $pass
  cd /allData/ascat/preview/L2/metop_a/25km/$year/$numeroDeDia
  hash
  bin
  mget *
  close
  bye
EOF_1


