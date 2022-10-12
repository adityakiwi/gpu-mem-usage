# Import packages
import torch
import os,sys,humanize,psutil,GPUtil
import torchvision.models as models

def mem_report():
    print("CPU RAM Free: " + humanize.naturalsize( psutil.virtual_memory().available ))
    GPUs = GPUtil.getGPUs()
    for i, gpu in enumerate(GPUs):
        print('GPU {:d} ... Mem Free: {:.0f}MB  / {:.0f}MB  | Utilization {:3.0f}%'.format(i, gpu.memoryFree, gpu.memoryTotal, gpu.memoryUtil*100))
    
wide_resnet50_2 = models.wide_resnet50_2(weights=models.Wide_ResNet50_2_Weights.DEFAULT)
if torch.cuda.is_available():
    wide_resnet50_2.cuda()

mem_report()
