from moviepy.editor import *
import json
import os

dir_path = 'data'

for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        if file_path.endswith('_cut.mp4'):
            input_video='data/'+file_path
            break

clip = VideoFileClip(input_video)

# getting video fps rate

rate = clip.fps

# setting a parts [s]

video_cuts = [[12,16]]

# cutting a clip

for i,j in enumerate(video_cuts):
    start_frame,end_frame=j[0]*rate,j[1]*rate
    # setting clip name
    clip_name=f'cuts/{i:03d}.mp4'

    # setting a start and end time
    start_time=int(max(0,start_frame/rate-1))
    end_time=int(min(end_frame/rate+4,clip.duration))

    # saving clip
    clip_tmp=clip.subclip(start_time,end_time)
    clip_tmp.write_videofile(clip_name,codec='libx264')