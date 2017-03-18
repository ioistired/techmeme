#!/usr/bin/env python3
# encoding: utf-8
# 
# © 2017 Benjamin Mintz
# https://bmintz.mit-license.org/@2017
#

"""
tests/config.py: Unit tests for config.py
"""

import unittest

from techmeme.config import TechnicalMemeConfig


class TechnicalMemeConfigTests(unittest.TestCase):
	def setUp(self):
		self.config = TechnicalMemeConfig('tests/sample_config.txt')
		
	def test_basic_attributes(self):
		"""test the attributes that don't need to be parsed first"""
		self.assertEqual(self.config.filename, 'tests/sample_config.txt')
	
	def test_parsed_attributes(self):
		"""test the attributes that do need to be parsed"""
		self.assertEqual(self.config.multiplier, 1.05)
		self.assertEqual(self.config.timestamps, [
			1.4142135623730951,
			3.141592653589793,
			5.0,
			26.3,
			69.420,
		])

if __name__ == '__main__':
	import sys
	sys.exit(unittest.main(verbosity=2))
