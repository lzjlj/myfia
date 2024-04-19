


import pandas as pd 
import os

file_folder = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\COND_selected\\"
output_folder = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\COND_selected_treatment\\"

for filename in os.listdir(file_folder):
    filepath = os.path.join(file_folder, filename)

    df = pd.read_csv(filepath)
    df = df[df['COND_STATUS_CD']==1] #选出COND_STATUS_CD列中为1的行, 1代表森林

    df = df[df['CARBON_STANDING_DEAD'].notna()] #剔除CARBON_STANDING_DEAD列中为空的行
    df = df[df['CARBON_STANDING_DEAD']!=0] #剔除CARBON_STANDING_DEAD列中不为0的行 0为异常值

    df = df[df['DSTRBCD1'].notna()] #剔除DSTRBCD1列中为空的行

    df = df[df['TRTCD1'].notna()] #剔除TRTCD1列中为空的行
    df = df[df['TRTCD1']==00] #选出TRTCD1列中为值为00的行
    df = df[df['PRESNFCD'].isna()] #选出PRESNFCD列中为空的行
    df = df[(df['INVYR'] >= 1981) & (df['INVYR'] <= 2020)]#选出INVYR列中1981-2020的行

    df = df.drop(['FLDAGE'], axis=1)

    # Create a new filename for the output file by appending "_processed" to the original filename
    output_filename = os.path.splitext(filename)[0] + "_processed.csv"
    output_filepath = os.path.join(output_folder, output_filename)

    df.to_csv(output_filepath, index=False)

# **********************************************************************************************************************

# import pandas as pd
# import os
# file_folder = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\TREE_selected"
# output_folder = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\TREE_selected_treatment"

# for filename in os.listdir(file_folder):
#     filepath = os.path.join(file_folder, filename)

#     df = pd.read_csv(filepath)

#     df = df[df['STATUSCD'].isin([1, 2])]
#     df = df[df['TREECLCD']==2]
#     df = df[df['PREV_STATUS_CD'].notna()]
#     df = df[(df['INVYR'] >= 1981) & (df['INVYR'] <= 2020)]#选出INVYR列中1981-2020的行
#     df = df.drop(['TOTAGE'], axis=1)


#     # Create a new filename for the output file by appending "_processed" to the original filename
#     output_filename = os.path.splitext(filename)[0] + "_processed.csv"
#     output_filepath = os.path.join(output_folder, output_filename)

#     df.to_csv(output_filepath, index=False)


# **********************************************************************************************************************


# import pandas as pd
# import os
# file_path = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\AL_TREE_GRM_ESTN.csv"

# df = pd.read_csv(file_path)

# df = pd.read_csv(filepath)
# df = df[df['STATUSCD']!=0]
# df = df[df['STATUSCD']!=3]
# df = df.drop(['CREATED_BY','CREATED_DATE','CREATED_IN_INSTANCE','MODIFIED_BY','MODIFIED_DATE','MODIFIED_IN_INSTANCE'], axis=1)
    

#     # Create a new filename for the output file by appending "_processed" to the original filename
# output_filename = os.path.splitext(filename)[0] + "_processed.csv"
# output_filepath = os.path.join(file_path_output, output_filename)

# df.to_csv(output_filepath, index=False)









