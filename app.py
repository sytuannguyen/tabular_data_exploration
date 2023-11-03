import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load CSV file
def load_data(file):
    data = pd.read_csv(file)
    return data

# Function to fill missing values based on user-selected strategy
def fill_missing_values(data, fill_strategy):
    if fill_strategy == "Constant":
        constant_value = st.number_input("Enter constant value to fill missing values", value=0)
        numerical_cols = data.select_dtypes(include=['float64', 'int64'])
        filled_numerical_cols = numerical_cols.fillna(constant_value)
        data_filled = data.copy()
        data_filled[numerical_cols.columns] = filled_numerical_cols
    elif fill_strategy == "Mean":
        numerical_cols = data.select_dtypes(include=['float64', 'int64'])
        filled_numerical_cols = numerical_cols.fillna(numerical_cols.mean())
        data_filled = data.copy()
        data_filled[numerical_cols.columns] = filled_numerical_cols
    elif fill_strategy == "Most Frequent":
        data_filled = data.fillna(data.mode().iloc[0])
    else:
        data_filled = data.copy()
    return data_filled

# Function to display the dataset with missing values filled
def display_dataframe(data):
    st.write("### Show the data")
    st.dataframe(data)
    
    # Display shape of the dataframe and number of missing values in each column
    st.write(f"#### Dataframe Shape: {data.shape}")
    missing_counts = data.isnull().sum().sort_values()
    st.write("#### Number of Missing Values in Each Column:")
    st.write(missing_counts)

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
    
    # Checkbox for each column to include in the heatmap
    selected_columns = st.multiselect("Select columns for the heatmap:", numerical_cols.columns.tolist(), default=numerical_cols.columns.tolist())
    
    # Filter data based on selected columns
    selected_data = numerical_cols[selected_columns]
    corr_matrix = selected_data.corr()
    
    # Color customization
    heatmap_color = st.color_picker("Select heatmap color", value='#3498db')
    
    plt.figure(figsize=(figure_size, figure_size))
    sns.heatmap(corr_matrix, annot=show_annotation, cmap=heatmap_color, fmt=".2f", linewidths=.5)
    st.pyplot(plt)

# Function to display histogram of selected column
def display_histogram(data):
    st.write("### Histogram of Selected Column")
    column_name = st.selectbox("Select a column:", data.columns)
    histogram_color = st.color_picker("Select histogram color", value='#3498db')
    plt.figure(figsize=(8, 6))
    plt.hist(data[column_name], bins=30, color=histogram_color, edgecolor='black')
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {column_name}")
    st.pyplot(plt)

# Function to display cross plot between selected columns
def display_cross_plot(data):
    st.write("### Cross Plot")
    x_column = st.selectbox("Select X-axis column:", data.columns)
    y_column = st.selectbox("Select Y-axis column:", data.columns)
    scatterplot_color = st.color_picker("Select scatter plot color", value='#3498db')
    plt.figure(figsize=(8, 6))
    plt.scatter(data[x_column], data[y_column], color=scatterplot_color)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"Cross Plot between {x_column} and {y_column}")
    st.pyplot(plt)

# Main function
def main():
    st.title("Explore Tabular Data")
    # Subtitle showing author name and institution
    st.markdown("**Dr. Tuan Nguyen-Sy** ")
    st.markdown("<font color='gray'>Institute for Computational Science and Artificial Intelligence, Van Lang University</font>", unsafe_allow_html=True)

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is None:
        uploaded_file = 'training.csv'
        
    data = load_data(uploaded_file)
    
    # Dropdown for data exploration options
    options = ["Display Data", "Display Basic Statistics", 
               "Display Correlation Heatmap", "Display Histogram", "Display Cross Plot"]
    selected_option = st.selectbox("Select an option:", options)
    
    # Dropdown for selecting missing value filling strategy
    fill_strategy = st.selectbox("Select missing value filling strategy:", ["None", "Constant", "Mean", "Most Frequent"])
    
    # Fill missing values based on user-selected strategy
    if fill_strategy != "None":
        data = fill_missing_values(data, fill_strategy)

    # Perform the selected action based on the dropdown choice
    if selected_option == "Display Data":
        display_dataframe(data)
    elif selected_option == "Display Basic Statistics":
        display_statistics(data)
    elif selected_option == "Display Correlation Heatmap":
        display_correlation_heatmap(data)
    elif selected_option == "Display Histogram":
        display_histogram(data)
    elif selected_option == "Display Cross Plot":
        display_cross_plot(data)

# Run the app
if __name__ == "__main__":
    main()
