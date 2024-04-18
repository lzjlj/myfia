# myfia
this code is for my SEM

The project is for analyzing the netcdf file
the code including how to combine different elements by numpy.

the dim of the origin data is hourly every year 
then I reshape the dim of the origin data to daily (365*24). (day = hour/24).
I divided the data by 24 and then got the daily mean data. (longitude, latitude, time)

then I combine all npy, and np transpose the shape as (time, latitude, longitude) which is because need to keep the same dim with feiyang`s code

