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

from config import TechnicalMemeConfig


class TechnicalMeme(CompositeVideoClip):
	def __init__(self, *, source_filename, config):
		self.source_filename = source_filename
		self.config = config
