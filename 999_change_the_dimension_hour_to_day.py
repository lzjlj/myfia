
#####这是没有循环处理多个文件的版本，用于查看单个文件的数据处理结果
import netCDF4 as nc
import numpy as np

file_path = "C:\\Users\\zhijiel\\Downloads\\ERA5data_rzsm\\adaptor.mars.internal-2020 - Copy.nc"
ds = nc.Dataset(file_path, 'r')
print(ds.variables.keys())
variables = ['t2m', 'tp', 'swvl1', 'swvl2', 'swvl3', 'rzsm']

for var in variables:
    data = ds.variables[var]  # Access the variable
    if var == 'tp':
        data_sum = data[:].sum(axis=(1, 2))  # This collapses the lat and lon dimensions by taking a sum
        print(data_sum.shape)


        print(f"Shape of {var}_sum:", data_sum.shape)  # Check the shape of data_sum
        data_sum = data_sum[:8760]  # Keep only the first 8760 values
        data_reshaped = data_sum.reshape((365, 24))  # Reshape the data into (365, 24)
        daily_sums = data_reshaped.sum(axis=1)  # Calculate daily sums
        print(f"Daily sums for {var}:", daily_sums)  # Print the results
        print(f"Number of daily sums for {var}:", daily_sums.size)
    else:
        data_mean = data[:].mean(axis=(1, 2))  # This collapses the lat and lon dimensions by taking an average
        if var == 't2m':
            data_mean = data_mean - 273.16  # Subtract 273.16 from 't2m' values
        data_mean = data_mean[:8760]  # Keep only the first 8760 values
        data_reshaped = data_mean.reshape((365, 24))  # Reshape the data into (365, 24)
        daily_means = data_reshaped.mean(axis=1)  # Calculate daily means
        print(f"Daily means for {var}:", daily_means)  # Print the results
        print(f"Number of daily means for {var}:", daily_means.size)



######这是没有循环处理多个文件的版本，用于导出单个文件的数据处理结果
# import netCDF4 as nc
# import numpy as np

# file_path = "C:\\Users\\zhijiel\\Downloads\\ERA5data_rzsm\\adaptor.mars.internal-2020 - Copy.nc"
# ds = nc.Dataset(file_path, 'r')

# variables = ['t2m', 'tp', 'swvl1', 'swvl2', 'swvl3', 'rzsm']
# results = {}

# for var in variables:
#     data = ds.variables[var][:]  # Access and load the entire variable
#     if var == 'tp':
#         data_sum = data.sum(axis=(1, 2))  # Sum over lat and lon
#         data_sum = data_sum[:8760]  # Truncate to 8760 hours (if applicable)
#         data_reshaped = data_sum.reshape((365, 24))  # Reshape to daily data
#         daily_sums = data_reshaped.sum(axis=1)  # Daily sums
#         results[f"{var}_daily_sum"] = daily_sums
#     else:
#         data_mean = data.mean(axis=(1, 2))  # Mean over lat and lon
#         if var == 't2m':
#             data_mean -= 273.16  # Convert Kelvin to Celsius 温度转换为开尔文！！
#         data_mean = data_mean[:8760]  # Truncate
#         data_reshaped = data_mean.reshape((365, 24))  # Reshape
#         daily_means = data_reshaped.mean(axis=1)  # Daily means
#         results[f"{var}_daily_mean"] = daily_means

# # Now, results dictionary contains all the daily sums and means for each variable
# latitude = ds.variables['latitude'][:]
# longitude = ds.variables['longitude'][:]
# ds.close()  # Close the original dataset

# # Step 2: Save the computed results to a new NetCDF file
# new_ds = nc.Dataset("C:\\Users\\zhijiel\\Downloads\\ERA5data_rzsm\\adaptor.mars.internal-2020 - Copy_test.nc", 'w', format='NETCDF4_CLASSIC')

# # Create dimensions
# time_dim = new_ds.createDimension('time', 365)
# lat_dim = new_ds.createDimension('latitude', len(latitude))
# lon_dim = new_ds.createDimension('longitude', len(longitude))

# # Create variables for coordinates
# times = new_ds.createVariable('time', 'f4', ('time',))
# lats = new_ds.createVariable('latitude', 'f4', ('latitude',))
# lons = new_ds.createVariable('longitude', 'f4', ('longitude',))
# times[:] = np.arange(365)
# lats[:] = latitude
# lons[:] = longitude

# # Create variables for computed results and assign data
# for result_name, data in results.items():
#     result_var = new_ds.createVariable(result_name, 'f4', ('time', 'latitude', 'longitude'), fill_value=np.nan)
#     result_var[:, :, :] = np.tile(data[:, np.newaxis, np.newaxis], (1, len(latitude), len(longitude)))

