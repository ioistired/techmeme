#!/usr/bin/env python3

from moviepy.editor import *
from techmeme.config import TechnicalMemeConfig
source_clip = VideoFileClip("tests/WANO.mp4")
timestamps = [0] + TechnicalMemeConfig("tests/sample_config.txt").timestamps + [source_clip.end]
subclips = [source_clip.subclip(*timestamps[i:i+2]) for i in range(len(timestamps) - 1)]
for exponent, subclip in enumerate(subclips):
	subclips[exponent] = vfx.speedx(subclip, 1.05**exponent)

for number, subclip in enumerate(subclips):
	subclip = subclip.without_audio()
	subclip = subclip.resize(480,360)
	subclip.write_videofile('tests/{}.mp4'.format(number))

#memed = CompositeVideoClip(subclips)
#memed.without_audio().resize(480,360).write_videofile('tests/WANO but every time they say "one" it gets 5% faster.mp4')
