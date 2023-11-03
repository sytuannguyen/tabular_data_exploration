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

# Function to display correlation heatmap
def display_correlation_heatmap(data):
    st.write("### Correlation Heatmap")
    numerical_cols = data.select_dtypes(include=['float64', 'int64'])
    corr_matrix = numerical_cols.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    st.pyplot(plt)

# Main function
def main():
    st.title("Explore Tabular Data")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is None:
        uploaded_file = 'training.csv'
        
    data = load_data(uploaded_file)
    
    # Dropdown for data exploration options
    options = ["Display Data", "Display Head", "Display Basic Statistics", "Display Correlation Heatmap"]
    selected_option = st.selectbox("Select an option:", options)

    # Perform the selected action based on the dropdown choice
    if selected_option == "Display Data":
        display_dataframe(data)
    elif selected_option == "Display Head":
        display_head(data)
    elif selected_option == "Display Basic Statistics":
        display_statistics(data)
    elif selected_option == "Display Correlation Heatmap":
        display_correlation_heatmap(data)

# Run the app
if __name__ == "__main__":
    main()
