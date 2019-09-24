#!/usr/bin/env python

import skimage
import glob
from os.path import basename
import numpy as np
import pickle

#class Chess:
#	def __init__(self):
#		self.DESCR = 'Chess'
#		self.COL_NAMES = ['label', 'data']
#		self.data      = []
#		self.target    = []

chess = {
	'DESCR':  'Chess',
	'COL_NAMES':  ['label', 'data'],
	'data':  [],
	'target': []
}

images = glob.glob("images/*.png")
for f in images:
  p = basename(f)
  img = skimage.io.imread(f, as_gray=True)
  img = img.reshape(-1)
  chess['data'].append(img)

  (piece,_) = p.split('_')
  chess['target'].append(piece)

chess['data'] = np.array(chess['data'])
chess['target'] = np.array(chess['target'])

X, y = chess['data'], chess['target']

# Pickle it


print(X.shape)
print(y.shape)

f = open("chess.dat", "wb")
pickle.dump(chess, f)