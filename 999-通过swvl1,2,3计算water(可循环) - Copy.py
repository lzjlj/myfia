
# # **********************************这是没有循环的版本
# import netCDF4 as nc
# import numpy as np

# # Open the NetCDF file
# file_path = "C:\\Users\\zhijiel\\Downloads\\ERA5data_original\\adaptor.mars.internal-2020 - Copy.nc"
# ds = nc.Dataset(file_path, 'r')  # Use 'r' mode to read

# print(ds.variables.keys())


# longitude = ds.variables['longitude'][:]
# latitude = ds.variables['latitude'][:]
# time = ds.variables['time'][:]
# t2m = ds.variables['t2m'][:]
# tp = ds.variables['tp'][:]
# swvl1 = ds.variables['swvl1'][:]
# swvl2 = ds.variables['swvl2'][:]
# swvl3 = ds.variables['swvl3'][:]

# # Calculate the water variable
# rzsm = swvl1 * 0.07 + swvl2 * 0.21 + swvl3 * 0.82

# # Close the original dataset
# ds.close()

# # Create a new NetCDF file
# new_file_path = "C:\\Users\\zhijiel\\Downloads\\ERA5data_original\\new_file.nc"
# new_ds = nc.Dataset(new_file_path, 'w', format='NETCDF4')

# # Create dimensions
# lon_dim = new_ds.createDimension('longitude', len(longitude))
# lat_dim = new_ds.createDimension('latitude', len(latitude))
# time_dim = new_ds.createDimension('time', len(time))

# # Create variables for dimensions and assign the data

# lon_var = new_ds.createVariable('longitude', np.float32, ('longitude',))
# lat_var = new_ds.createVariable('latitude', np.float32, ('latitude',))
# time_var = new_ds.createVariable('time', np.float32, ('time',))
# time_var[:] = time
# lat_var[:] = latitude
# lon_var[:] = longitude

# # Create the other variables
# t2m_var = new_ds.createVariable('t2m', np.float32, ('time', 'latitude', 'longitude'))
# tp_var = new_ds.createVariable('tp', np.float32, ('time', 'latitude', 'longitude'))
# swvl1_var = new_ds.createVariable('swl1', np.float32, ('time', 'latitude', 'longitude'))
# swvl2_var = new_ds.createVariable('swl2', np.float32, ('time', 'latitude', 'longitude'))
# swvl3_var = new_ds.createVariable('swl3', np.float32, ('time', 'latitude', 'longitude'))
# water_var = new_ds.createVariable('rzsm', np.float32, ('time', 'latitude', 'longitude'))

# # Assign the calculated data to the new variables
# t2m_var[:] = t2m
# tp_var[:] = tp
# swvl1_var[:] = swvl1
# swvl2_var[:] = swvl2
# swvl3_var[:] = swvl3
# water_var[:] = rzsm

# # Add attributes to the new variable if needed
# t2m_var.units = 'Celsius'
# t2m_var.long_name = '2m temperature'
# tp_var.units = 'm'
# tp_var.long_name = 'total precipitation'
# swvl1_var.units = 'm3/m3'
# swvl1_var.long_name = 'volumetric soil water layer 1'
# swvl2_var.units = 'm3/m3'
# swvl2_var.long_name = 'volumetric soil water layer 2'
# swvl3_var.units = 'm3/m3'
# swvl3_var.long_name = 'volumetric soil water layer 3'
# water_var.units = 'm3/m3'
# water_var.long_name = 'root zone soil moisture'

# print(new_ds.variables.keys())
# print(new_ds.variables['rzsm'].shape)


# # Close the new dataset to write the file
# new_ds.close()




#**********************************这是有循环的版本# from tqdm import tqdm
import os
import netCDF4 as nc
import numpy as np
from tqdm import tqdm


directory = "E:\\ERA5 data process\\ERA5data_original" # Specify the directory you want to process
output_directory = "E:\\ERA5 data process\\ERA5data_rzsm" # Specify the directory you want to save the new files


files = [f for f in os.listdir(directory) if f.endswith(".nc")] # Get a list of all files in the directory

# Loop over all files in the directory with a progress bar
for filename in tqdm(files):  # Add progress bar with tqdm
    file_path = os.path.join(directory, filename)

    # Open the NetCDF file
    ds = nc.Dataset(file_path)

    longitude = ds.variables['longitude'][:]
    latitude = ds.variables['latitude'][:]
    time = ds.variables['time'][:]
    t2m = ds.variables['t2m'][:]
    tp = ds.variables['tp'][:]
    swvl1 = ds.variables['swvl1'][:]
    swvl2 = ds.variables['swvl2'][:]
    swvl3 = ds.variables['swvl3'][:]

    # Calculate the water variable
    rzsm = swvl1 * 0.07 + swvl2 * 0.21 + swvl3 * 0.72

    # Close the original dataset
    ds.close()

    # Create a new NetCDF file
    new_file_path = os.path.join(output_directory, filename)
    new_ds = nc.Dataset(new_file_path, 'w', format='NETCDF4')

    # Create dimensions
    lon_dim = new_ds.createDimension('longitude', len(longitude))
    lat_dim = new_ds.createDimension('latitude', len(latitude))
    time_dim = new_ds.createDimension('time', len(time))

    # Create variables for dimensions and assign the data
    lon_var = new_ds.createVariable('longitude', np.float32, ('longitude',))
    lat_var = new_ds.createVariable('latitude', np.float32, ('latitude',))
    time_var = new_ds.createVariable('time', np.float32, ('time',))
    time_var[:] = time
    lat_var[:] = latitude
    lon_var[:] = longitude

    # Create the other variables
    t2m_var = new_ds.createVariable('t2m', np.float32, ('time', 'latitude', 'longitude'))
    tp_var = new_ds.createVariable('tp', np.float32, ('time', 'latitude', 'longitude'))
    swvl1_var = new_ds.createVariable('swvl1', np.float32, ('time', 'latitude', 'longitude'))
    swvl2_var = new_ds.createVariable('swvl2', np.float32, ('time', 'latitude', 'longitude'))
    swvl3_var = new_ds.createVariable('swvl3', np.float32, ('time', 'latitude', 'longitude'))
    rzsm_var = new_ds.createVariable('rzsm', np.float32, ('time', 'latitude', 'longitude'))

    # Assign the calculated data to the new variables
    t2m_var[:] = t2m
    tp_var[:] = tp
    swvl1_var[:] = swvl1
    swvl2_var[:] = swvl2
    swvl3_var[:] = swvl3
    rzsm_var[:] = rzsm

    # Add attributes to the new variable if needed
    t2m_var.units = 'Celsius'
    t2m_var.long_name = '2m temperature'
    tp_var.units = 'm'
    tp_var.long_name = 'total precipitation'
    swvl1_var.units = 'm3/m3'
    swvl1_var.long_name = 'volumetric soil water layer 1'
    swvl2_var.units = 'm3/m3'
    swvl2_var.long_name = 'volumetric soil water layer 2'
    swvl3_var.units = 'm3/m3'
    swvl3_var.long_name = 'volumetric soil water layer 3'
    rzsm_var.units = 'm3/m3'
    rzsm_var.long_name = 'root zone soil moisture'

    print(new_ds.variables.keys())
    print(new_ds.variables['rzsm'].shape)

    # Close the new dataset to write the file
    new_ds.close()







