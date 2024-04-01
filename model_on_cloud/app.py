import os
import tensorflow as tf
from google.cloud import aiplatform
import numpy as np

# Define constants
PROJECT_ID = "cosmic-ascent-418910"
ENDPOINT_ID = "2492781976168169472"
REGION = "asia-east2"
IMG_FILE = "data\\testSample\img_344.jpg"

# Define the possible classes (numbers 0 to 9)
number_class = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def get_num_class(probability_result):
    """Returns the class with the highest probability."""
    # Use argmax to find the index of the maximum probability
    return number_class[tf.argmax(probability_result[0])]


def resizing_img(img):
    """Preprocesses and resizes the input image for model prediction."""
    img = tf.image.decode_jpeg(img)
    img = tf.image.resize(img, [28, 28])
    img = tf.squeeze(img, axis=-1)
    img = img / 255.0
    img = tf.expand_dims(img, axis=0)
    return img


def predict_custom_trained_model(instances, project_number, region, endpoint_id):
    """Uses Vertex AI endpoint to make predictions."""
    endpoint = aiplatform.Endpoint(
        endpoint_name=f"projects/{project_number}/locations/{region}/endpoints/{endpoint_id}"
    )
    result = endpoint.predict(instances=[instances])
    return result.predictions


# Read image and convert to bytes
cwd = os.path.abspath(os.path.dirname(__file__))
img_path = os.path.join(os.getcwd(), IMG_FILE)
img = tf.io.read_file(img_path)

# Preprocess and resize the image
img = resizing_img(img)

# Convert to list for Vertex AI endpoint prediction
img_as_list = img.numpy().tolist()

# Make predictions using the custom trained model
prediction_result = predict_custom_trained_model(
    instances=img_as_list,
    project_number=PROJECT_ID,
    region=REGION,
    endpoint_id=ENDPOINT_ID,
)

# Print the predicted class
print("This number is: ", get_num_class(prediction_result))
