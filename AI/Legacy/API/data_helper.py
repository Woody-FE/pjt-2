# -*- coding:utf-8 -*-
import os
import json
import random
import pandas as pd
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset

# 이미지 사이즈는 origin 삽화 기준으로 설정할 것!
image_size = 64


class FaceImageDataset(Dataset):
    def __init__(self, root, info, device, mode='train'):
        self.root = root
        self.info = info
        self.mode = mode
        self.device = device

        if mode not in ['train', 'validation', 'test']:
            raise NotImplemented('Must choose mode('train', 'validation', 'test'))

    def __getitem__(self, idx):
        temp=self.info[idx]
        image_path=os.path.join(self.root, temp['image'])

        image=self.image_preprocess(img_path)
        sex=(0 if temp['sex'] == 'male' else 1)
        age=self._age_categorization(temp['age'])

        return {
            'image': image,
            'sex': sex,
            'age': age
        }

    def image_preprocess(self, image_path):
        image = Image.open(image_path)
        if self.mode == 'train':
            preprocess = transforms.Compose([transforms.Resize(image_size+4),
            transforms.RandomCrop()])
