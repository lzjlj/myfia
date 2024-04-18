


#********************************************************************************************************************
#********************************************************************************************************************
####################################这是单个文件处理的代码

# import numpy as np
# from netCDF4 import Dataset

# # # Open the NetCDF file
# file_path = "E:\\ERA5 data process\\ERA5data_original\\adaptor.mars.internal-2003.nc"
# nc_data = Dataset(file_path, mode='r')

# # # Read variables
# longitude = nc_data.variables['longitude'][:]
# latitude = nc_data.variables['latitude'][:]
# time_hour = nc_data.variables['time'][:]
# t2m = nc_data.variables['t2m'][:8760] - 273.15  # Convert Kelvin to Celsius
# tp = nc_data.variables['tp'][:8760]
# swvl1 = nc_data.variables['swvl1'][:8760]
# swvl2 = nc_data.variables['swvl2'][:8760]
# swvl3 = nc_data.variables['swvl3'][:8760]

# # # Compute root zone soil moisture (rzsm)
# rzsm = swvl1 * 0.07 + swvl2 * 0.21 + swvl3 * 0.72

# # # Reshape and calculate daily means or sums
# t2m_reshaped = t2m.reshape(241, 121, 365, 24)
# t2m_daily_mean = np.mean(t2m_reshaped, axis=3)

# tp_reshaped = tp.reshape(241, 121, 365, 24)
# tp_daily_mean = np.mean(tp_reshaped, axis=3)

# rzsm_reshaped = rzsm.reshape(241, 121, 365, 24)
# rzsm_daily_mean = np.mean(rzsm_reshaped, axis=3)

# # # Close the original data file
# nc_data.close()

# # # Create a new NetCDF file
# outputfile = "E:\\ERA5 data process\\daily_mean\\daymean_adaptor.mars.internal-2003.nc"
# nc_new = Dataset(outputfile, 'w', format='NETCDF4')

# # # Define dimensions
# longitude_dim = nc_new.createDimension('longitude', len(longitude))
# latitude_dim = nc_new.createDimension('latitude', len(latitude))
# time_dim = nc_new.createDimension('time', 365)

# # # Create variables
# longitude_var = nc_new.createVariable('longitude', 'f4', ('longitude',))
# latitude_var = nc_new.createVariable('latitude', 'f4', ('latitude',))
# time_var = nc_new.createVariable('time', 'i4', ('time',))

# longitude_var[:] = longitude
# latitude_var[:] = latitude
# time_var[:] = np.arange(1, 366)

# t2m_var = nc_new.createVariable('t2m', 'f8', ('longitude', 'latitude', 'time'), fill_value=False)
# tp_var = nc_new.createVariable('tp', 'f8', ('longitude', 'latitude', 'time'), fill_value=False)
# rzsm_var = nc_new.createVariable('rzsm', 'f8', ('longitude', 'latitude', 'time'), fill_value=False)

# # # Put data
# t2m_var[:, :, :] = t2m_daily_mean
# tp_var[:, :, :] = tp_daily_mean
# rzsm_var[:, :, :] = rzsm_daily_mean

# # # Close the new file
# nc_new.close()



#********************************************************************************************************************
#********************************************************************************************************************
#####################################################这是循环处理多个文件的代码

# import numpy as np
# from netCDF4 import Dataset
# import os

# path_files = "E:\\ERA5 data process\\ERA5data_original"
# files = [f for f in os.listdir(path_files) if f.endswith(".nc")]

# for filename in files:
#     i = os.path.join(path_files, filename)
#     year = int(filename.split('-')[1].split('.')[0])
#     nc_data = Dataset(i, mode='r')
#     # Read variables
#     longitude = nc_data.variables['longitude'][:]
#     latitude = nc_data.variables['latitude'][:]
#     time_hour = nc_data.variables['time'][:]
#     t2m = nc_data.variables['t2m'][:8760] - 273.15  # Convert Kelvin to Celsius
#     tp = nc_data.variables['tp'][:8760]
#     swvl1 = nc_data.variables['swvl1'][:8760]
#     swvl2 = nc_data.variables['swvl2'][:8760]
#     swvl3 = nc_data.variables['swvl3'][:8760]
#     rzsm = swvl1 * 0.07 + swvl2 * 0.21 + swvl3 * 0.72

