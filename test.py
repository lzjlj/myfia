



# import numpy as np
# import csv 
# import pandas as pd
# from tqdm import tqdm
# from multiprocessing import Process, cpu_count

# df = pd.read_csv("C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\COND_selected_treatment\\_COND_selected_combined_location_drought.csv")

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
#     np_file = './data_with_cond_feiyang/cond_data_combine.npz'
#     np_df = np.load(np_file)
#     #print(np_df['flash_drought_data'].shape)
#     fd_data = np_df['flash_drought_data']
#     sd_data = np_df['slow_drought_data']
#     position_set_data = np_df['position_set_data']

#     for idx, (latitude,longitude,year) in tqdm(enumerate(zip(pd_df['LAT'], pd_df['LON'], pd_df['INVYR'])), desc="position", total=len(pd_df['LAT'])):
#         #print(idx)
#         # if idx == 100:
#         #     break
#         if year > 2020 or year < 1981:
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
#         fd = fd_data[i][year-1981]
#         sd = sd_data[i][year-1981]
#         pd_df.loc[idx, ['num_of_flash_drought', 'mean_duration_flash_drought', 'mean_severity_flash_drought', 'mean_speed_flash_droughts', 'num_of_slow_drought', 'mean_duration_slow_drought', 'mean_severity_slow_drought', 'mean_speed_slow_droughts']] = fd.tolist() + sd.tolist()
#         #print(f"process_id: {idx}", pd_df.loc[idx, ['num_of_flash_drought', 'mean_duration_flash_drought', 'mean_severity_flash_drought', 'mean_speed_flash_droughts', 'num_of_slow_drought', 'mean_duration_slow_drought', 'mean_severity_slow_drought', 'mean_speed_slow_droughts']])
#         #print("process_id: {}, idx: {}".format(process_id, idx))

#     # print(process_id, pd_df[:100])
#     print(f"saving to csv, process_id: {process_id}")
#     pd_df.to_csv(f"C:/FIA-Data/FIA_data/1_COND_selected_all_USA_drought_bilinear_interpolation_{process_id}.csv", index=False)
#     # print(process_id, pd_df[:10])

# if __name__ == '__main__':
#     #np_file = 'drought_data_combine.npz'
#     pd_file = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\COND_selected_treatment\\_COND_selected_combined_location_drought.csv"
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







import pandas as pd

# 读取CSV文件
df1 = pd.read_csv("E:\\insert_county_info\\biomass_ALL_shapefile_county_without_SAP_and_WDLD.csv")
df2 = pd.read_csv("E:\\insert_county_info\\drought_data_with_county_cleaned_modified_uppercase_average.csv")

# 将文件2中的其他值赋予到文件1中的相对位置
merged_df = pd.merge(df1, df2, on=['YEAR', 'STATE', 'COUNTY'], suffixes=('_file1', '_file2'), how='outer')

# 输出合并后的DataFrame
print(merged_df)

# 将结果保存为CSV文件
merged_df.to_csv("E:\\insert_county_info\\biomass_ALL_shapefile_county_without_SAP_and_WDLD_final.csv", index=False)
