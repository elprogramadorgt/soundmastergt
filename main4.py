#!/usr/bin/env python

import sys
import subprocess
import os
import shutil
from moviepy.editor import VideoFileClip, concatenate_videoclips
# Read WAV and MP3 files to array
from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
import plotly
import IPython

# Fix-sized segmentation (breaks a signal into non-overlapping segments)
fs, signal = wavfile.read("data/out.wav")
signal = signal / (2**15)
signal_len = len(signal)
segment_size_t = 1 # segment size in seconds
segment_size = segment_size_t * fs  # segment size in samples

# Break signal into list of segments in a single-line Python code
segments = np.array([signal[x:x + segment_size] for x in np.arange(0, signal_len - segment_size + 1, segment_size)])

# Save each segment in a separate filename
# for iS, s in enumerate(segments):
#     wavfile.write("data/out_{0:d}_{1:d}.wav".format(segment_size_t * iS,
#                                                               segment_size_t * (iS + 1)), fs, (s))

# Remove pauses using an energy threshold = 50% of the median energy:
energies = [(s**2).sum() / len(s) for s in segments]
# (attention: integer overflow would occur without normalization here!)
thres = 0.5 * np.median(energies)
index_of_segments_to_keep = (np.where(energies > thres)[0])
# get segments that have energies higher than the threshold:
segments2 = segments[index_of_segments_to_keep]
# concatenate segments to signal:
new_signal = np.concatenate(segments2)

# Normalize the values in new_signal to the range [-1, 1]
new_signal_normalized = np.int16(new_signal * (32767 / np.max(np.abs(new_signal))))

# and write to file:
wavfile.write("data/out2.wav", fs, new_signal_normalized)

plotly.offline.iplot({ "data": [go.Scatter(y=energies, name="energy"),
                                go.Scatter(y=np.ones(len(energies)) * thres, 
                                           name="thres")]})
# play the initial and the generated files in the notebook:
IPython.display.display(IPython.display.Audio("data/out.wav"))
IPython.display.display(IPython.display.Audio("data/out2.wav"))
