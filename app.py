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

# Function to display correlation heatmap with user-defined options
def display_correlation_heatmap(data, show_annotation, figure_size):
    st.write("### Correlation Heatmap")
    numerical_cols = data.select_dtypes(include=['float64', 'int64'])
    corr_matrix = numerical_cols.corr()
    plt.figure(figsize=figure_size)
    sns.heatmap(corr_matrix, annot=show_annotation, cmap='coolwarm', fmt=".2f", linewidths=.5)
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
        # Options for the correlation heatmap
        show_annotation = st.checkbox("Show Annotation", value=True)
        figure_size = st.slider("Figure Size", min_value=5, max_value=20, value=10, step=1)
        display_correlation_heatmap(data, show_annotation, (figure_size, figure_size))

# Run the app
if __name__ == "__main__":
    main()
