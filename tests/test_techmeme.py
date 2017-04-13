#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
tests/test_techmeme.py: Unit tests for TechnicalMeme class
"""

# tmp (directory|file) removal should be handled
# by techmeme itself but not atm
from shutil import rmtree 
import os
import tempfile
from glob import glob

import unittest

from moviepy.video.io.VideoFileClip import VideoFileClip
from techmeme import TechnicalMeme
from techmeme.config import TechnicalMemeConfig


class TechnicalMemeTests(unittest.TestCase):
	def setUp(self):
		# make a temp dir for storing the video parts
		self.tmpdir = tempfile.mkdtemp(prefix="techmeme", dir="tests")
		self.meme = TechnicalMeme("tests/sample_config.txt")
		
	def tearDown(self):
		rmtree(self.tmpdir)
		for tmpfile in glob("TMP_techmeme*"):
		
			try:
				os.remove(tmpfile)
			except:
				pass
	
	def test_attributes(self):
		self.assertIsInstance(self.meme.source_video, VideoFileClip)
		self.assertIsInstance(self.meme.config, TechnicalMemeConfig)
	
	def test_fix_up_timestamps(self):
		self.assertEqual(self.meme.config.timestamps[0], 0)
		self.assertEqual(self.meme.config.timestamps[-1], self.meme.source_video.end)
	
	def test_get_subclip(self):
		# get the clip that goes from the 3rd "one" to the 4th "one"
		# even though array indexes start at 0, subclips[3] is still the third
		# "one" because the first timestamp is 0 and so the first subclip contains
		# no "one"s
		subclip_3 = self.meme._get_subclip(3)
		self.assertIsInstance(subclip_3, VideoFileClip)
		
		# the third subclip should have length timestamps[4] - timestamps[3]
		self.assertEqual(subclip_3.end, 77.91304 - 56.91304)
		
		with self.assertRaises(IndexError, msg="timestamp number out of range"):
			self.meme._get_subclip(-1)
			self.meme._get_subclip(12)
	
	def test_get_sped_up_subclip(self):
		# we'll be using the sped up subclip for comparison
		# so save the subclip object for later
		sped_up_subclip_3 = self.meme._get_sped_up_subclip(3)
		self.assertIsInstance(sped_up_subclip_3, VideoFileClip)
		
		# speedup is 1.05 so each clip is progressively 0.95× slower
		# also floats aren't too accurate, so as long as the clip is about right
		# it's cool
		self.assertAlmostEqual(sped_up_subclip_3.end,
				(77.91304 - 56.91304) * 0.95**3,
				delta=0.2,
		)
	
	def test_write_subclip(self):
		sped_up_subclip_6 = self.meme._get_sped_up_subclip(6)
		
		self.meme._write_subclip(6)
		self.assertAlmostEqual(
				VideoFileClip("TMP_techmeme_6.mp4").end,
				sped_up_subclip_6.end,
				delta=0.2,
		)
	
	def test_write_all_subclips(self):
		"""
		test that the code can properly write *every* single subclip.
		this can take a while...
		"""
		
		self.meme._write_all_subclips()
		# make sure 14 mp4 files were written
		self.assertEqual(len(glob("TMP_techmeme*.mp4")), 13)
