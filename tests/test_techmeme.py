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

from techmeme import TechnicalMeme


class TechnicalMemeTests(unittest.TestCase):
	def setUp(self):
		# make a temp dir for storing the video parts
		self.tmpdir = tempfile.mkdtemp(prefix="techmeme")
		self.meme = TechnicalMeme("WANO.mp4", "sample_config.txt")
		
	def tearDown(self):
		rmtree(self.tmpdir)
