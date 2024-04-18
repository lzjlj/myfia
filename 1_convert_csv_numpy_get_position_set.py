import pandas as pd
import numpy as np

# 步骤1：读取CSV文件
df = pd.read_csv('./region_all_original_data_location.csv')

# 步骤2：转换为Numpy数组
array = df.to_numpy()

# 步骤3：保存为.npy文件
np.save('./position_set.npy', array)

print(array.shape)