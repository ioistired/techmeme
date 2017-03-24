#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
tests/test_techmeme.py: Unit tests for TechnicalMeme class
"""

from shutil import rmtree # this and tempfile should be handled
import tempfile # by techmeme itself but not atm
import unittest

from moviepy.video.io.VideoFileClip import VideoFileClip
from techmeme import TechnicalMeme
from techmeme.config import TechnicalMemeConfig


class TechnicalMemeTests(unittest.TestCase):
	def setUp(self):
		# make a temp dir for storing the video parts
		self.tmpdir = tempfile.mkdtemp(prefix="techmeme")
		self.meme = TechnicalMeme("WANO.mp4", "sample_config.txt")
	
	def tearDown(self):
		rmtree(self.tmpdir)
	
	def test_attributes(self):
		self.assertIsInstance(self.meme.source_video, VideoFileClip)
		self.assertIsInstance(self.meme.config, TechnicalMemeConfig)
	
	def test_fix_up_timestamps(self):
		self.assertEqual(self.meme.config.timestamps[0], 0)
		self.assertEqual(self.meme.config.timestamps[-1], self.meme.source_video.end)
