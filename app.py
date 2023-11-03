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

# Function to display basic statistics
def display_statistics(data):
    st.write("### Basic Statistics")
    st.write(data.describe())

# Function to display correlation heatmap with user-defined options
def display_correlation_heatmap(data):
    st.write("### Correlation Heatmap")
    # Options for the correlation heatmap
    show_annotation = st.checkbox("Show Annotation", value=True)
    figure_size = st.slider("Figure Size", min_value=5, max_value=20, value=10, step=1)
    numerical_cols = data.select_dtypes(include=['float64', 'int64'])
    corr_matrix = numerical_cols.corr()
    plt.figure(figsize=(figure_size,figure_size))
    sns.heatmap(corr_matrix, annot=show_annotation, cmap='coolwarm', fmt=".2f", linewidths=.5)
    st.pyplot(plt)

# Function to display histogram of selected column
def display_histogram(data):
    st.write("### Histogram of Selected Column")
    column_name = st.selectbox("Select a column:", data.columns)
    plt.figure(figsize=(8, 6))
    plt.hist(data[column_name], bins=30, color='skyblue', edgecolor='black')
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {column_name}")
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
    options = ["Display Data", "Display Basic Statistics", 
               "Display Correlation Heatmap", "Display Histogram"]
    selected_option = st.selectbox("Select an option:", options)

    # Perform the selected action based on the dropdown choice
    if selected_option == "Display Data":
        display_dataframe(data)
    elif selected_option == "Display Basic Statistics":
        display_statistics(data)
    elif selected_option == "Display Correlation Heatmap":
        display_correlation_heatmap(data)
    elif selected_option == "Display Histogram":
        display_histogram(data)

# Run the app
if __name__ == "__main__":
    main()
