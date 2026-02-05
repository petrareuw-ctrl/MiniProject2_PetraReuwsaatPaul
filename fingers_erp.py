import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calc_mean_erp(trial_points, ecog_data):
    # Convert DataFrame to array - easier for indexing
    # Struggled with this at first but realized I need just the values
    ecog_array = ecog_data[0].values
    
    # Create structure to store trials by finger
    # Using dictionary because each finger has different number of trials
    trials_by_finger = {1: [], 2: [], 3: [], 4: [], 5: []}
    
    # Go through each movement and extract brain window
    for index, row in trial_points.iterrows():
        starting = row['starting_point']
        finger = row['finger']
        
        # Calculate window: 200ms before, 1ms at start, 1000ms after. Total 1201 points
        start_window = starting - 200
        end_window = starting + 1000
        
        # Extract brain data for this time window
        brain_window = ecog_array[start_window:end_window+1]
       
        trials_by_finger[finger].append(brain_window)
    
    # Initialize matrix to store final ERPs
    # 5 rows (fingers) x 1201 columns (time points)
    fingers_erp_mean = np.zeros((5, 1201))
    
    # Calculate average for each finger
    for finger in range(1, 6):
        # Convert list of arrays to 2D array
        # Shape (n_trials, 1201)
        trials_array = np.array(trials_by_finger[finger])
        
        # Average across trials
        mean_signal = np.mean(trials_array, axis=0)
        
        # Store in matrix 
        fingers_erp_mean[finger-1, :] = mean_signal
    
    # Plot the ERPs
    time_axis = np.arange(-200, 1001)
    
    plt.figure(figsize=(10, 12))
    
    # Create subplot for each finger
    for i in range(5):
        plt.subplot(5, 1, i+1)
        plt.plot(time_axis, fingers_erp_mean[i, :])
        
        # Red line at t=0 (movement start)
        plt.axvline(0, color='red', linestyle='--', alpha=0.5)
        
        plt.xlabel('Time (ms)')
        plt.ylabel('Brain Signal')
        plt.title(f'Finger {i+1} ERP')
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return fingers_erp_mean