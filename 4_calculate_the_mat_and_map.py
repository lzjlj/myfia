



#############################这是针对单独一个文件的操作############################################
# import numpy as np
# import os
# data_t2m = np.load("./location_result/t2m_pentad_subset_0.npz")
# mean_t2m_data = np.mean(data_t2m["t2m_pentad_subset"], axis=2)
# np.savez(f"./location_result/mat_pentad_subset_{0}.npz", mean_t2m_datat=mean_t2m_data, position_set_subset=data_t2m["position_set_subset"])




#############################这是针对多个文件的操作 for lpp[############################################

############这是针对于t2m的操作（mat年均温）######################### mean annual temperature

import numpy as np
import os
directory = './location_result'
for filename in os.listdir(directory):
    if filename.endswith(".npz") and filename.startswith("t2m_subset"):
        file_path = os.path.join(directory, filename)
        data_t2m = np.load(file_path)
        #print(f"Keys in {filename}: {list(data_t2m.keys())}")  # This will show what keys are available in the npz file
        mean_t2m_data = np.mean(data_t2m["t2m_subset"], axis=2)
        process_id = filename.split('_')[-1].split('.')[0] # Extract process_id from filename
        output_file_path = f"./bilinear_inter_data/mat/mat_subset_{process_id}.npz"
        np.savez(output_file_path, mat=mean_t2m_data, position_set_subset=data_t2m["position_set_subset"])
       #print(f"Processed and saved data to {output_file_path}")

directory_mat = './bilinear_inter_data/mat'
mat_data = []
position_set_data = []

for i in os.listdir(directory_mat):
    if i.endswith(".npz"):
        data_mat_path = os.path.join(directory_mat, i)
        files = np.load(data_mat_path)
        mat_data.append(files["mat"])
        position_set_data.append(files["position_set_subset"])
mat_data = np.concatenate(mat_data, axis=0)
position_set_data = np.concatenate(position_set_data, axis=0)
print(mat_data.shape, position_set_data.shape)
np.savez("./bilinear_inter_data/mat/combine_mat_subset", mat_data=mat_data, position_set_data=position_set_data)


############################合并文件,只需要更改路径就行############################################

# 这是针对于tp的操作（map年均降水）############################## 

import numpy as np
import os
directory = './location_result'
for filename in os.listdir(directory):
    if filename.endswith(".npz") and filename.startswith("tp_subset"):
        file_path = os.path.join(directory, filename)
        data_tp = np.load(file_path)
        #print(f"Keys in {filename}: {list(data_tp.keys())}")  # This will show what keys are available in the npz file
        sum_tp_data = np.sum(data_tp["tp_subset"], axis=2)   
        process_id = filename.split('_')[-1].split('.')[0] # Extract process_id from filename
        output_file_path = f"./bilinear_inter_data/map/map_subset_{process_id}.npz"
        np.savez(output_file_path, map=sum_tp_data, position_set_subset=data_tp["position_set_subset"])
       #print(f"Processed and saved data to {output_file_path}")

directory_map = './bilinear_inter_data/map'
map_data = []
position_set_data = []


for i in os.listdir(directory_map):
    if i.endswith(".npz"):
        data_map_path = os.path.join(directory_map, i)
        files = np.load(data_map_path)
        map_data.append(files["map"])
        position_set_data.append(files["position_set_subset"])
map_data = np.concatenate(map_data, axis=0)
position_set_data = np.concatenate(position_set_data, axis=0)
print(map_data.shape, position_set_data.shape)
np.savez("./bilinear_inter_data/map/combine_map_subset", map_data=map_data, position_set_data=position_set_data)


