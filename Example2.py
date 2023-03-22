import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/model2.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

cotton_leaf = cv2.imread(
    'C:/Users/justm/AppData/Local/Programs/Python/Python311/Plant-Leaf-Disease-Prediction-main/Dataset2/Test/bacterial_blight/bact420.jpg')
# load imageC:\Users\justm\AppData\Local\Programs\Python\Python311\Plant-Leaf-Disease-Prediction-main\Dataset2\Test\fussarium_wilt\fus374.jpg
test_image = cv2.resize(cotton_leaf, (128, 128))

# convert image to np array and normalize
test_image = img_to_array(test_image)/255
test_image = np.expand_dims(test_image, axis=0)  # change dimension 3D to 4D

result = model.predict(test_image)  # predict diseased plant or not

pred = np.argmax(result, axis=1)
print(pred)

if pred == 0:
    print("bacterial_blight")
elif pred == 1:
    print("curl_virus ")
elif pred == 2:
    print("fussarium_wilt")
elif pred == 3:
    print("healthy")
