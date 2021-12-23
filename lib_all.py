import os
import random
import xml.etree.ElementTree as ET
import cv2
import torch
import torch.utils.data as data
import os
import numpy as np
#gửi request tới trang chứa đường link download của mình
import urllib.request
# File download về là file zip nên phải unzip ra
import zipfile
# Nếu là file tar thì dùng cái dưới
import tarfile
from matplotlib import pyplot as plt
# Sử dụng trong augmentation.py
from torchvision import transforms
import types
from numpy import random


# Cài đặt các tham số ngẫu nhiên
torch.manual_seed(1234)
np.random.seed(1234)
random.seed(1234)

