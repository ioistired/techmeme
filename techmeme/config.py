#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
config.py: Config objects store video 
"""

import os.path


class TechnicalMemeConfig:
	def __init__(self, filename):
		self.filename = filename
		self.parse_config()
	
	def parse_config(self):
		with open(self.filename) as config_file:
			# since video filenames are relative to the config file,
			# rather than the current directory of the script, 
			# but video filenames are specified relative to the config file,
			# we need to get the absolute path to the config file.
			config_dir = os.path.dirname(os.path.abspath(self.filename))
			
			# get first line and save as absolute video filename
			"""absolute path to the source video material"""
			self.source_filename = os.path.join(config_dir, next(config_file).strip())
			
			# get next line and save as speed multiplier
			"""how much to increase(>1)/decrease(<1) the speed of the source at every timestamp"""
			self.multiplier = float(next(config_file).strip())
			"""list of timestamps where the video should speed up"""
			self.timestamps = [float(line.strip()) for line in config_file]
			
			# if the timestamps are not in order,
			# the speedups will be applied in the wrong order
			self.timestamps.sort()
