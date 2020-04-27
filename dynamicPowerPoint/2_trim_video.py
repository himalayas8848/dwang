#!/bin/env python
# Requires: ffmpeg
# Usage:
#

import os
import subprocess

name = r'.\videos\video_tuan.mp4'

times = []
times.append(["00:00:02", "00:00:8"])

open('concatenate.txt', 'w').close()
for idx, time in enumerate(times):
    output_filename = f"output{idx}.mp4"
    cmd = ["ffmpeg", "-i", name, "-ss", time[0], "-to", time[1], "-c:v", "copy", "-c:a", "copy", output_filename]
    subprocess.check_output(cmd)
    with open("concatenate.txt", "a") as myfile:
        myfile.write(f"file {output_filename}\n")

cmd = ["ffmpeg", "-f", "concat", "-i", "concatenate.txt", "-c", "copy", "final.mp4"]
output = subprocess.check_output(cmd).decode("utf-8").strip()
os.remove("concatenate.txt")
os.remove(output_filename)