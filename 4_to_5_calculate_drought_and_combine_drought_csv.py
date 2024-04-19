

# ********************************************************************************************************************************************************
# TEST

# import pandas as pd
# import numpy as np

# final = np.load('./data_with_drought/percentile_pentad_subset_0_drought.npz')
# print(final.keys())
# print(final["position_set_subset"].shape)

# for i in range(1000):
#     print(final["position_set_subset"][i])
#     print(final["flash_drought_data"][i])
#     break

# *****************************************************************************************************************************************************

#执行此代码的前一步的过程是在费杨电脑上进行的
# Combine the npz files, 这是针对慢旱和闪旱的数据   

# import numpy as np
# flash_drought_data = []
# slow_drought_data = []
# percentile_pentad_data = []
# position_set_data = []
# for i in range(8):
#     data_path = f"./bilinear_inter_data/percentile/percentile_pentad_subset_{i}.npz"
#     data = np.load(data_path)
#     flash_drought_data.append(data["flash_drought_data"])
#     slow_drought_data.append(data["slow_drought_data"])
#     percentile_pentad_data.append(data["percentile_pentad_subset"])
#     position_set_data.append(data["position_set_subset"])
# flash_drought_data = np.concatenate(flash_drought_data, axis=0)
# slow_drought_data = np.concatenate(slow_drought_data, axis=0)
# percentile_pentad_data = np.concatenate(percentile_pentad_data, axis=0)
# position_set_data = np.concatenate(position_set_data, axis=0)
# print(flash_drought_data.shape, slow_drought_data.shape, percentile_pentad_data.shape, position_set_data.shape)
# np.savez("./bilinear_inter_data/percentile/combine_percentile_pentad_subset.npz", slow_drought_data=slow_drought_data, flash_drought_data=flash_drought_data, percentile_pentad_data=percentile_pentad_data, position_set_data=position_set_data)


# # *****************************************************************************************************************************************************

# 为csv文件中进行赋值

# import numpy as np
# import pandas as pd
# from tqdm import tqdm
# from multiprocessing import Process, cpu_count

# df = pd.read_csv("./region_all_original_data_location.csv")

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
#     np_file = './bilinear_inter_data/percentile/combine_percentile_pentad_subset.npz'
#     np_df = np.load(np_file)
#     #print(np_df['flash_drought_data'].shape)
#     fd_data = np_df['flash_drought_data']
#     sd_data = np_df['slow_drought_data']
#     position_set_data = np_df['position_set_data']

#     print(fd_data.shape, sd_data.shape)
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
#         sd = sd_data[i][year-2001]
#         pd_df.loc[idx, ['num_of_flash_drought', 'mean_duration_flash_drought', 'mean_severity_flash_drought', 'mean_speed_flash_drought', 'num_of_slow_drought', 'mean_duration_slow_drought', 'mean_severity_slow_drought', 'mean_speed_slow_drought']] = fd.tolist() + sd.tolist()
#         #print(f"process_id: {idx}", pd_df.loc[idx, ['num_of_flash_drought', 'mean_duration_flash_drought', 'mean_severity_flash_drought', 'mean_speed_flash_droughts', 'num_of_slow_drought', 'mean_duration_slow_drought', 'mean_severity_slow_drought', 'mean_speed_slow_droughts']])
#         #print("process_id: {}, idx: {}".format(process_id, idx))

#     # print(process_id, pd_df[:100])
#     print(f"saving to csv, process_id: {process_id}")
#     pd_df.to_csv(f"./bilinear_inter_data/percentile/all_USA_drought_bilinear_interpolation_{process_id}.csv", index=False)
#     # print(process_id, pd_df[:10])

# if __name__ == '__main__':
#     #np_file = 'drought_data_combine.npz'
#     pd_file = "./region_all_original_data_location.csv"
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

# # # # ********************************************************************************************************************************************************

# # Combine the csv files 合并csv文件

import pandas as pd
import os

data_path = "./bilinear_inter_data/percentile"
FIA = []
for i in os.listdir(data_path):
    if i.endswith(".csv") and i.startswith("all_USA_drought_bilinear_interpolation") :
            j = os.path.join(data_path, i)
            print(j)
            FIA.append(j)
FIA.sort()
df=pd.concat([pd.read_csv(f) for f in FIA], ignore_index=True)
df.to_csv('./bilinear_inter_data/percentile/combine_all_USA_drought_bilinear_interpolation.csv', index=False)

# # ********************************************************************************************************************************************************



