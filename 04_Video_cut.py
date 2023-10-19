from moviepy.editor import *
import json
import os

def cut_vid(file,path,cuts_file_name):

    # dir_path = 'data'

    # for file_path in os.listdir(dir_path):
    #     # check if current file_path is a file
    #     if os.path.isfile(os.path.join(dir_path, file_path)):
    #         # add filename to list
    #         if file_path.endswith('.mp4') and 'video_cuts_{}'.format(file_path.replace('.mp4','.json')) in dir_path:
    #             input_video='data/'+file_path
    #         # res.append(file_path)

    clip = VideoFileClip(f'{path}\{file}')

    # getting data

    with open(f'{path}\{cuts_file_name}') as json_file:
        video_cuts = json.load(json_file)

    # getting video fps rate

    rate = 15 #clip.fps - tests todo

    # setting minimum clip time

    min_clip_time=0.1

    # cutting a clip

    for i,j in enumerate(video_cuts):
        start_frame,end_frame=j[0],j[1]
        #    checking minimum lenght
        if (end_frame-start_frame)/rate<min_clip_time:
            clip_name='cuts/_tmp/{}_{:03d}.mp4'.format(file.replace('.mp4',''),i)        
        else:
            # setting clip name
            clip_name='cuts/{}_{:03d}.mp4'.format(file.replace('.mp4',''),i)

        # setting a start and end time
        start_time=max(0,start_frame/rate-1)
        end_time=min(end_frame/rate+2,clip.duration)

        # saving clip
        clip_tmp=clip.subclip(start_time,end_time)
        clip_tmp.write_videofile(clip_name,codec='libx264')


for i,j,k in os.walk('data'):
    for l in k:
        cuts_file_name=l.replace('.mp4','_video_cuts.json')
        if all( (l.endswith('.mp4'), not l.endswith('resized.mp4') , cuts_file_name in k)):
            cut_vid(l,i,cuts_file_name)