#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
config.py: Config objects store video 
"""


class TechnicalMemeConfig:
	def __init__(self, video_filename, filename):
		self.video_filename = video_filename
		self.filename = filename
		
		self.parse_config()
	
	def parse_config(self):
		with open(self.filename) as config_file:
			# get first line and save as speed multiplier
			self.multiplier = float(next(config_file).strip())
			self.timestamps = [float(line.strip()) for line in config_file]
