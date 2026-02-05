import pandas as pd
from fingers_erp import calc_mean_erp

# Load the data files
# Make sure to specify int dtype as required
trial_points = pd.read_csv('events_file_ordered.csv', 
                           dtype={'starting_point': int, 
                                  'peak_point': int, 
                                  'finger': int})

ecog_data = pd.read_csv('brain_data_channel_one.csv', header=None)

# Run the function
fingers_erp_mean = calc_mean_erp(trial_points, ecog_data)

# Show the output matrix
print("ERP matrix shape:", fingers_erp_mean.shape)
print("\nFirst 5 time points for each finger:")
print(fingers_erp_mean[:, :5])