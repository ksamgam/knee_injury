from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    width_shift_range=[-25, 25],
    height_shift_range=[-25, 25],
    rotation_range=[-25,25],
    horizontal_flip=True)