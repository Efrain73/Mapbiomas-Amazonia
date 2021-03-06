#Script para mostras clasif col2 MapbiomasAmazonia
#by:EYTC
# Param
years = [2000,2018] #indicar Años a visualizar

import ee
from ee_plugin import Map
palettes = ['ffffff','129912','1f4423','006400','00ff00','687537','76a5af',
   '29eee4','77a605','935132','bbfcac','45c2a5','b8af4f','bbfcac','ffffb2',
   'ffd966','f6b26b','f99f40','e974ed','d5a6bd','c27ba0','fff3bf','ea9999',
   'dd7e6b','aa0000','ff99ff','0000ff','d5d5e5','dd497f','b2ae7c','af2a2a',
   '8a2be2','968c46','0000ff','4fd3ff']
for num in years:
   descrip = 'classification_'+str(num)
   clasif = ee.Image('projects/mapbiomas-raisg/public/collection2/mapbiomas_raisg_panamazonia_collection2_integration_v2').select(descrip)
            #.select(descrip)
   Map.addLayer(clasif, {'min':0,'max':34,'palette':palettes},descrip,False)
   #print(clasif)
