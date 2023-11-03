import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load CSV file
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to display basic info
def display_info(data):
    st.write("### Dataset Info")
    st.write(data.info())

# Function to display head of the dataset
def display_head(data):
    st.write("### Dataset Head")
    st.write(data.head())

# Function to display basic statistics
def display_statistics(data):
    st.write("### Basic Statistics")
    st.write(data.describe())

# Function to fill missing values
def fill_missing_values(data):
    st.write("### Fill Missing Values")
    filled_data = data.fillna(method='ffill')  # You can use any filling method here
    st.write(filled_data)

# Function to plot histogram
def plot_histogram(data, feature):
    st.write("### Histogram Plot")
    plt.figure(figsize=(8, 6))
    sns.histplot(data[feature], kde=True)
    st.pyplot()

# Function to plot heatmap for feature correlation
def plot_heatmap(data):
    st.write("### Heatmap for Feature Correlation")
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    st.pyplot()

# Main function
def main():
    st.title("Explore Tabular Data")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        
        # Dropdown for data exploration options
        options = ["Display Info", "Display Head", "Display Basic Statistics", "Fill Missing Values", "Histogram Plot", "Heatmap Plot"]
        selected_option = st.selectbox("Select an option:", options)

        # Perform the selected action based on the dropdown choice
        if selected_option == "Display Info":
            #display_info(data)
            st.write("### Dataset Infos")
            st.write(data.info())
        elif selected_option == "Display Head":
            display_head(data)
        elif selected_option == "Display Basic Statistics":
            display_statistics(data)
        elif selected_option == "Fill Missing Values":
            fill_missing_values(data)
        elif selected_option == "Histogram Plot":
            selected_feature = st.selectbox("Select a feature for histogram plot:", data.columns)
            plot_histogram(data, selected_feature)
        elif selected_option == "Heatmap Plot":
            plot_heatmap(data)

# Run the app
if __name__ == "__main__":
    main()
