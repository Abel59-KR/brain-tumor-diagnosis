import streamlit as st
import pandas as pd
import numpy as np
from auth import login
from PIL import Image
from ultralytics import YOLO
from dbco import mycursor

# Define containers
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
recordSection = st.container()

# Function to show main page for brain tumor classification
def show_main_page():
    with mainSection:
        # Set title
        st.title('Brain Tumor Classification')

        # Set header
        st.header('Please upload brain MRI image')

        # Load model
        model = YOLO("C:\\Users\\User\\PycharmProjects\\pythonProject6\\runs\\classify\\train5\weights\\best.pt")

        # Upload file
        uploaded_image = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])

        if uploaded_image is not None:
            # Open the uploaded image
            with Image.open(uploaded_image) as image:
                st.image(image=image)
                img = image.convert('RGB')
                results = model.predict(img)
                names = results[0].names

                probability = results[0].probs.data.numpy()
                prediction = np.argmax(probability)
                # Display the prediction results
                for i in range(len(names)):
                    if probability[i] > 0.90:
                        st.write(f"Class: {names[i]}, Confidence: {probability[i]:.2f}")

# Function to handle log out
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False

# Function to show log out page
def show_logout_page():
    loginSection.empty()
    with logOutSection:
        st.button("Log Out", key="logout", on_click=LoggedOut_Clicked)

# Function to handle log in
def LoggedIn_Clicked(UserId, password):
    if login(UserId, password):
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid user name or password")

# Function to show log in page
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            UserId = st.text_input(label="", value="", placeholder="Enter your user name")
            password = st.text_input(label="", value="", placeholder="Enter password", type="password")
            st.button("Login", on_click=LoggedIn_Clicked, args=(UserId, password))

# Function to record records to the database
def record(facility_name, disease):
    # Query database to check if the provided credentials are valid
    query = "SELECT * FROM records WHERE facility_name = %s AND disease = %s"
    mycursor.execute(query, (facility_name, disease))
    records = mycursor.fetchone()
    return records

# Main function to run the app
def main():
    with headerSection:
        if 'loggedIn' not in st.session_state:
            st.session_state['loggedIn'] = False
            show_login_page()
        else:
            if st.session_state['loggedIn']:
                show_logout_page()
                show_main_page()
            else:
                show_login_page()

    with recordSection:
        st.title("Record and Visualization")
        facility_name = st.text_input("Enter facility name:")
        disease = st.text_input("Enter disease:")
        if st.button("Record"):
            records = record(facility_name, disease)
            if records:
                st.success("Record saved successfully.")
            else:
                st.error("Failed to save record.")

            # Visualization using bar graph (dummy data)
            df = pd.DataFrame({
                'Facility Name': ['Facility 1', 'Facility 2', 'Facility 3'],
                'Disease Count': [10, 20, 15]
            })
            st.bar_chart(df.set_index('Facility Name'))

# Run the app
if __name__ == "__main__":
    main()
