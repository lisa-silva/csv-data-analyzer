# This Streamlit application analyzes uploaded CSV files.

import streamlit as st
import pandas as pd
import io

# --- Configuration ---
st.set_page_config(
    page_title="CSV Data Analyzer (Pandas Dashboard)",
    layout="wide"
)

# --- Title and Uploader (Always visible to prevent blank page) ---
st.title("📊 CSV Data Analyzer")
st.markdown("Upload a CSV file to instantly analyze its structure, statistics, and column data.")

uploaded_file = st.file_uploader(
    "Choose a CSV file:", 
    type=["csv"],
    help="The file should be comma-separated, like a spreadsheet export."
)

# --- Main Analysis Logic ---
if uploaded_file is not None:
    try:
        # Read the file from the uploader into a Pandas DataFrame
        data = pd.read_csv(uploaded_file)
        
        st.success("File uploaded and read successfully!")

        st.header("1. Data Overview")
        st.markdown(f"**Total Rows:** {len(data)}")
        st.markdown(f"**Total Columns:** {len(data.columns)}")
        st.markdown("---")
        
        # Display the first few rows of the data
        st.subheader("First 5 Rows")
        st.dataframe(data.head())
        
        # Display column information
        st.subheader("Column Data Types")
        col_info = pd.DataFrame(data.dtypes, columns=['Data Type'])
        st.dataframe(col_info)
        
        st.header("2. Descriptive Statistics")
        st.markdown("Summary statistics for all numerical columns:")
        st.dataframe(data.describe())

        st.header("3. Interactive Data Visualizer")
        
        # --- Interactive Plotting Section ---
        
        numerical_cols = data.select_dtypes(include=['number']).columns.tolist()
        
        if numerical_cols:
            col1, col2 = st.columns(2)
            
            with col1:
                # Select a column for plotting
                selected_column = st.selectbox(
                    "Select a column to visualize:",
                    numerical_cols
                )
            
            with col2:
                # Select plot type
                plot_type = st.selectbox(
                    "Select plot type:",
                    ["Histogram", "Box Plot"]
                )

            # Generate the chart based on user selection
            st.subheader(f"Visualization: {selected_column}")
            
            if plot_type == "Histogram":
                st.bar_chart(data[selected_column])
            elif plot_type == "Box Plot":
                # Using Streamlit's simple plotting for a box plot representation
                st.area_chart(data[selected_column])
        else:
            st.info("No numerical columns found for plotting.")

    except Exception as e:
        st.error(f"An error occurred during file processing: {e}")

# This message appears when no file is uploaded
else:
    st.info("Upload a CSV file above to begin analysis.")
