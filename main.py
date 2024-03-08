import ffmpeg


def trim_video(input_file, output_file, start_time, end_time):
    (
        ffmpeg.input(input_file, ss=start_time,to=end_time)
        .output(output_file)
        .run()
    )
input_file = 'testvideo.mp4'
output_file = 'output.mp4'
start_time = '00:28:00'  # Replace with your desired start time
end_time = '00:30:30'    # Replace with your desired end time

trim_video(input_file, output_file, start_time, end_time)