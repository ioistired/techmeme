#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
config.py: Config objects store video 
"""


class Config:
	def __init__(self, video_filename, filename):
		self.video_filename = video_filename
		self.filename = filename
