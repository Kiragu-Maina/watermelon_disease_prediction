import tensorflow as tf
import numpy as np
import zipfile

with zipfile.ZipFile('class_names.zip', 'r') as archive:
    class_names_str = archive.read('class_names.txt').decode('utf-8')

# Split the string to get the class names as a list
class_names = class_names_str.split('\n')


# Replace this with the path to your saved model directory
saved_model_path = "/home/kiragu-m/ml models/watermelon_disease_prediction_model_zip(1)/"

# Load the saved model
model = tf.saved_model.load(saved_model_path)

image_path = '/home/kiragu-m/ml models/IMG_4071.jpg'

# Load the image from the local file
img = tf.keras.utils.load_img(image_path, target_size=(512, 512))
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create a batch

predictions = model(img_array)
score = tf.nn.softmax(predictions[0])

print(score)

# Replace 'class_names' with the list of class names used by your model
# class_names = [...]  # Add your class names here

print(
    "This image most likely belongs to {}"
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)
