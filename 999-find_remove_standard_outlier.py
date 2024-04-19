


##这是对tree的计算，通过除以2将生物量转换为碳

# import pandas as pd

# # Load the data
# df = pd.read_csv("C:\\FIA-Data\\FIA_data\\tree\\1_TREE_selected_all_USA_drought_bilinear_interpolation_combine.csv")

# # List of columns to divide by 2
# columns = ['DRYBIO_BOLE', 'DRYBIO_TOP', 'DRYBIO_STUMP', 'DRYBIO_SAPLING', 'DRYBIO_WDLD_SPP', 'DRYBIO_AG']

# # Divide each column by 2 and save the result in a new column
# for col in columns:
#     df[col+'_div2'] = df[col] / 2

# # Rename the 'CN_x' column to 'CN'
# df = df.rename(columns={'CN_x': 'CN'})

# # Drop the 'CN_y' column
# df = df.drop(columns=['CN_y'])

# # Write the DataFrame back to CSV
# df.to_csv("C:\\FIA-Data\\FIA_data\\tree\\1_TREE_selected_all_USA_drought_bilinear_interpolation_combine_convert_biomass_to_carbon.csv", index=False)



#针对tree进行异常值筛选的数据 columns = ['CARBON_AG','CARBON_BG','DRYBIO_BOLE_div2','DRYBIO_TOP_div2','DRYBIO_STUMP_div2','DRYBIO_SAPLING_div2','DRYBIO_WDLD_SPP_div2','DRYBIO_AG_div2']

#针对cond进行异常值筛选的数据 columns = ['CARBON_DOWN_DEAD', 'CARBON_LITTER', 'CARBON_SOIL_ORG', 'CARBON_STANDING_DEAD', 'CARBON_UNDERSTORY_AG', 'CARBON_UNDERSTORY_BG']

# ************************************************************************************************************************************************************


# import pandas as pd
# import numpy as np

# # Load the CSV file into a DataFrame
# file_path = "C:\\FIA-Data\\FIA_data\\tree\\1_TREE_selected_all_USA_drought_bilinear_interpolation_combine_convert_biomass_to_carbon.csv" # Replace with the path to your CSV file
# df = pd.read_csv(file_path)
# df_new = df.copy()
# columns = ['CARBON_AG','CARBON_BG','DRYBIO_BOLE_div2','DRYBIO_TOP_div2','DRYBIO_STUMP_div2','DRYBIO_SAPLING_div2','DRYBIO_WDLD_SPP_div2','DRYBIO_AG_div2']

# detect outliers and remove for normalized distribution
# for i in columns:
#     mean = df_new[i].mean()
#     std = df_new[i].std()
#     print(f"For column {i}, Mean: {mean}, Std: {std}")
#     lower_limit = mean - 3*std # 3 is the threshold
#     upper_limit = mean + 3*std
#     print(f"Lower limit: {lower_limit}, Upper limit: {upper_limit}")
#     outliers = df_new[(df_new[i] < lower_limit) | (df_new[i] > upper_limit)]
#     print(outliers)
#     new_df = df_new.drop(outliers.index)    
# new_df.to_csv("C:\\FIA-Data\\FIA_data\\1_COND_selected_all_USA_drought_bilinear_interpolation_combine_new_delete_blank_1981_2020_no_outliers (for normalized distribution).csv", index=False)


# detect outliers and remove for non-normalized distribution
# for j in columns:
#     q1 = df_new[j].quantile(0.25)
#     q3 = df_new[j].quantile(0.75)
#     iqr = q3 - q1
#     print(iqr)
#     lower_limit = q1 - 1.5*iqr
#     upper_limit = q3 + 1.5*iqr
#     print(f"Lower limit: {lower_limit}, Upper limit: {upper_limit}")
#     outliers = df_new[(df_new[j] < lower_limit) | (df_new[j] > upper_limit)]
#     print(outliers)
#     new_df = df_new.drop(outliers.index)
# new_df.to_csv("C:\\FIA-Data\\FIA_data\\tree\\1_TREE_selected_all_USA_drought_bilinear_interpolation_combine_convert_biomass_to_carbon (for non-normalized distribution)_outlier.csv", index=False)

# ************************************************************************************************************************************************************

# data standardization by z-score  dont necessary
# import pandas as pd
# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt

# # Load the CSV file into a DataFrame
# file_path = "C:\\FIA-Data\\FIA_data\\1_COND_selected_all_USA_drought_bilinear_interpolation_combine_new_delete_blank_1981_2020_no_outliers (for non-normalized distribution).csv"
# df = pd.read_csv(file_path)

# df_new = df.copy()

# columns = [
#     'CARBON_DOWN_DEAD', 'CARBON_LITTER', 'CARBON_SOIL_ORG', 'CARBON_STANDING_DEAD', 'CARBON_UNDERSTORY_AG', 'CARBON_UNDERSTORY_BG', 
#     'num_of_flash_drought', 'num_of_slow_drought', 'mean_duration_flash_drought', 'mean_duration_slow_drought', 
#     'mean_severity_flash_drought', 'mean_severity_slow_drought', 'mean_speed_flash_drought', 'mean_speed_slow_drought'
#     ]

# for k in columns:
#     df_new[k] = stats.zscore(df_new[k])        
# df_new.to_csv("C:\\FIA-Data\\FIA_data\\1_COND_selected_all_USA_drought_bilinear_interpolation_combine_new_delete_blank_1981_2020_no_outliers (for non-normalized distribution)_zscore.csv", index=False)

# ************************************************************************************************************************************************************

# data standardization by max-min

#import pandas as pd
#import numpy as np
#from scipy import stats
#import matplotlib.pyplot as plt
#import seaborn as sns


# Load the CSV file into a DataFrame
#file_path = "C:\\FIA-Data\\FIA_data\\tree\\1_TREE_selected_all_USA_drought_bilinear_interpolation_combine_convert_biomass_to_carbon (for non-normalized distribution)_outlier.csv"
#df = pd.read_csv(file_path)

#columns = [
#    'CARBON_AG','CARBON_BG','DRYBIO_BOLE_div2','DRYBIO_TOP_div2','DRYBIO_STUMP_div2','DRYBIO_SAPLING_div2','DRYBIO_WDLD_SPP_div2','DRYBIO_AG_div2',
#    'num_of_flash_drought', 'num_of_slow_drought', 'mean_duration_flash_drought', 'mean_duration_slow_drought', 
#    'mean_severity_flash_drought', 'mean_severity_slow_drought', 'mean_speed_flash_droughts', 'mean_speed_slow_droughts'
#   ]

#def normalize(df):
#    result = df.copy()
#    for feature_name in df.columns:
#        if feature_name in columns:
#            max_value = df[feature_name].max()
#            min_value = df[feature_name].min()
#            result[feature_name] = round(df[feature_name] - min_value) / (max_value - min_value)#roud to 6 decimal places 表示保持6位有效数字
#    return result
#df_new = normalize(df)

#df_new.to_csv("C:\\FIA-Data\\FIA_data\\tree\\1_TREE_selected_all_USA_drought_bilinear_interpolation_combine_convert_biomass_to_carbon (for non-normalized distribution)_outlier_max-min standrized.csv", index=False)
