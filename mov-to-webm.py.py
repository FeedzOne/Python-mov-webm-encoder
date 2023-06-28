import os
import subprocess

sourcedir = "your source directory"
outputdir = "your output directory"
video_enc = "libvpx-vp9"

if len(os.listdir(sourcedir) ) == 0:
    print("Directory is empty")
else:
    for file in os.listdir(sourcedir):
        name = file[:file.rfind(".")]
        list_of_commands = [
            "ffmpeg", "-i", 
            sourcedir+"/"+name+".mov", 
            "-lossless", "1", 
            "-c:v", video_enc,
            "-preset", "veryfast",
            "-r", "60",  
            "-auto-alt-ref", "0", 
            outputdir+"/"+name+".webm"
        ]
        subprocess.run(list_of_commands)
        print("\n\nDONE:"+name+"\n\n")
    print("\n\n\nALL DONE\n\n\n")