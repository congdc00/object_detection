import os
import os.path as osp
import random
import xml.etree.ElementTree as ET
import cv2
import torch
import torch.utils.data as data
from torch.autograd import Function # tu dong tinh gradient
import numpy as np
#noron network
import torch.nn as nn
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
import pandas as pd
from numpy import random
from math import sqrt

import itertools

# Cài đặt các tham số ngẫu nhiên
torch.manual_seed(1234)
np.random.seed(1234)
random.seed(1234)

import torch.nn as nn
from torch.autograd import Function
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
from matplotlib import pyplot as plt

import itertools
from math import sqrt
import time

import streamlit
from PIL import Image
import nbimporter
