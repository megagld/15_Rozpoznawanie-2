import json
import os

def group(file_to_group):

    # getting data
    with open(file_to_group) as json_file:
        detected_frames = json.load(json_file)

    # setting frames max gap
    max_gap=15 # ~ 1sec with 30fps

    tmp=[]
    grouped_frames=[]
    for i,j in enumerate(detected_frames[:-1]):
        if detected_frames[i+1]-j<max_gap:
            tmp.append(j)
        else:
            if tmp:
                grouped_frames.append(tmp)
            tmp=[]
    if tmp:
        grouped_frames.append(tmp)

    # making a start and end cuts

    video_cuts=[(min(i),max(i)) for i in grouped_frames]

    # setting cuts to json

    with open('{}'.format(file_to_group.replace('detected_frames','video_cuts')), 'w') as f:
        json.dump(video_cuts, f)
    
    
for i,j,k in os.walk('data'):
    for l in k:
        if 'detected_frames' in l:
            group('{}\{}'.format(i,l))