# # Close the new dataset
# new_ds.close()





# *******************************循环处理多个文件
# import os
# import netCDF4 as nc
# from tqdm import tqdm
# import numpy as np

# directory = "E:\\ERA5 data process\\ERA5data_rzsm"
# output_directory = "E:\\ERA5 data process\\ERA5data_hour_to_day"

# files = [f for f in os.listdir(directory) if f.endswith(".nc")]

# for filename in tqdm(files):  # Add progress bar with tqdm
#     file_path = os.path.join(directory, filename)

#     # Open the dataset
#     ds = nc.Dataset(file_path, 'r')

#     variables = ['t2m', 'tp', 'swvl1', 'swvl2', 'swvl3', 'rzsm']
#     results = {}

#     for var in variables:
#         data = ds.variables[var][:]  # Access and load the entire variable
#         if data.shape[0] < 8760:
#             print(f"Skipping variable {var} in file {filename} because it has less than 8760 hours")
#             continue
#         if var == 'tp':
#             data_sum = data.sum(axis=(1, 2))  # Sum over lat and lon
#             data_sum = data_sum[:8760]  # Truncate to 8760 hours (if applicable)
#             data_reshaped = data_sum.reshape((365, 24))  # Reshape to daily data
#             daily_sums = data_reshaped.sum(axis=1)  # Daily sums
#             results[f"{var}_daily_sum"] = daily_sums
#         else:
#             data_mean = data.mean(axis=(1, 2))  # Mean over lat and lon
#             if var == 't2m':
#                 data_mean -= 273.16  # Convert Kelvin to Celsius
#             data_mean = data_mean[:8760]  # Truncate
#             data_reshaped = data_mean.reshape((365, 24))  # Reshape
#             daily_means = data_reshaped.mean(axis=1)  # Daily means
#             results[f"{var}_daily_mean"] = daily_means

#     # Now, results dictionary contains all the daily sums and means for each variable
#     latitude = ds.variables['latitude'][:]
#     longitude = ds.variables['longitude'][:]
#     ds.close()  # Close the original dataset

#     # Step 2: Save the computed results to a new NetCDF file
#     output_file_path = os.path.join(output_directory, f"computed_{filename}")
#     new_ds = nc.Dataset(output_file_path, 'w', format='NETCDF4_CLASSIC')

#     # Create dimensions
#     time_dim = new_ds.createDimension('time', 365)
#     lat_dim = new_ds.createDimension('latitude', len(latitude))
#     lon_dim = new_ds.createDimension('longitude', len(longitude))

#     # Create variables for coordinates
#     times = new_ds.createVariable('time', 'f4', ('time',))
#     lats = new_ds.createVariable('latitude', 'f4', ('latitude',))
#     lons = new_ds.createVariable('longitude', 'f4', ('longitude',))
#     times[:] = np.arange(365)
#     lats[:] = latitude
#     lons[:] = longitude

#     # Create variables for computed results and assign data
#     for result_name, data in results.items():
#         result_var = new_ds.createVariable(result_name, 'f4', ('time', 'latitude', 'longitude'), fill_value=np.nan)
#         result_var[:, :, :] = np.tile(data[:, np.newaxis, np.newaxis], (1, len(latitude), len(longitude)))

#     # Close the new dataset
#     new_ds.close()


# *******************************按照年份合并文件

#####这是循环处理多个文件的版本，并合并为npz文件

import netCDF4 as nc
import numpy as np
import os

folder_path = "E:\ERA5 data process\ERA5data_hour_to_day"

t2m_list = []
tp_list = []
rzsm_list = []

files = [f for f in os.listdir(folder_path) if f.endswith(".nc")]
for file in files:
    t2m_daily_mean = nc.Dataset(os.path.join(folder_path, file), 'r').variables['t2m_daily_mean'][:]
    t2m_list.append(t2m_daily_mean.reshape(1, 365, 121, 241))
    tp = nc.Dataset(os.path.join(folder_path, file), 'r').variables['tp_daily_sum'][:]
    tp_list.append(tp.reshape(1, 365, 121, 241))
    rzsm = nc.Dataset(os.path.join(folder_path, file), 'r').variables['rzsm_daily_mean'][:]
    rzsm_list.append(rzsm.reshape(1, 365, 121, 241))

t2m = np.concatenate(t2m_list, axis=0)
tp = np.concatenate(tp_list, axis=0)
rzsm = np.concatenate(rzsm_list, axis=0)
print(t2m.shape, tp.shape, rzsm.shape)
np.savez("E:\ERA5 data process\ERA5data_hour_to_day\\ERA5-daily.npz", t2m=t2m, tp=tp, rzsm=rzsm)





