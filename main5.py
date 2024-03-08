import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment

def remove_pauses(video_path, output_path):
    # Load the video file
    video_clip = VideoFileClip(video_path)

    # Extract audio from the video clip
    audio = video_clip.audio.to_soundarray()
    
    # Convert to mono if needed
    if len(audio.shape) > 1:
        audio = audio.mean(axis=1)

    # Fix-sized segmentation (breaks a signal into non-overlapping segments)
    fs = video_clip.audio.fps
    signal_len = len(audio)
    segment_size_t = 1  # segment size in seconds
    segment_size = int(segment_size_t * fs)  # segment size in samples

    # Break signal into list of segments
    segments = [audio[x:x + segment_size] for x in np.arange(0, signal_len - segment_size + 1, segment_size)]

    # Remove pauses using an energy threshold = 50% of the median energy:
    energies = [(s**2).sum() / len(s) for s in segments]
    thres = 0.5 * np.median(energies)
    index_of_segments_to_keep = (np.where(energies > thres)[0])
    segments2 = [segments[i] for i in index_of_segments_to_keep]
    new_signal = np.concatenate(segments2)

    # Normalize the values in new_signal to the range [-1, 1]
    new_signal_normalized = np.int16(new_signal * (32767 / np.max(np.abs(new_signal))))

    # Create a new AudioSegment with the processed audio
    processed_audio = AudioSegment(data=new_signal_normalized.tobytes(), sample_width=2, frame_rate=fs, channels=1)

    # Set the processed audio to the video clip
    video_clip = video_clip.set_audio(processed_audio)

    # Write the video with modified audio to an MP4 file
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

video_path = "data/output.mp4"
output_path = "data/file_processed.mp4"

remove_pauses(video_path, output_path)
