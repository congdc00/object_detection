from lib_all import *
from sourc_code.utils.augmentations import Compose, ConvertFromInts, ToAbsoluteCoords, PhotometricDistort, Expand, RandomSampleCrop, RandomMirror, ToPercentCoords, Resize, SubtractMeans

class DataTransform:
    def __init__(self, input_size, color_mean):
        self.data_transform = {
            "train": Compose([
                ConvertFromInts(), #Chuyển định dạng ảnh từ int về float 32
                ToAbsoluteCoords(), #Chuyển thông tin annotation về dạng nomarl
                PhotometricDistort(), #Thay đổi màu sắc
                Expand(color_mean), #Mở rộng bức ảnh
                RandomSampleCrop(), #Cắt 1 phần bất kỳ của bức ảnh ra
                RandomMirror(), #Xoay ảnh ngược lại ( từ trái -> phải, phải -> trái)
                ToPercentCoords(), #Chuyển nó về dạng chuẩn hóa [0,1]
                Resize(input_size), #Đưa về dạng 300*300
                SubtractMeans(color_mean), #Trừ đi mean của từng channel BGR để đưa nó về dạng chuẩn hóa
            ]),
            "val": Compose([
                ConvertFromInts(),
                Resize(input_size),
                SubtractMeans(color_mean)
            ])
        }
    def __call__(self, img, phase, boxes, labels): #phase là train hay là validation
        return self.data_transform[phase](img,boxes, labels)