#!/usr/bin/env python
import subprocess
import glob
from os.path import basename

squares = {
  'B':'WB',
  'K':'WK',
  'L':'BK',
  'M':'BN',
  'N':'WN',
  'O':'BP',
  'P':'WP',
  'Q':'WQ',
  'R':'WR',
  'T':'BR',
  'V':'BB',
  'W':'BQ',
  'b':'WB',
  'k':'WK',
  'l':'BK',
  'm':'BN',
  'n':'WN',
  'o':'BP',
  'p':'WP',
  'q':'WQ',
  'r':'WR',
  't':'BR',
  'v':'BB',
  'w':'BQ'
  }

i = 0
for k in squares.keys():
  # Basic image

  origFilename = "%s_%d.png" % (squares[k], i)
  command = 'convert -background white -alpha remove -size 72x72 xc:none -font "fonts/CASEFONT.TTF" -pointsize 72 -fill black -annotate +0+72 "%s" images/%s' % (k, origFilename)
  subprocess.run(command, shell=True, check=True)
  i += 1	

  # Noise image
  noiseFilename = "%s_%d.png" % (squares[k], i)
  command = 'convert images/%s +noise Poisson images/%s' % (origFilename, noiseFilename)
  subprocess.run(command, shell=True, check=True)
  i += 1

  # Blur original image
  blurFilename = "%s_%d.png" % (squares[k], i)
  command = 'convert images/%s -blur 0x2 images/%s' % (origFilename, blurFilename)
  subprocess.run(command, shell=True, check=True)
  i += 1

  # Blur noise image
  blurFilename = "%s_%d.png" % (squares[k], i)
  command = 'convert images/%s -blur 0x2 images/%s' % (noiseFilename, blurFilename)
  subprocess.run(command, shell=True, check=True)
  i += 1

# Rotate every image in 5 degree increments
images = glob.glob("images/*.png")
for f in images:
  p = basename(f)
  (piece,_) = p.split('_')
  for r in range(5, 360, 5):
    rotatedFilename = "%s_%d.png" % (piece, i)
    command = 'convert images/%s -rotate %d -crop 72x72+0+0 images/%s' % (p, r, rotatedFilename)
    subprocess.run(command, shell=True, check=True)
    i += 1
    print(i)

# Black Squares
# B - white bishop
# K - white king
# L - black king
# M - black knight
# N - white knight
# O - black pawn
# P - white pawn
# Q - white queen
# R - white rook
# T - black rook
# V - black bishop
# W - black queen

# White Squares
# b - white bishop
# k - white king
# l - black king
# m - black knight
# n - white knight
# o - black pawn
# p - white pawn
# q - white queen
# r - white rook
# t - black rook
# v - black bishop
# w - black queen
