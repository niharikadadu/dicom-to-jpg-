# -*- coding: utf-8 -*-


import pydicom as dicom
import os
import cv2
import PIL # optional

# make it True if you want in PNG format
PNG = False
# Specify the .dcm folder path
folder_path = ""
# Specify the output jpg/png folder path
jpg_folder_path = ""

import matplotlib.pylab as plt

images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    if PNG == False:
        image = image.replace('.dicom', '.jpg')
    else:
        image = image.replace('.dicom', '.png')
    plt.imsave(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))