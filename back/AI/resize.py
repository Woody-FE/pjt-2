import os
import cv2
import math
import numpy as np
import face_recognition as fr
from PIL import Image
from Cartoonization import test

hat_image_path = './images/hat_images/zookeeper_hat.png'
hat_image = Image.open(hat_image_path)
resize_size = (250, 150)
resized_hat_image = hat_image.resize(resize_size)

resized_hat_image.save(hat_image_path, "PNG", quality = 100)