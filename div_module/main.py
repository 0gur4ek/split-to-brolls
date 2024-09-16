import os

import moviepy

from moviepy.video.io.VideoFileClip import VideoFileClip

def split_video(video_path : str, splits : tuple, output_path_template):
    """
    Splits a video into multiple parts.
    
    :param video_path:           Path to the input video file.
    :param splits:               A list of tuples (start_time, end_time) in seconds.
    :param output_path_template: Template for output file names.
    :return:                     File names of b-rolls.
    """
    with VideoFileClip(video_path) as video:
    
    # Loop over the list of start and end times
        for i, (start, end) in enumerate(splits):
        # Extract the subclip
            subclip = video.subclip(start, end)
        
        # Generate output file name
            output_file = output_path_template.format(i+1)
        
        # Write the subclip to a file
            subclip.write_videofile(
                output_file,
                codec="libx264",
                audio_codec="aac"
            )


if __name__ == '__main__':
    splits = [(0, 30), (30, 60), (60, 90)]  # Splitting into 30-second chunks
    output_path_template = "local/output_part{}.mp4"

    split_video("stock.mp4", splits, output_path_template)