import librosa
import matplotlib.pyplot as plt
import numpy as np

audio_file_path = 'output.mp3'
y, sr = librosa.load(audio_file_path, sr=None)

# Specify start and end times in seconds
start_time_sec = 0  # Adjust as needed
end_time_sec = 5    # Adjust as needed

# Convert times to sample indices
start_index = int(start_time_sec * sr)
end_index = int(end_time_sec * sr)

# Plot the specified portion of the array
time_axis = np.linspace(start_time_sec, end_time_sec, end_index - start_index)
plt.plot(time_axis, y[start_index:end_index])
plt.title('Audio Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')

# Find where the amplitude crosses zero
zero_crossings = np.where(np.diff(np.sign(y[start_index:end_index])))[0] + start_index

# Mark zero crossings on the plot
plt.legend()
# plt.scatter(zero_crossings / sr, y[zero_crossings], color='red', label='Zero Crossing', zorder=2)

plt.scatter(zero_crossings / sr, y[zero_crossings], color='red', label='Zero Crossing',zorder=2)


plt.show()

# Get the start and end times for the red line segments
start_times = time_axis[zero_crossings[:-1]]
end_times = time_axis[zero_crossings[1:]]

for i, (start, end) in enumerate(zip(start_times, end_times), 1):
    print(f"Segment {i}: Start Time = {start:.2f} seconds, End Time = {end:.2f} seconds")
