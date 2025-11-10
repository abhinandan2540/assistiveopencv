

# FRAME EXTRACTION FROM VIDEO FILES

import subprocess
import os

input_folder = 'videos'
output_folder = 'frames'
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith('.mp4'):
        video_path = os.path.join(input_folder, file)
        output_path = os.path.join(
            output_folder, file.replace('.mp4', '_%04d.jpg'))

        subprocess.run(['ffmpeg', '-i', video_path,
                       '-vf', 'fps=3', output_path])

print('DONE')