#     # Reshape and calculate daily means or sums
#     t2m_reshaped = t2m.reshape(241, 121, 365, 24)
#     t2m_daily_mean = np.mean(t2m_reshaped, axis=3)

#     tp_reshaped = tp.reshape(241, 121, 365, 24)
#     tp_daily_mean = np.mean(tp_reshaped, axis=3)

#     rzsm_reshaped = rzsm.reshape(241, 121, 365, 24)
#     rzsm_daily_mean = np.mean(rzsm_reshaped, axis=3)

#     # Close the original data file
#     nc_data.close()
    
#     # Create a new NetCDF file
#     outputfile = f"E:\\ERA5 data process\\daily_mean\\daymean_adaptor.mars.internal-{year}.nc"
#     nc_new = Dataset(outputfile, 'w', format='NETCDF4')

#     # Define dimensions
#     longitude_dim = nc_new.createDimension('longitude', len(longitude))
#     latitude_dim = nc_new.createDimension('latitude', len(latitude))
#     time_dim = nc_new.createDimension('time', 365)

#     # Create variables
#     longitude_var = nc_new.createVariable('longitude', 'f4', ('longitude',))
#     latitude_var = nc_new.createVariable('latitude', 'f4', ('latitude',))
#     time_var = nc_new.createVariable('time', 'i4', ('time',))

#     longitude_var[:] = longitude
#     latitude_var[:] = latitude
#     time_var[:] = np.arange(1, 366)

#     t2m_var = nc_new.createVariable('t2m', 'f8', ('longitude', 'latitude', 'time'), fill_value=False)
#     tp_var = nc_new.createVariable('tp', 'f8', ('longitude', 'latitude', 'time'), fill_value=False)
#     rzsm_var = nc_new.createVariable('rzsm', 'f8', ('longitude', 'latitude', 'time'), fill_value=False)

#     # Put data
#     t2m_var[:, :, :] = t2m_daily_mean
#     tp_var[:, :, :] = tp_daily_mean
#     rzsm_var[:, :, :] = rzsm_daily_mean

#     # Close the new file
#     nc_new.close()

#********************************************************************************************************************
#********************************************************************************************************************

#############################这是将多个文件合并成一个文件的代码
import netCDF4 as nc
import numpy as np
import os

folder_path = "E:\\ERA5 data process\\ERA5daily_mean"
files = [f for f in os.listdir(folder_path) if f.endswith(".nc")]

t2m_list = []
tp_list = []
rzsm_list = []

files = [f for f in os.listdir(folder_path) if f.endswith(".nc")]
for file in files:
    t2m_daily_mean = nc.Dataset(os.path.join(folder_path, file), 'r').variables['t2m'][:]
    t2m_list.append(t2m_daily_mean.reshape(241, 121, 365, 1))

    tp_daily_mean = nc.Dataset(os.path.join(folder_path, file), 'r').variables['tp'][:]
    tp_list.append(tp_daily_mean.reshape(241, 121, 365, 1))

    rzsm_daily_mean = nc.Dataset(os.path.join(folder_path, file), 'r').variables['rzsm'][:]
    rzsm_list.append(rzsm_daily_mean.reshape(241, 121, 365, 1))

t2m = np.concatenate(t2m_list, axis=3).transpose(3, 2, 1, 0) #将维度从(241, 121, 365, 20)转为(20, 365, 121, 241)为了与cfy写的代码保持一致
tp = np.concatenate(tp_list, axis=3).transpose(3, 2, 1, 0)
rzsm = np.concatenate(rzsm_list, axis=3).transpose(3, 2, 1, 0)
print(t2m.shape, tp.shape, rzsm.shape)


np.savez("E:\\ERA5 data process\\ERA5daily_mean\\combine_daily_mean.npz", t2m=t2m, tp=tp, rzsm=rzsm)

#print("E:\\ERA5 data process\\ERA5daily_mean\\combine_daily_mean.npz")


