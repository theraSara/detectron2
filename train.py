import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import pathlib
import os
import random
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, MaxPool2D
from tensorflow.keras import Model, layers, models, Input
from tensorflow.keras.utils import plot_model
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
import warnings
warnings.filterwarnings('ignore')

dataset = '/kaggle/input/trash-type-detection/trash_images/'
dataset_dir = pathlib.Path(dataset)

class_names = os.listdir(dataset_dir)
print(class_names)
