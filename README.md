# MiniProject 2: Event-Related Potential (ERP) Analysis

## Project Description
This project analyzes brain signals (ECoG data) recorded during finger movements. The goal is to calculate the average Event-Related Potential (ERP) for each of the five fingers.

## Files
- `fingers_erp.py`: Contains the `calc_mean_erp()` function
- `main.py`: Main script that loads data and runs the analysis
- `events_file_ordered.csv`: Finger movement timing data (starting points, peaks, finger IDs)
- `brain_data_channel_one.csv`: ECoG brain signal data from one electrode


## Output
- **Matrix (5 x 1201)**: Average brain response for each finger
  - 5 rows: one per finger (1-5)
  - 1201 columns: time points from -200ms to +1000ms relative to movement start
- **Plots**: Visual representation of the ERP for each finger

## Author
Petra Reuwsaat Paul

## Course
MSc Brain Sciences - Data Science for Neuroscience