#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
techmeme.py: CLI app to turn videos into dank technical may-mays
"""

import moviepy.video

from config import TechnicalMemeConfig


class TechnicalMeme(moviepy.video.VideoClip):
	def __init__(self, *, source_filename, config):
		self.source_filename = source_filename
		self.config = config
