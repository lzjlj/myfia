

import numpy as np
from netCDF4 import Dataset
import netCDF4 as nc

# Open the NetCDF file
file1 = "E:\\ERA5 data process\\daily_mean\\daymean_adaptor.mars.internal-2007.nc"
file2 = "E:\\ERA5 data process\\daily_mean\\daymean_adaptor.mars.internal-2008.nc"

# Open both files
data1 = nc.Dataset(file1, mode='r')
data2 = nc.Dataset(file2, mode='r')


print(data1.variables['t2m'].shape)

#print(data1.variables.keys())
#print(data1.variables['t2m'][:])
#print(data1.variables['rzsm'][:].max())

# Read the 'rzsm' variable from both files

# t2m1 = data1.variables['t2m'][:]
# t2m2 = data2.variables['t2m'][:]
# tp1 = data1.variables['tp'][:]
# tp2 = data2.variables['tp'][:]
# rzsm1 = data1.variables['rzsm'][:]
# rzsm2 = data2.variables['rzsm'][:]


# if (t2m1 == t2m2).all():
#     print("The 't2m' variable is identical in both files.")
# else:
#     print("The 't2m' variable differs in the files.")

# if (tp1 == tp2).all():
#     print("The 't2m' variable is identical in both files.")
# else:
#     print("The 't2m' variable differs in the files.")

# if (rzsm1 == rzsm2).all():
#     print("The 'rzsm' variable is identical in both files.")
# else:
#     print("The 'rzsm' variable differs in the files.")




