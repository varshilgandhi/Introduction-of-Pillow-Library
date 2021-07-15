# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 01:54:19 2021

@author: abc
"""
#In pillow noot a numpy array
from PIL import Image

img = Image.open("C:/Users/abc/Desktop/image/test_image.jpg")
"""
print(type(img))

print(img.format)

print(img.mode)

print(img.size)

small_img = img.resize((200,300))
small_img.save("C:/Users/abc/Desktop/image/test_image_small.jpg")

img.thumbnail((1200,1300))
img.save("C:/Users/abc/Desktop/image/test_image_tmbnail.jpg")
print(img.size)
"""

##############################################################################
"""
cropped_img = img.crop((0,0,300,300))
cropped_img.save("C:/Users/abc/Desktop/image/cropped_img.jpg")

"""

##############################################################################

"""

# copy and paste the image:
img1 = Image.open("C:/Users/abc/Desktop/image/test_image.jpg")
print(img1.size)
img2 = Image.open("C:/Users/abc/Desktop/image/lighthouse.jpg")

print(img2.size)
img2.thumbnail((150,200))



img1_copy = img1.copy()
img1_copy.paste(img2,(50,50))

img1_copy.save("C:/Users/abc/Desktop/image/pasted_image.jpg")


"""
##############################################################################

"""
#Image Rotaion

img45 = img.rotate(45,expand=True)
img45.save("C:/Users/abc/Desktop/image/rotated45.jpg")
"""

##############################################################################
"""

#flip the image  (RIGHT TO LEFT   OR    TOP TO BOTTOM)

img_flipTB = img.transpose(Image.)
img_flipTB.save("C:/Users/abc/Desktop/image/filppedTB.jpg")
"""


##############################################################################
"""
#Convert image into gray image

grey_img = img.Convert("L")
grey_img.save("C:/Users/abc/Desktop/image/gray_rgbimage.jpg")
"""

#############################################################################

# Glob Library
"""
from PIL import Image
import glob

path = "C:/Users/abc/Desktop/image/aeroplane/*"

for file in glob.glob(path):
    print(file)
    a = Image.open(file)
    rotated45 = a.rotate(45, expand=True)
    rotated45.save(file+"_rotated45.png","PNG")  

"""

##############################################################################



                        #THANK YOU











 








