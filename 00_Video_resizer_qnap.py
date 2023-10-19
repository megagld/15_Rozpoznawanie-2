import moviepy.editor as mp
import os

dir_path = 'data'

for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        # add filename to list
        input_file=file_path
        # res.append(file_path)

clip = mp.VideoFileClip(dir_path+'/'+input_file)
clip_resized = clip.resize(height=384).without_audio() # make the height 360px and remove audio ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
clip_resized.write_videofile(f"data/{input_file}_resized.mp4".replace('.mp4_','_'))