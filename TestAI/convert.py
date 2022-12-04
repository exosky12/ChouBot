from moviepy.editor import *

clip = VideoFileClip("video.mp4")
clip.audio.write_audiofile("audio.wav",codec='pcm_s16le')
