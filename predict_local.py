from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np


model=load_model(r"C:\Users\rasoo\Data_science\OLD DATA BOOKS\Image-classification-Project\model\model_vgg16.h5")
img=image.load_img(r"C:\Users\rasoo\Data_science\OLD DATA BOOKS\Image-classification-Project\cat.jpg",target_size=(224,224))
# Z = plt.imread(r'/content/cat.jpg')
# plt.imshow(Z)
image_array = image.img_to_array(img)
print("-------",image_array.shape)
image_array = image_array/255
image_array = np.expand_dims(image_array, axis = 0)
test_image=preprocess_input(image_array)
result = np.argmax(model.predict(test_image), axis=1)
if result[0] == 1:
    prediction = 'dog'
    print(prediction)
else:
    prediction = 'cat'
    print(prediction)