#!/usr/bin/env python3
# encoding: utf-8

import techmeme
from techmeme import TechnicalMeme


def main(config_filename, output_filename):
	TechnicalMeme(config_filename).save(output_filename)


if __name__ == '__main__':
	import sys

	if len(sys.argv) < 3:
		print('Usage: {} <config_filename> <output_filename>'.format(sys.argv[0]))
	else:
		# could also do *argv[1:3] but that's less clear IMO
		main(sys.argv[1], sys.argv[2])
