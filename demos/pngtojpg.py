import argparse
import os

import cv2
import glob

parser = argparse.ArgumentParser()
options = parser.add_argument_group('How to use')

options.add_argument('-f', '--folder', dest='input', type=str,
					 required=True)

args = parser.parse_args()
for i in glob.glob(args.input):
	names = (os.path.split(os.path.abspath(i)))
	cv2.imwrite(names[0] + '\\' + names[1].replace('png', 'jpg'), cv2.imread(i))
