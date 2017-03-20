#!/usr/bin/env python3

from moviepy.editor import *
from techmeme.config import TechnicalMemeConfig

config = TechnicalMemeConfig("tests/sample_config.txt")
source_clip = VideoFileClip("tests/WANO.mp4")
timestamps = [0] + config.timestamps + [source_clip.end]
subclips = [source_clip.subclip(*timestamps[i:i+2]) for i in range(len(timestamps) - 1)]

for exponent, subclip in enumerate(subclips):
	vfx.speedx(subclip, config.multiplier**exponent).write_videofile("tests/{}.mp4".format(exponent))

#memed = CompositeVideoClip(subclips)
#memed.write_videofile('tests/WANO but every time they say "one" it gets 5% faster.mp4')
