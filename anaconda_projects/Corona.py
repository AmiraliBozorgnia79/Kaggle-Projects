import kagglehub
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import os
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Flatten,Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential
import random

# 1) Set a fixed seed value
SEED = 42

# 2) Set seeds for Python, NumPy, and TensorFlow
os.environ['PYTHONHASHSEED'] = str(SEED)
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

path="/Users/amiralibozorgnia/PycharmProjects/Kaggle Projects/Covid19-dataset"


#=======================================================================================
"remove the file contaiong DS store module"
for filename in os.listdir(path):
    if filename.endswith(".DS_Store"):
       (os.remove(os.path.join(path, filename)))
    else:
        print("no file with extension .DS_Store")
"checking the folders'names"
for filename in os.listdir(path):
    print(filename)
#=======================================================================================
file_director={}
for filename in os.listdir(path):
    file_director[filename]=os.path.join(path,filename)
print(file_director)
print('\n','-----'*30)

train_directory={}
for filename in os.listdir(file_director['train']):
    train_directory[filename]=os.path.join(file_director['train'],filename)
print(train_directory)
print('\n','-----'*30)

test_directory={}
for filename in os.listdir(file_director['test']):
    test_directory[filename]=os.path.join(file_director['test'],filename)
print(test_directory)
print('\n','-----'*30)
#=======================================================================================
"image loading"
train_path=file_director['train']
test_path=file_director['test']
print(train_path)

IMG_size=(224,224)
SEED=42
batch_size=32

train_dataset=tf.keras.utils.image_dataset_from_directory(
    train_path,
    image_size=IMG_size,
    seed=SEED,
    batch_size=batch_size,
    label_mode='int',
    shuffle=True,
    color_mode="grayscale"
)

test_dataset=tf.keras.utils.image_dataset_from_directory(
    test_path,
    image_size=IMG_size,
    seed=SEED,
    batch_size=batch_size,
    label_mode='int',
    shuffle=True,
    color_mode="grayscale"
)

print(train_dataset.class_names)


#=======================================================================================
"Ploting samples of data "
def image_plot():
   for image,label in train_dataset.take(1):
      for i in range(12):
        plt.subplot(4,3,i+1)
        plt.imshow(image[i].numpy().astype('uint8'),cmap='gray')
        plt.axis('off')
        plt.title(train_dataset.class_names[label[i]])
   plt.show()
#=======================================================================================
"Building model"
model=Sequential()

#first layer:
model.add(Conv2D(filters=16, kernel_size=(3,3),
                activation='relu', padding='Same'))
#pooling layer
model.add(MaxPooling2D(pool_size=(2,2)))

#second hidden layer
model.add(Conv2D(filters=32, kernel_size=(3,3),
                 activation='relu', padding='Same'))
#pooling layer
model.add(MaxPooling2D(pool_size=(2,2)))

#Third layer
model.add(Conv2D(filters=64, kernel_size=(3,3),
                 activation='relu', padding='Same'))
#max pooling layer
model.add(MaxPooling2D(pool_size=(2,2)))

#Dropout layer
model.add(Dropout(0.2))

#Flatten the data
model.add(Flatten())

#Dense Layer
model.add(Dense(128, activation='relu'))

#model drop out
model.add(Dropout(0.5))

#Last layer
model.add(Dense(3, activation='softmax'))

#-----compiling model with data---------

model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer='adam',metrics=['accuracy'])

history=model.fit(train_dataset,epochs=10)

#=====================================
y_pred=[]
y_true=[]
for image,labels in test_dataset:
    pred=model.predict(image,verbose=0)
    pred=np.argmax(pred,axis=1)
    y_pred.extend(pred)
    y_true.extend(labels.numpy())

y_true = np.array(y_true)
y_pred = np.array(y_pred)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
class_names = test_dataset.class_names  # folder names

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_names, yticklabels=class_names)

plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()