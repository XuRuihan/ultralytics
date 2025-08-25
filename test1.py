import torch
import torch.nn as nn
from thop import profile  # 假设已安装 thop

model = nn.ConvTranspose2d(in_channels=256, out_channels=128, kernel_size=2, stride=2)
input = torch.randn(1, 256, 20, 20)  # 批次 1，3 通道，16x16
model2 = nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=2, stride=2)
input2 = torch.randn(1, 128, 40, 40)  # 批次 1，3 通道，16x16
flops, params = profile(model, inputs=(input,))
flops2, params2 = profile(model2, inputs=(input2,))
print((flops+flops2)/1e9 *2)