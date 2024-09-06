import os
import librosa
import pandas as pd
import numpy as np
import parselmouth

def extract_features(X, sample_rate):
    mfccs_list = []
    pitch_means = []
    pitch_stds = []
    
    for i in range(0, len(X), sample_rate):  # step size for 1-second segments
        end_i = min(i + sample_rate, len(X))
        segment_mfccs = librosa.feature.mfcc(y=X[i:end_i], sr=sample_rate, n_mfcc=20)
        mfccs_list.append(segment_mfccs.mean(axis=1))
        
        # Extract pitch using Parselmouth for each second
        segment_sound = parselmouth.Sound(X[i:end_i], sampling_frequency=sample_rate)
        segment_pitch = segment_sound.to_pitch()
        segment_pitch_values = segment_pitch.selected_array['frequency']
        pitch_means.append(np.mean(segment_pitch_values[segment_pitch_values != 0]) if segment_pitch_values.any() else 0)
        pitch_stds.append(np.std(segment_pitch_values[segment_pitch_values != 0]) if segment_pitch_values.any() else 0)

    return np.array(mfccs_list).T, pitch_means, pitch_stds

def feature_extraction(file_path):
    try:
        X, sample_rate = librosa.load(file_path, sr=None)
        if X.ndim > 1:
            X = X[:, 0]  # Mono channel

        mfccs, pitch_means, pitch_stds = extract_features(X, sample_rate)
        
        # Flatten all the feature arrays to store in a single row
        mfccs_flat = mfccs.flatten()
        pitch_means_flat = np.array(pitch_means).flatten()
        pitch_stds_flat = np.array(pitch_stds).flatten()

        return mfccs_flat, pitch_means_flat, pitch_stds_flat
    except Exception as e:
        print("[Error] There was an error in feature extraction:", e)
        return None, None, None

def create_dataframe(root_folder):
    data = []
    combined_excel_file = os.path.join(root_folder, "real1.xlsx")
    df_excel = pd.read_excel(combined_excel_file, engine='openpyxl')

    for index, row in df_excel.iterrows():
        file_name_with_ext = row['File name']
        file_name = os.path.splitext(file_name_with_ext)[0] + ".wav"
        audio_file_path = os.path.join(root_folder, file_name)

        try:
            if os.path.exists(audio_file_path):
                sampling_rate, duration = load_audio_info(audio_file_path)
                mfccs_flat, pitch_means_flat, pitch_stds_flat = feature_extraction(audio_file_path)

                if mfccs_flat is not None:
                    features_data = {}
                    num_seconds = len(mfccs_flat) // 20  # assuming 20 MFCCs per second

                    for sec in range(num_seconds):
                        for mfcc_index in range(20):  # 20 MFCCs
                            features_data[f'MFCC_{mfcc_index+1}_{sec+1}'] = mfccs_flat[sec*20 + mfcc_index]
                        features_data[f'Pitch_mean_{sec+1}'] = pitch_means_flat[sec]
                        features_data[f'Pitch_std_{sec+1}'] = pitch_stds_flat[sec]

                    data.append({
                        'File Name': file_name_with_ext,
                        'Expression and Volume': row['Expression and Volume'],
                        'Phrasing and Intonation': row['Phrasing and Intonation'],
                        'Smoothness': row['Smoothness'],
                        'Pace': row['Pace'],
                        **features_data
                    })
        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

    return pd.DataFrame(data)

def load_audio_info(audio_file_path):
    x, sampling_rate = librosa.load(audio_file_path, sr=None)
    duration = librosa.get_duration(y=x, sr=sampling_rate)
    return sampling_rate, duration

# Define the root folder
root_folder = r'C:\Users\vijet\Downloads\Real_world'

# Create the dataframe
df = create_dataframe(root_folder)

# Save dataframe to CSV
df.to_csv(os.path.join(root_folder, "real_world_test.csv"), index=False)

print("Feature extraction completed and saved to real_world_test.csv")
