
# coding: utf-8

# In[1]:


import argparse
import tensorflow as tf
import numpy as np
from PIL import Image
import time
import matplotlib.pyplot as plt
import cv2

from tqdm import trange
from utils.config import Config
from model import ICNet, ICNet_BN


# # Setup configurations

# In[2]:


model_config = {'train': ICNet, 'trainval': ICNet, 'train_bn': ICNet_BN, 'trainval_bn': ICNet_BN, 'others': ICNet_BN}

# Choose dataset here, but remember to use `script/downlaod_weight.py` first
dataset = 'ade20k'
filter_scale = 2
    
class InferenceConfig(Config):
    def __init__(self, dataset, is_training, filter_scale):
        Config.__init__(self, dataset, is_training, filter_scale)
    
    # You can choose different model here, see "model_config" dictionary. If you choose "others", 
    # it means that you use self-trained model, you need to change "filter_scale" to 2.
    model_type = 'trainval_bn'

    # Set pre-trained weights here (You can download weight from Google Drive) 
    model_weight = 'ade20k/model.ckpt-27150'
    
    # Define default input size here
    INFER_SIZE = (256, 512, 3)
                  
cfg = InferenceConfig(dataset, is_training=False, filter_scale=filter_scale)
cfg.display()


# # Create graph, session, and restore weights

# In[3]:


start_time = time.time()
# Create graph here 
model = model_config[cfg.model_type]
net = model(cfg=cfg, mode='inference')
# Create session & restore weight!
net.create_session()
net.restore(cfg.model_weight)
print("time to load model: ", time.time() - start_time)


# # Run segmentation on single image

# In[4]:


im1 = cv2.imread('bedroom.jpg')
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
if im1.shape != cfg.INFER_SIZE:
    im1 = cv2.resize(im1, (cfg.INFER_SIZE[1], cfg.INFER_SIZE[0]))
start = time.time()
results1 = net.predict(im1)
overlap_results1 = 0.5 * im1 + 0.5 * results1[0]
vis_im1 = np.concatenate([im1/255.0, results1[0]/255.0, overlap_results1/255.0], axis=1)
print("time to predic: ", time.time() - start)
plt.figure(figsize=(20, 15))
plt.imshow(vis_im1)

