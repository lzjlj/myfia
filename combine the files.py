

import pandas as pd
import os

input_folder = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\TREE_selected_treatment"
output_folder = "C:\\FIA-Data\\FIA_data\\USA_COND+PLOT+TREE\\TREE_selected_treatment"

# Create an empty DataFrame to store all data
all_data = pd.DataFrame()

for file in os.listdir(input_folder):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(input_folder, file))
        
        # Concatenate the current DataFrame with the overall DataFrame
        all_data = pd.concat([all_data, df])

# Save the concatenated DataFrame to a CSV file
all_data.to_csv(os.path.join(output_folder, '_TREE_selected_combined.csv'), index=False)


