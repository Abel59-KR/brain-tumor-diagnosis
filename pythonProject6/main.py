from ultralytics import YOLO
import numpy as np
import streamlit as st
from PIL import Image
from dbco import mydb, mycursor
import streamlit as st

# Function to validate user credentials
def authenticate(UserId, password):
    # Query database to check if the provided credentials are valid
    query = "SELECT * FROM users WHERE UserId = %s AND password = %s"
    mycursor.execute(query, (UserId, password))
    user = mycursor.fetchone()
    return user

# Function to run the main application
def main_app():

    # Set title
    st.title('Brain tumor classification')

    # Set header
    st.header('Please upload brain MRI image')

    # Load model
    #model_path = r"C:\Users\User\Desktop\comp 403\runs\classify\train\weights\best.pt"

    # Initializing the model
    model = YOLO("C:\\Users\\User\\PycharmProjects\\pythonProject6\\runs\\classify\\train5\weights\\best.pt")

    # Upload file
    uploaded_image = st.file_uploader('Upload Image', type=['jpg','jpeg','png'])

    if uploaded_image is not None:
        # Open the uploaded image
        with Image.open(uploaded_image) as image:
            st.image(image=image)
            #img1 = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
            img = image.convert('RGB')
            results = model.predict(img)
           # image = results[0].image
            names = results[0].names

           # width = img.shape[0]


            probability = results[0].probs.data.numpy()
            prediction = np.argmax(probability)
            # Display the prediction results
            for i in range(len(names)):
                if probability[i] > 0.90:
                    st.write(f"Class: {names[i]}, Confidence: {probability[i]:.2f}")
                #: st.write("unable to classify")

            #st.write(names)
            #st.write(prediction)


