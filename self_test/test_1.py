import torch.nn as nn
import torch

in_channels = 6
model = nn.ConvTranspose3d(in_channels, in_channels * 4, kernel_size=3, stride=1,bias=False,padding=1)
model_2 = nn.Conv2d(in_channels, in_channels * 4, kernel_size=3, stride=2,bias=False,padding=1)
model_3 = nn.Conv3d(in_channels, in_channels * 4, kernel_size=3, stride=2,bias=False,padding=1)

one = torch.randn(4,6,6,512,640)
two = torch.randn(4,6,512,640)

out = model_3(two)

print("test")

