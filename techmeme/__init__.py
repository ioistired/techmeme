#!/usr/bin/env python3
# encoding: utf-8
#
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
techmeme: class that turns videos into dank technical may-mays
"""

import os
from subprocess import Popen

from moviepy.video.io.VideoFileClip import VideoFileClip as _VideoFileClip
from moviepy.video.fx.speedx import speedx as _speedx

from .config import TechnicalMemeConfig as _TechnicalMemeConfig


class TechnicalMeme:
	
	_FFMPEG_CONCAT_LIST_FILENAME = 'TMP_techmeme_concat_list.txt'
	
	def __init__(self, config_filename):
		self.config = _TechnicalMemeConfig(config_filename)
		self.source_video = _VideoFileClip(self.config.source_filename)
		self._fix_up_timestamps()
	
	
	def _fix_up_timestamps(self):
		self.config.timestamps = [0] + self.config.timestamps + [self.source_video.end]
	
	
	def _get_subclip(self, timestamp_number):
		"""get a subclip at the timestamp given by self.config.timestamps[timestamp_number]"""
		
		if 0 <= timestamp_number < len(self.config.timestamps):
			return self.source_video.subclip(*self.config.timestamps[timestamp_number:timestamp_number+2])
		else:
			raise IndexError("timestamp number out of range")
	
	
	def _get_sped_up_subclip(self, timestamp_number):
		try:
			return self._get_subclip(timestamp_number)\
				.fx(_speedx, self.config.multiplier**timestamp_number)
		except:
			raise
	
	
	def _write_subclip(self, timestamp_number):
		try:
			self._get_sped_up_subclip(timestamp_number)\
				.write_videofile("TMP_techmeme_{}.mp4"
					.format(timestamp_number))
		except IndexError:
			raise
		# moviepy is buggy and often returns index errors (raised as OSErrors)
		# when trying to save the last clip
		except OSError as ex:
			print(ex)
	
	
	def _write_all_subclips(self):
		for timestamp_number in range(len(self.config.timestamps)):
			
			print("{}...".format(timestamp_number), end=" ")
			
			try:
				self._write_subclip(timestamp_number)
			except IndexError:
				print("failed!")
				raise
			else:
				print("done.")
	
	
	def save(self, output_name):
	
		try:
			self._write_all_subclips()
			self._write_ffmpeg_concat_config()
			self._concat_clips(output_name)
		except:
			raise
	
	
	def _write_ffmpeg_concat_config(self):
		ffmpeg_config = open(self._FFMPEG_CONCAT_LIST_FILENAME, 'w')
		
		for i in range(len(self.config.timestamps)):
			filename = './TMP_techmeme_{}.mp4'.format(i)
			
			# if there was an error saving the video
			# (again, usually the last one)
			# so only build the concat list out of existing files
			try:
				with open(filename): # don't care about the file itself, only if it exists
					ffmpeg_config.write("file '{}'\n".format(filename))
			except OSError:
				pass
		
		ffmpeg_config.close()
	
	
	def _concat_clips(self, output_name):
		Popen(['ffmpeg',
				'-safe',
				'0',
				'-f',
				'concat',
				'-i',
				self._FFMPEG_CONCAT_LIST_FILENAME,
				'-c',
				'copy',
				output_name])