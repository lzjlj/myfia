import numpy as np
import pandas as pd
from tqdm import tqdm

# read the npz file
data_path = "./bilinear_inter_data_feiyang/drought_data_combine_west.npz"
data = np.load(data_path)

flash_drought_data = data["flash_drought_data"]
slow_drought_data = data["slow_drought_data"]
position_set_data = data["position_set_data"]

print(flash_drought_data.shape, slow_drought_data.shape, position_set_data.shape)

year_start_index = 1981
# create a pd dataframe
#df = pd.DataFrame(columns=["year", "latitude", "longitude", "num_of_slow_drought", "mean_duration_slow_drought", "mean_severity_slow_drought", "mean_speed_slow_drought", "num_of_flash_drought", "mean_duration_flash_drought", "mean_severity_flash_drought", "mean_speed_flash_drought"])
rows = []
for idx, (flash_drought, slow_drought, position_set) in tqdm(enumerate(zip(flash_drought_data, slow_drought_data, position_set_data)), total=len(flash_drought_data)):
    latitude, longitude = position_set
    for year in range(40):
        num_of_flash_drought = flash_drought[year][0]
        mean_duration_flash_drought = flash_drought[year][1]
        mean_severity_flash_drought = flash_drought[year][2]
        mean_speed_flash_drought = flash_drought[year][3]
        num_of_slow_drought = slow_drought[year][0]
        mean_duration_slow_drought = slow_drought[year][1]
        mean_severity_slow_drought = slow_drought[year][2]
        mean_speed_slow_drought = slow_drought[year][3]
        real_year = year_start_index + year

        rows.append({"year": real_year, "latitude": latitude, "longitude": longitude, "num_of_slow_drought": num_of_slow_drought, "mean_duration_slow_drought": mean_duration_slow_drought, "mean_severity_slow_drought": mean_severity_slow_drought, "mean_speed_slow_drought": mean_speed_slow_drought, "num_of_flash_drought": num_of_flash_drought, "mean_duration_flash_drought": mean_duration_flash_drought, "mean_severity_flash_drought": mean_severity_flash_drought, "mean_speed_flash_drought": mean_speed_flash_drought})

df = pd.DataFrame(rows)
df.to_csv("drought_data_for_all_years.csv", index=False)