import torch
import torchvision.transforms as transforms
import cv2
import matplotlib.pyplot as plt

from network.Transformer import Transformer

model = Transformer()
model.load_state_dict(torch.load('pretrained_model/Hayao_net_G_float.pth'))
model.eval()
print('Model Loaded!')