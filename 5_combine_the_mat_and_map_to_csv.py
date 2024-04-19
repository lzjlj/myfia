


######################为csv文件中进行赋值

# import numpy as np
# import csv 
# import pandas as pd
# from tqdm import tqdm
# from multiprocessing import Process, cpu_count

# df = pd.read_csv("./region_all_original_data_location.csv")  ############这里的df是更改的，最初是region_all_original_data_location.csv用于计算combine_all_USA_drought_bilinear_interpolation.csv的数据，
# ##然后是combine_all_USA_drought_bilinear_interpolation.csv用于计算mat的数据得到combine_all_USA_mat_bilinear_interpolation.csv
# #然后是combine_all_USA_mat_bilinear_interpolation.csv用于计算combine_all_USA_mat_bilinear_interpolation.csv

# split_idx = len(df) // 8 
# for i in range(8):
#      df1 = df.iloc[i*split_idx:(i+1)*split_idx]
#      df1.to_csv(f"file{i+1}.csv", index=False)
    
# def process_subset(process_id, sub_length):
#     pd_file = f"file{process_id+1}.csv"
#     #np_df = np.load(np_file)
#     #pd_df = pd.read_csv(pd_file)[sub_length*process_id:sub_length*(process_id+1)].copy()
#     pd_df = pd.read_csv(pd_file)
#     # pd_df = pd_df
    
#     #pd_df_subset = pd_df_subset.copy()
#     np_file = './bilinear_inter_data/mat/combine_mat_subset.npz' ######## 'variable' 这里更具变量名称进行修改
#     np_df = np.load(np_file)
#     fd_data = np_df['mat_data']######## 'variable' 这里更具变量名称进行修改
#     position_set_data = np_df['position_set_data']

#     print(fd_data.shape)
#     ###assert 1==2


#     for idx, (latitude,longitude,year) in tqdm(enumerate(zip(pd_df['LAT'], pd_df['LON'], pd_df['INVYR'])), desc="position", total=len(pd_df['LAT'])):
#         #print(idx)
        
#         year = int(year)
#         print("year", year)
#         # if idx == 100:
#         #     break
#         if year > 2020 or year < 2001: # 2001-2020
#             continue
#         #print(year, latitude, longitude)
#         found_flag = False
#         for i, (lat, lon) in enumerate(zip(position_set_data[:, 0], position_set_data[:, 1])):
#             if latitude == lat and longitude == lon:
#                 found_flag = True
#                 break
#         if found_flag == False:
#             print(f"not found: {latitude}, {longitude}")
#             continue
#         fd = fd_data[i][year-2001]
#         pd_df.loc[idx, ['mat_data']] = fd.tolist()  ######## 'variable' 这里更具变量名称进行修改
#         #print(f"process_id: {idx}", pd_df.loc[idx, ['mat_data']])
#         #print("process_id: {}, idx: {}".formap(process_id, idx))

#     # print(process_id, pd_df[:100])
#     print(f"saving to csv, process_id: {process_id}")
#     pd_df.to_csv(f"./bilinear_inter_data/mat/all_USA_mat_bilinear_interpolation_{process_id}.csv", index=False)  ######## 'variable' 这里更具变量名称进行修改
#     # print(process_id, pd_df[:10])

# if __name__ == '__main__':
#     #np_file = 'drought_data_combine.npz'
#     pd_file = "./region_all_original_data_location.csv"    ############ 这里的df是更改的，最初是region_all_original_data_location.csv用于计算combine_all_USA_drought_bilinear_interpolation.csv的数据，然后是combine_all_USA_drought_bilinear_interpolation.csv用于计算mat的数据得到combine_all_USA_mat_bilinear_interpolation.csv
#                                                                                                    #然后是combine_all_USA_mat_bilinear_interpolation.csv用于计算combine_all_USA_mat_bilinear_interpolation.csv
#     #np_df = np.load(np_file)
#     pd_df = pd.read_csv(pd_file)

#     num_processes = cpu_count()
#     print(len(pd_df))
#     df_parts = np.array_split(pd_df, num_processes)
#     sub_length = len(pd_df) // num_processes
#     # assert 1==2
#     print(len(df_parts))


#     processes = []
#     for i, subset in enumerate(df_parts):
#         p = Process(target=process_subset, args=(i, sub_length))
#         processes.append(p)
#         p.start()


#     for p in processes:
#         p.join()

# # # ********************************************************************************************************************************************************

####################Combine the csv files 合并csv文件

import pandas as pd
import os

data_path = "./bilinear_inter_data/map"
FIA = []
for i in os.listdir(data_path):
    if i.endswith(".csv") and i.startswith("all_USA_map"): ######## 'variable' 这里更具变量名称进行修改
            j = os.path.join(data_path, i)
            print(j)
            FIA.append(j)
FIA.sort()
df=pd.concat([pd.read_csv(f) for f in FIA], ignore_index=True)
df.to_csv('./bilinear_inter_data/map/combine_all_USA_map_bilinear_interpolation.csv', index=False) ######## 'variable' 这里更具变量名称进行修改

# ********************************************************************************************************************************************************












