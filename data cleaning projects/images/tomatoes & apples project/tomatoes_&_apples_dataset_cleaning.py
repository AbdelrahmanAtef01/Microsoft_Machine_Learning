# -*- coding: utf-8 -*-
"""Tomatoes & Apples_dataset_cleaning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mvTbK3Kwd5pGKkT3FtbxdcspjgTqlupB
"""

!pip install imagehash

import pandas as pd
import numpy as np
import random

from google.colab import drive
drive.mount('/content/drive')

from PIL import Image, ImageEnhance
import imagehash

import cv2
import os

import matplotlib.pylab as plt
plt.style.use('ggplot')

tomato_files = os.listdir('/content/drive/MyDrive/Data sets/tomatoes & apples/tomatoes')
tomato_images = []
for file in tomato_files:
  tomato_images.append(cv2.imread('/content/drive/MyDrive/Data sets/tomatoes & apples/tomatoes/' + file))

apple_files = os.listdir('/content/drive/MyDrive/Data sets/tomatoes & apples/apples')
apple_images = []
for file in apple_files:
  apple_images.append(cv2.imread('/content/drive/MyDrive/Data sets/tomatoes & apples/apples/' + file))

plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(cv2.cvtColor(tomato_images[i], cv2.COLOR_BGR2RGB))
    plt.axis('off')
plt.show()

plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(cv2.cvtColor(apple_images[i], cv2.COLOR_BGR2RGB))
    plt.axis('off')
plt.show()

#check for imbalanced data

print(len(tomato_files))
print(len(apple_files))

#hashing images and find duplicates

tomato_image_hashes = {}
tomato_duplicates = []

apple_image_hashes = {}
apple_duplicates = []

for img_array  in tomato_images:

    img = Image.fromarray(img_array)
    hash_value = imagehash.phash(img)
    if hash_value in tomato_image_hashes:
       tomato_duplicates.append((img_array, tomato_image_hashes[hash_value]))
    else:
       tomato_image_hashes[hash_value] = img_array

for img_array  in apple_images:

    img = Image.fromarray(img_array)
    hash_value = imagehash.phash(img)
    if hash_value in apple_image_hashes:
       apple_duplicates.append((img_array, apple_image_hashes[hash_value]))
    else:
       apple_image_hashes[hash_value] = img_array

print(len(tomato_duplicates))
print(len(apple_duplicates))

#delete duplicates

for duplicate in tomato_duplicates:
  for i in range(len(tomato_images)):
    if tomato_images[i].shape == duplicate[0].shape and np.array_equal(tomato_images[i], duplicate[0]):
      del tomato_images[i]
      break

for duplicate in apple_duplicates:
  for i in range(len(apple_images)):
    if apple_images[i].shape == duplicate[0].shape and np.array_equal(apple_images[i], duplicate[0]):
      del apple_images[i]
      break

print(len(tomato_images))
print(len(apple_images))

#resizing images to a standard

for i in range(len(tomato_images)):
  tomato_images[i] = cv2.resize(tomato_images[i], (224, 224), interpolation = cv2.INTER_CUBIC)

for i in range(len(apple_images)):
  apple_images[i] = cv2.resize(apple_images[i], (224, 224), interpolation = cv2.INTER_CUBIC)

print(tomato_images[7].shape)
print(apple_images[0].shape)

#since all photos are very bright let's darken some

for tomato_image,file in zip(tomato_images, tomato_files):
    darkened_image = cv2.convertScaleAbs(tomato_image, alpha=0.5, beta=0)
    cv2.imwrite('/content/drive/MyDrive/Data sets/tomatoes & apples/tomatoes/darken' + file, darkened_image)

for apple_image,file in zip(apple_images, apple_files):
    darkened_image = cv2.convertScaleAbs(apple_image, alpha=0.5, beta=0)
    cv2.imwrite('/content/drive/MyDrive/Data sets/tomatoes & apples/apples/darken' + file, darkened_image)

tomato_files = os.listdir('/content/drive/MyDrive/Data sets/tomatoes & apples/tomatoes')
tomato_images_total = []
for file in tomato_files:
  tomato_images_total.append(cv2.imread('/content/drive/MyDrive/Data sets/tomatoes & apples/tomatoes/' + file))

plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(cv2.cvtColor(tomato_images_total[i + 220], cv2.COLOR_BGR2RGB))
    plt.axis('off')
plt.show()

apple_files = os.listdir('/content/drive/MyDrive/Data sets/tomatoes & apples/apples')
apple_images_total = []
for file in apple_files:
  apple_images_total.append(cv2.imread('/content/drive/MyDrive/Data sets/tomatoes & apples/apples/' + file))

plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(cv2.cvtColor(apple_images_total[i + 220], cv2.COLOR_BGR2RGB))
    plt.axis('off')
plt.show()

#applying image augmentation for diversity

for tomato_image, file in zip(tomato_images, tomato_files):
    i=random.choice([0,1,2,3,4])
    if i==0:
       aug_img = cv2.flip(tomato_image, i)
    elif i==1:
       aug_img = cv2.flip(tomato_image, i)
    elif i==2:
      height, width = tomato_image.shape[:2]
      rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
      aug_img = cv2.warpAffine(tomato_image, rotation_matrix, (width, height))
    elif i==3:
      aug_img = cv2.transpose(tomato_image)
    else:
      temp = cv2.resize(tomato_image, (448, 448), interpolation = cv2.INTER_CUBIC)
      aug_img = tomato_image[112:336, 112:336]

    cv2.imwrite('/content/drive/MyDrive/Data sets/tomatoes & apples/tomatoes/aug ' + file, aug_img)

for apple_image, file in zip(apple_images, apple_files):
    i=random.choice([0,1,2,3,4])
    if i==0:
      aug_img = cv2.flip(apple_image, i)
    elif i==1:
      aug_img = cv2.flip(apple_image, i)
    elif i==2:
      height, width = apple_image.shape[:2]
      rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
      aug_img = cv2.warpAffine(apple_image, rotation_matrix, (width, height))
    elif i==3:
      aug_img = cv2.transpose(apple_image)
    else:
      temp = cv2.resize(apple_image, (448, 448), interpolation = cv2.INTER_CUBIC)
      aug_img = apple_image[112:336, 112:336]

    cv2.imwrite('/content/drive/MyDrive/Data sets/tomatoes & apples/apples/aug ' + file, aug_img)

tomato_files = os.listdir('/content/drive/MyDrive/Data sets/tomatoes & apples/tomatoes')
tomato_images_total = []
for file in tomato_files:
  tomato_images_total.append(cv2.imread('/content/drive/MyDrive/Data sets/tomatoes & apples/tomatoes/' + file))

plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(cv2.cvtColor(tomato_images_total[i + 400], cv2.COLOR_BGR2RGB))
    plt.axis('off')
plt.show()

apple_files = os.listdir('/content/drive/MyDrive/Data sets/tomatoes & apples/apples')
apple_images_total = []
for file in apple_files:
  apple_images_total.append(cv2.imread('/content/drive/MyDrive/Data sets/tomatoes & apples/apples/' + file))

plt.figure(figsize=(10, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(cv2.cvtColor(apple_images_total[i + 500], cv2.COLOR_BGR2RGB))
    plt.axis('off')
plt.show()