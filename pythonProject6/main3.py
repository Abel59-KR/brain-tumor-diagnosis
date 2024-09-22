
import streamlit as st
from auth import login
import numpy as np
from PIL import Image
from ultralytics import YOLO
from dbco import mydb, mycursor
import pandas as pd
from utils import set_background


headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()


set_background('human-brain-medical-digital-illustration.jpg')



def show_main_page():
    with mainSection :
        # Set title
        st.title('Brain tumor classification')
        # Set header
        st.header('Please upload brain MRI image')

        # Load model
        # model_path = r"C:\Users\User\Desktop\comp 403\runs\classify\train\weights\best.pt"

        # Initializing the model
        model = YOLO("C:\\Users\\User\\Videos\\runs\\classify\\train\\weights\\last.pt")
        # caution warning
        st.write("Caution: Handle medical images with care")
        # Upload file
        uploaded_image = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])

        if uploaded_image is not None:
            # Open the uploaded image
            with Image.open(uploaded_image) as image:
                st.image(image=image)
                # img1 = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
                img = image.convert('RGB')
                results = model.predict(img)
                # image = results[0].image
                names = results[0].names

                # width = img.shape[0]

                probability = results[0].probs.data.numpy()
                prediction = np.argmax(probability)
                # Display the prediction results
                # load class names

                for i in range(len(names)):
                    if probability[i] > 0.90:
                        st.write(f"Class: {names[i]}, Confidence: {probability[i]:.2f}")
                        classname = names[i]
                        confidence_score = float(probability[i])

                        query = 'INSERT INTO predictions (classname, Confidence_score,created_at) VALUES (%s, %s, NOW())'
                        val = (classname, confidence_score)
                        mycursor.execute(query, val)
                        mydb.commit()


                        # Button to display all predictions


        # Button to display all predictions
        if st.session_state['loggedIn']:
            if st.button("Activity"):
                # Retrieve all records from the 'predictions' table
                query = "SELECT * FROM predictions"
                mycursor.execute(query)
                results = mycursor.fetchall()

                # Display retrieved data in a table
                if results:
                    st.write("**Prediction History**")
                    df = pd.DataFrame(results, columns=["Class Name", "Confidence Score","Date & Time "])
                    st.table(df)
                else:
                    st.write("No predictions found in the database.")


def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False


def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button("Log Out", key="logout", on_click=LoggedOut_Clicked)


def LoggedIn_Clicked(UserId, password):
    if login(UserId, password):
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False;
        st.error("Invalid user name or password")


def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            UserId = st.text_input(label="", value="", placeholder="Enter your user name")
            password = st.text_input(label="", value="", placeholder="Enter password", type="password")
            st.button("Login", on_click=LoggedIn_Clicked, args=(UserId, password))


with headerSection:
    # st.title("Streamlit Application")
    # first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page()
    else:
        if st.session_state['loggedIn']:
            show_logout_page()
            show_main_page()
        else:
            show_login_page()