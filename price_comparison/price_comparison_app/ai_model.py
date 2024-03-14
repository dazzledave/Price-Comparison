# ai_model.py
# You'll need to install tensorflow & pillow to run this
 
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pre-trained InceptionV3 model
model = InceptionV3(weights='imagenet')

def describe_image(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(299, 299))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict the content of the image
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Extract labels and scores
    predictions_list = []
    for _, label, score in decoded_predictions:
        predictions_list.append(f"{label} ({score:.2f})")

    return predictions_list

