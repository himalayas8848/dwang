#!/bin/env python
# Requires: youtube_dl module
# Requires: ffmpeg
# Usage:
#
# python youtube2mp3.py <URL>, ...
# 
# Example:
# cd to download folder
# python youtube2mp3.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

from pytube import YouTube
import sys

filename = 'https://youtu.be/Pb4jqUOhsc8'


if __name__ == "__main__":
    yt = YouTube(filename)
    stream=yt.streams.filter(only_audio=True).filter(file_extension='mp4').first()
    stream.download()