#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
techmeme.py: CLI app to turn videos into dank technical may-mays
"""

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.speedx import speedx

from config import TechnicalMemeConfig


class TechnicalMeme(CompositeVideoClip):
	def __init__(self, *, source_filename, config):
		self.source_video = VideoFileClip(source_filename)
		self.config = config
		self._fix_up_timestamps()
	
	def _fix_up_timestamps(self):
		self.config.timestamps = [0] + self.config.timestamps + [self.source_video.end]
	
	def _get_subclip(self, timestamp_number):
		"""get a subclip at the timestamp given by self.config.timestamps[timestamp_number]"""
		
		if timestamp_number < len(self.timestamps):
			return self.source_video.subclip(*self.timestamps[timestamp_number:timestamp_number+2])
		else:
			raise ValueError("timestamp number too large")
