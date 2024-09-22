import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
from tempfile import NamedTemporaryFile
# Load the custom YOLOv8 classifier model
model = YOLO('C:\\Users\\User\\Desktop\comp 403\\runs\classify\\train\weights\\best.pt')


# Define a function to classify brain tumors
def classify_brain_tumor(image):
    #convert numot array to pil image
    image_pil = Image.fromarray(image)
    # Make predictions using the model
    results = model.predict(image_pil)

    # Extract the class label and confidence score
    class_label = results.names[int(results.pred[0].cls)]
    confidence_score = results.conf[0, int(results.pred[0].cls)]

    # Return the class label and confidence score
    return class_label, confidence_score


# Define a function to display the image and classification result
def display_result(image, class_label, confidence_score):
    st.image(image, caption='Brain Tumor Image')
    st.write(f'Class Label: {class_label}')
    st.write(f'Confidence Score: {confidence_score}')


# Upload the brain tumor image
image = st.file_uploader('Upload Brain Tumor Image', type=['jpg','jpeg','png'])

# If an image is uploaded, classify it
if image is not None:
    #save the uploaded imag eto a temporary file
   # with NamedTemporaryFile(delete= False) as tmp:
      #  tmp.write(image.getbuffer())
       # tmp.seek(0)
       # image_path = tmp.name
    image_pil = Image.open(image)
    # Read the image as a numpy array

    image = cv2.cvtColor(np.array(image_pil),cv2.COLOR_RGB2BGR)
    #image = Image.fromarray(image)

    # Classify the brain tumor
    class_label, confidence_score = classify_brain_tumor(image)

    # Display the classification result
    display_result(image, class_label, confidence_score)
