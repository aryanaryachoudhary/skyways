import pandas as pd
import pyulog

def parse_log(file_name, threshold):
    # Load the log file
    ulog = pyulog.ULog(file_name)

    # Convert to pandas DataFrame
    data = ulog.data_list_to_df()

    # Filter for high vibration instances
    high_vibes = data[(data['vibe_x'] > threshold) | (data['vibe_y'] > threshold) | (data['vibe_z'] > threshold)]

    # Write to CSV
    high_vibes.to_csv('high_vibes.csv', columns=['timestamp', 'vibe_x', 'vibe_y', 'vibe_z'], index=False)

# Call the function with your log file and threshold
parse_log('skyways_swe.BIN', 35)
