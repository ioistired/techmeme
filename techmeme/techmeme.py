#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
techmeme.py: class that turns videos into dank technical may-mays
"""

from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.speedx import speedx

from .config import TechnicalMemeConfig


class TechnicalMeme(CompositeVideoClip):
	def __init__(self, *, source_filename, config_filename):
		self.source_video = VideoFileClip(source_filename)
		self.config = TechnicalMemeConfig(config_filename)
		self._fix_up_timestamps()
		
		# write em up
		self._write_all_subclips()
	
	
	def _fix_up_timestamps(self):
		self.config.timestamps = [0] + self.config.timestamps + [self.source_video.end]
	
	
	def _get_subclip(self, timestamp_number):
		"""get a subclip at the timestamp given by self.config.timestamps[timestamp_number]"""
		
		if timestamp_number < len(self.config.timestamps):
			return self.source_video.subclip(*self.config.timestamps[timestamp_number:timestamp_number+2])
		else:
			raise ValueError("timestamp number too large")
	
	
	def _get_sped_up_subclip(self, timestamp_number):
		try:
			return self._get_subclip(timestamp_number)\
				.speedx(self.config.multiplier**timestamp_number)
		except ValueError:
			raise
	
	
	def _write_subclip(self, timestamp_number):
		try:
			self._get_sped_up_subclip(timestamp_number)\
				.write_videofile("TMP_techmeme_{}.mp4"
					.format(timestamp_number))
		except ValueError:
			raise
	
	def _write_all_subclips(self):
		for timestamp_number in range(len(self.config.timestamps)):
			try:
				self._write_subclip(timestamp_number)
			except ValueError:
				raise
