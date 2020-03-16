# Spin up ImageJ.
import imagej

# ij = imagej.init('sc.fiji:fiji:2.0.0-pre-10')
ij = imagej.init('G:/My Drive/Harvard/Ophthalmology Research/Software/Fiji.app')

print(ij.getVersion())
print(ij.getApp().getInfo(True))

from skimage import io
import numpy as np
img = io.imread('https://samples.fiji.sc/new-lenna.jpg')
img = np.mean(img[500:1000,300:850], axis=2)
ij.py.show(img, cmap = 'gray')