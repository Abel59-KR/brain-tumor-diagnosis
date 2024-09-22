# steps 
# data 
The data is acquired from kaggle(link) and the dataset is categorized into 3 part
1. meningiom.
2. Glicoma.
3. pitiutary.
# Data pre-processing
The images are of the .jpeg or .png extension.
Denoising technique used is bilateral filtering.
Qualitative analysis used is PSNR for evaluating the effectiveness of the the denoising technique.
Histogram equalizationis used to distribute pixel intesity across the image. 
# Training and evaluation 
YOLOv8 pretrained model is used for trainning and validation. 
