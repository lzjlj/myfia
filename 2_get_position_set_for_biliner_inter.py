
import pandas as pd
import numpy as np

position_set_path = "./position_set.npy"

file = "./region_all_original_data_location.csv"
df = pd.read_csv(file)[["LAT", "LON"]]
print(df.info())
#print(df.head)
print(df.shape)

position_set = set() ##这行代码创建了一个空的集合对象，集合中的每一个元素都是唯一的，集合中的元素是无序的，集合中的元素是不可变的（不可变的意思是不能修改元素，不能删除元素，不能添加元素）。因此，position_set 最终将包含所有不重复的、保留两位小数的经纬度对。153564

for index, row in df.iterrows():##遍历每一行 iterrows() 方法返回 DataFrame 中每一行的索引和对应的数据作为一个元组，但有时候在循环中并不需要索引值。这时可以通过设置参数 index=False 来去掉索引值。
    position = (round(row["LAT"],2), round(row["LON"],2)) ##对经纬度进行四舍五入，保留两位小数
    pre_len = len(position_set)
    position_set.add(position)


print(type(position_set))  # 输出集合的类型
print(len(position_set))   # 输出集合中元素的数量

np.save(position_set_path, np.array(list(position_set)))



#####list(position_set): 将集合 position_set 转换为列表，因为 NumPy 数组的输入应该是一个列表或数组。
#####np.array(list(position_set)): 将列表转换为 NumPy 数组，因为 NumPy 数组是 NumPy 库的核心数据结构。
#####np.save(position_set_path, np.array(list(position_set))): 将 NumPy 数组保存为一个名为 position_set.npy 的文件。 position_set_path 是保存文件的路径。



