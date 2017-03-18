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
		# <https://github.com/WonderJ13/We-Are-Number-One-Meme-Generator/blob/master/main.py>
		self.assertEqual(self.config.timestamps, [
			39.21739,
			45.21739,
			56.91304,
			77.91304,
			83.69565,
			91.086956,
			132.60869,
			139.30434,
			156.30434,
			162.30434,
			163.82608,
			165.30434,
		])

if __name__ == '__main__':
	import sys
	sys.exit(unittest.main(verbosity=2))
