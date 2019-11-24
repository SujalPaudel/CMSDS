#This code helps to put a white patch behind the cropped image.
#The final dimension after the white patch would be 96*96

from PIL import Image
import os
import random
import time

rootdir = 'cummilative_dataset/100%'

def patcher(rootdir):

	count = 0

	rootdir = rootdir

	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
	    	if file.endswith('.png'):
			    g = os.path.join(subdir, file)
			    img = Image.open(g)
			    width, height = img.size

			    half_width = width /2
			    half_height = height /2

			    x1, y1, x2, y2 = 0, 0, 352, 288  # cropping coordinates

			    xm = 176
			    ym = 144

			    start_x = round(xm - half_width)

			    start_y = round(ym - half_height)

			    bg = Image.new('RGB', (x2 - x1, y2 - y1), (0,0,0))
			    bg.paste(img, (start_x, start_y))
			    bg.save('ramlal/100%/' + file)


patcher(rootdir)
