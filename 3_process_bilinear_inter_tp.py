# input: position set
# input： dataset
# 对温度进行插值计


import numpy as np
from netCDF4 import Dataset
from tqdm import tqdm
from scipy import stats
from multiprocessing import Process, cpu_count

position_set = np.load("./position_set.npy") #导入集合
print(position_set.shape)
# shape: (166092, 2) #############################################更改update后成为了(153564, 2) 第一个维度的大小是153564 (与代码2中的集合中的值保持相同)， 第二个维度的大小是LAT, LON

# 得到初始经纬度值
example_file = "./computed_adaptor.mars.internal-2001.nc"
nc_data = Dataset(example_file, 'r')
data_key = nc_data.variables.keys()
longitude = nc_data.variables['longitude'][:]
latitude = nc_data.variables['latitude'][:]


# 读入大原始数据
with np.load("E:\\ERA5 data process\\ERA5daily_mean\\combine_daily_mean.npz") as npz: #这里是导入的合并的2001-2020年的daily_mean数据
    #data = np.ma.MaskedArray(**npz)#############################################不知道什么意思，问CFY
    data = npz['tp']
print(data.shape) # shape (20, 365, 121, 241)这个是维度(年，天，纬度，经度)


#插值函数
def bilinear_interpolation(x, y, points):
    '''Interpolate (x,y) from values associated with four points.

    The four points are a list of four triplets:  (x, y, value).
    The returned value is a float.
    '''
    # See formula at:  https://en.wikipedia.org/wiki/Bilinear_interpolation

    points = sorted(points)               # order points by x, then by y
    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

    if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
        raise ValueError('points do not form a rectangle')
    if not x1 <= x <= x2 or not y1 <= y <= y2:
        raise ValueError('(x, y) not within the rectangle')

    return (q11 * (x2 - x) * (y2 - y) +
            q21 * (x - x1) * (y2 - y) +
            q12 * (x2 - x) * (y - y1) +
            q22 * (x - x1) * (y - y1)
           ) / ((x2 - x1) * (y2 - y1) + 0.0)



# def compute_percentile(data):
#     # data: shape (# of years, # of pentad days) 
#     # output (soil moisture percentile): shape (# of years, # of pentad days)

#     assert len(data.shape) == 2
#     num_years, num_pentad_days = data.shape

#     soil_moisture_percentiles = np.zeros((num_years, num_pentad_days))
#     for day in range(num_pentad_days):
#         l = data[:, day].flatten()
#         for year in range(num_years):
#             soil_moisture = data[year, day]
#             soil_moisture_percentile_1 = stats.percentileofscore(l, soil_moisture)       
#             soil_moisture_percentiles[year, day] = soil_moisture_percentile_1
#     return soil_moisture_percentiles



# 多线程的代码
def process_subset(position_set_subset, process_id):
    print("process_id: {}, len(position_set_subset): {}".format(process_id, len(position_set_subset)))
    tp_pentad_subset = np.empty((len(position_set_subset), 20, 365)) ########### 这个函数创建了一个新的数组，其形状由参数指定，但不会初始化数组元素，只是分配了数组的内存空间。
    ####################len(position_set_subset): 这是position_set_subset的长度，可能是一个包含位置的列表或数组。
    ##############################20: 这是数组的第二维。看起来你正在为20个元素分配空间。
    #################################365: 这是数组的第三维。它可能计算一年中的天的数量

    #position_set_subset = np.empty((len(position_set_subset), 2))

    for i, (lat, lon) in tqdm(enumerate(position_set_subset), desc="position", total=len(position_set_subset)):
        assert lat <= latitude[0] and lat >= latitude[-1], "i: {}, lat: {}, lon: {}".format(i, lat, lon) # reverse order
        assert lon >= longitude[0] and lon <= longitude[-1], "i: {}, lat: {}, lon: {}".format(i, lat, lon)
        lon_idx = int((lon - longitude[0]) // (longitude[1] - longitude[0]))
        lat_idx = int((latitude[0] - lat) // (latitude[0] - latitude[1]))
        assert latitude[lat_idx+1]<=lat<=latitude[lat_idx]
        assert longitude[lon_idx]<=lon<=longitude[lon_idx+1]
        position_index = np.array([(lat_idx+1, lon_idx), (lat_idx+1, lon_idx+1), (lat_idx, lon_idx), (lat_idx, lon_idx+1)])
        position_data = data[:, :, position_index[:, 0], position_index[:, 1]] # (40, 183, 4)
        position_data = position_data.reshape(-1, 4)

        tp_bilinear_interpolation = np.empty((position_data.shape[0]))
        for k, position_data_daily in tqdm(enumerate(position_data), desc="daily", total=position_data.shape[0], leave=False):
            points = ((latitude[lat_idx+1], longitude[lon_idx], position_data_daily[0]), \
                      (latitude[lat_idx+1], longitude[lon_idx+1], position_data_daily[1]), \
                      (latitude[lat_idx], longitude[lon_idx], position_data_daily[2]), \
                      (latitude[lat_idx], longitude[lon_idx+1], position_data_daily[3]))
            interpolated_data = bilinear_interpolation(lat, lon, points)
            tp_bilinear_interpolation[k] = interpolated_data
        tp_bilinear_interpolation = tp_bilinear_interpolation.reshape(20, 365)
        # moisture_bilinear_interpolation_pentad = np.empty((20, 365))
        # for pentad_day in range(365):
        #     pentad_data = moisture_bilinear_interpolation[:, pentad_day*5:(pentad_day+1)*5]
            # moisture_bilinear_interpolation_pentad[:, pentad_day] = np.mean(pentad_data, axis=1)
        # percentile_pentad = compute_percentile(moisture_bilinear_interpolation_pentad)
        tp_pentad_subset[i] = tp_bilinear_interpolation
    # save the percentile_pentad_subset and position_set_subset
    np.savez(f"./location_result/tp_pentad_subset_{process_id}.npz", tp_pentad_subset=tp_pentad_subset, position_set_subset=position_set_subset)
                                                                                                                                                                                                          
#final_data = np.empty((len(position_set), 20, 365))

if __name__ == '__main__':
    num_processes = 8
    #num_processes = 1
    position_set_subsets = np.array_split(list(position_set), num_processes)

    processes = []
    for i, subset in enumerate(position_set_subsets):
        p = Process(target=process_subset, args=(subset, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()