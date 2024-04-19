
# select necessary columns from file*****************


import pandas as pd
import os

input_folder = "C:\\FIA-Data\\FIA_data\\USA 50 states data after settling\\P2-chapter2\\COND"
output_folder = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\COND_selected"

for filename in os.listdir(input_folder):
    filepath = os.path.join(input_folder, filename)
    df = pd.read_csv(filepath)
    new_df = df[
            ['CN','PLT_CN','INVYR','STATECD','UNITCD','COUNTYCD','PLOT','COND_STATUS_CD','FLDTYPCD',
 'MAPDEN','STDAGE','STDSZCD','SITECLCD','STDORGCD','CONDPROP_UNADJ','SLOPE','ASPECT','DSTRBCD1','TRTCD1',
 'PRESNFCD','BALIVE','FLDAGE','ALSTK','FORTYPCDCALC','CARBON_DOWN_DEAD','CARBON_LITTER','CARBON_SOIL_ORG',
 'CARBON_STANDING_DEAD','CARBON_UNDERSTORY_AG','CARBON_UNDERSTORY_BG']
             ]
    

    output_filename = os.path.splitext(filename)[0] + "_selected.csv"
    output_filepath = os.path.join(output_folder, output_filename)

    new_df.to_csv(output_filepath, index=False)


# *******************************************************
# this is for [cond] data***************** 
# ['CN','PLT_CN','INVYR','STATECD','UNITCD','COUNTYCD','PLOT','COND_STATUS_CD','FLDTYPCD',
#  'MAPDEN','STDAGE','STDSZCD','SITECLCD','STDORGCD','CONDPROP_UNADJ','SLOPE','ASPECT','DSTRBCD1','TRTCD1',
#  'PRESNFCD','BALIVE','FLDAGE','ALSTK','FORTYPCDCALC','CARBON_DOWN_DEAD','CARBON_LITTER','CARBON_SOIL_ORG',
#  'CARBON_STANDING_DEAD','CARBON_UNDERSTORY_AG','CARBON_UNDERSTORY_BG']
    

# this is for [tree] data***************** 
# [
#  ['CN','PLT_CN','INVYR','STATECD','UNITCD','COUNTYCD','PLOT','SUBP','TREE','AZIMUTH','STATUSCD',
# 'SPCD','SPGRPCD','DIA','HT','TREECLCD','TREEGRCD','AGENTCD','DECAYCD','STOCKING','TOTAGE','PREV_STATUS_CD','TPA_UNADJ',
# 'TPAMORT_UNADJ','DRYBIO_BOLE','DRYBIO_TOP','DRYBIO_STUMP','DRYBIO_SAPLING','DRYBIO_WDLD_SPP','DRYBIO_BG','CARBON_AG','CARBON_BG','DRYBIO_AG']
# ]

# *******************************************************





