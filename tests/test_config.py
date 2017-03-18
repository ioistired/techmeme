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


if __name__ == '__main__':
	import sys
	sys.exit(unittest.main(verbosity=2))
