import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load CSV file
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to display the dataset
def display_dataframe(data):
    st.write("### Show the data")
    st.dataframe(data)

# Function to display head of the dataset
def display_head(data):
    st.write("### Dataset Head")
    st.write(data.head())

# Function to display basic statistics
def display_statistics(data):
    st.write("### Basic Statistics")
    st.write(data.describe())

# Main function
def main():
    st.title("Explore Tabular Data")

    # File upload
    uploaded_file = 'training.csv'#st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        
        # Dropdown for data exploration options
        options = ["Display Data", "Display Head", "Display Basic Statistics"]
        selected_option = st.selectbox("Select an option:", options)

        # Perform the selected action based on the dropdown choice
        if selected_option == "Display Data":
            display_dataframe(data)
        elif selected_option == "Display Head":
            display_head(data)
        elif selected_option == "Display Basic Statistics":
            display_statistics(data)

# Run the app
if __name__ == "__main__":
    main()
