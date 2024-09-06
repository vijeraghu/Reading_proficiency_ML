import pandas as pd

def keep_selected_columns(file_path, column_names):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Keep only the specified columns
    df = df[column_names]

    # Save the modified CSV file
    df.to_csv(file_path, index=False)
    print("Data deleted successfully.")

# Example usage: Keep only the specified columns
keep_selected_columns(r"C:\Users\vijet\Downloads\Real_world\real_world_test.csv", [
    "File Name", "Expression and Volume", "Phrasing and Intonation", 
    "Smoothness", "Pace", "MFCC_1_1", "MFCC_2_1", "MFCC_3_1", "MFCC_4_1",
    "MFCC_5_1", "MFCC_6_1", "MFCC_7_1", "MFCC_8_1", "MFCC_9_1", "MFCC_10_1",
    "MFCC_11_1", "MFCC_12_1", "MFCC_13_1", "MFCC_14_1", "MFCC_15_1", "MFCC_16_1",
    "MFCC_17_1", "MFCC_18_1", "MFCC_19_1", "MFCC_20_1", "Pitch_mean_1", "Pitch_std_1",
    "MFCC_1_2", "MFCC_2_2", "MFCC_3_2", "MFCC_4_2", "MFCC_5_2", "MFCC_6_2", "MFCC_7_2",
    "MFCC_8_2", "MFCC_9_2", "MFCC_10_2", "MFCC_11_2", "MFCC_12_2", "MFCC_13_2", "MFCC_14_2",
    "MFCC_15_2", "MFCC_16_2", "MFCC_17_2", "MFCC_18_2", "MFCC_19_2", "MFCC_20_2", "Pitch_mean_2",
    "Pitch_std_2", "MFCC_1_3", "MFCC_2_3", "MFCC_3_3", "MFCC_4_3", "MFCC_5_3", "MFCC_6_3", "MFCC_7_3",
    "MFCC_8_3", "MFCC_9_3", "MFCC_10_3", "MFCC_11_3", "MFCC_12_3", "MFCC_13_3", "MFCC_14_3", "MFCC_15_3",
    "MFCC_16_3", "MFCC_17_3", "MFCC_18_3", "MFCC_19_3", "MFCC_20_3", "Pitch_mean_3", "Pitch_std_3",
    "MFCC_1_4", "MFCC_2_4", "MFCC_3_4", "MFCC_4_4", "MFCC_5_4", "MFCC_6_4", "MFCC_7_4", "MFCC_8_4",
    "MFCC_9_4", "MFCC_10_4", "MFCC_11_4", "MFCC_12_4", "MFCC_13_4", "MFCC_14_4", "MFCC_15_4", "MFCC_16_4",
    "MFCC_17_4", "MFCC_18_4", "MFCC_19_4", "MFCC_20_4", "Pitch_mean_4", "Pitch_std_4", "MFCC_1_5", "MFCC_2_5",
    "MFCC_3_5", "MFCC_4_5", "MFCC_5_5", "MFCC_6_5", "MFCC_7_5", "MFCC_8_5", "MFCC_9_5", "MFCC_10_5", "MFCC_11_5",
    "MFCC_12_5", "MFCC_13_5", "MFCC_14_5", "MFCC_15_5", "MFCC_16_5", "MFCC_17_5", "MFCC_18_5", "MFCC_19_5", "MFCC_20_5",
    "Pitch_mean_5", "Pitch_std_5", "MFCC_1_6", "MFCC_2_6", "MFCC_3_6", "MFCC_4_6", "MFCC_5_6", "MFCC_6_6", "MFCC_7_6",
    "MFCC_8_6", "MFCC_9_6", "MFCC_10_6", "MFCC_11_6", "MFCC_12_6", "MFCC_13_6", "MFCC_14_6", "MFCC_15_6", "MFCC_16_6",
    "MFCC_17_6", "MFCC_18_6", "MFCC_19_6", "MFCC_20_6", "Pitch_mean_6", "Pitch_std_6", "MFCC_1_7", "MFCC_2_7", "MFCC_3_7",
    "MFCC_4_7", "MFCC_5_7", "MFCC_6_7", "MFCC_7_7", "MFCC_8_7", "MFCC_9_7", "MFCC_10_7", "MFCC_11_7", "MFCC_12_7", "MFCC_13_7",
    "MFCC_14_7", "MFCC_15_7", "MFCC_16_7", "MFCC_17_7", "MFCC_18_7", "MFCC_19_7", "MFCC_20_7", "Pitch_mean_7", "Pitch_std_7",
    "MFCC_1_8", "MFCC_2_8", "MFCC_3_8", "MFCC_4_8", "MFCC_5_8", "MFCC_6_8", "MFCC_7_8", "MFCC_8_8", "MFCC_9_8", "MFCC_10_8",
    "MFCC_11_8", "MFCC_12_8", "MFCC_13_8", "MFCC_14_8", "MFCC_15_8", "MFCC_16_8", "MFCC_17_8", "MFCC_18_8", "MFCC_19_8", "MFCC_20_8",
    "Pitch_mean_8", "Pitch_std_8", "MFCC_1_9", "MFCC_2_9", "MFCC_3_9", "MFCC_4_9", "MFCC_5_9", "MFCC_6_9", "MFCC_7_9", "MFCC_8_9",
    "MFCC_9_9", "MFCC_10_9", "MFCC_11_9", "MFCC_12_9", "MFCC_13_9", "MFCC_14_9", "MFCC_15_9", "MFCC_16_9", "MFCC_17_9", "MFCC_18_9",
    "MFCC_19_9", "MFCC_20_9", "Pitch_mean_9", "Pitch_std_9"
])
