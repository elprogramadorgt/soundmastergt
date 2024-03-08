import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


# Load the audio file
audio_file_path = 'output.mp3'
y, sr = librosa.load(audio_file_path, sr=None)

# Specify start and end times in seconds
start_time_sec = 0  # Adjust as needed
end_time_sec = 5   # Adjust as needed

# Convert times to sample indices
start_index = int(start_time_sec * sr)
end_index = int(end_time_sec * sr)

# Plot the specified portion of the array
plt.plot(np.linspace(start_time_sec, end_time_sec, end_index - start_index), y[start_index:end_index])
plt.title('Audio Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

# Find where the amplitude crosses zero
zero_crossings = np.where(np.diff(np.sign(y[start_index:end_index])))[0] + start_index

# Mark zero crossings on the plot
plt.scatter(zero_crossings / sr, y[zero_crossings], color='red', label='Zero Crossing')

plt.legend()

# Get the start and end times for the red line segments
start_times = time_axis[zero_crossings[:-1]]
end_times = time_axis[zero_crossings[1:]]

for i, (start, end) in enumerate(zip(start_times, end_times), 1):
    print(f"Segment {i}: Start Time = {start:.2f} seconds, End Time = {end:.2f} seconds")

plt.show()




# # Specify the target second
# target_second =35  # Replace with the specific second you're interested in

# # Convert the target second to a sample index
# target_index = int(target_second * sr)

# # Get the amplitude at the specified second
# amplitude_at_second = y[target_index]
# print(amplitude_at_second)


# # Plot the waveform
# plt.figure(figsize=(12, 6))
# librosa.display.waveshow(y, sr=sr, color='b')  # Specify color directly

# plt.title('Audio Waveform')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()