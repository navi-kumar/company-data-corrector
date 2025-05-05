import streamlit as st
import pandas as pd
import io
import time
from company_utils import correct_company_name, get_company_info, process_company_batch

# Page configuration
st.set_page_config(
    page_title="Company Data Corrector",
    page_icon="🏢",
    layout="wide"
)

# Header with image
st.image("https://images.unsplash.com/photo-1523961131990-5ea7c61b2107", use_column_width=True)
st.title("Company Data Corrector")
st.markdown("Correct company names and retrieve industry information and LinkedIn URLs using fuzzy matching")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["Single Company", "Bulk Upload"])

with tab1:
    st.header("Single Company Correction")
    st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40", use_column_width=True)
    
    # Single company input
    company_name = st.text_input("Enter a company name:", placeholder="e.g., Googl")
    
    if company_name:
        with st.spinner("Processing company information..."):
            # Process the company name
            corrected_name, match_score = correct_company_name(company_name)
            industry, linkedin_url = get_company_info(corrected_name)
            
            # Create a DataFrame for display
            data = {
                "Input Name": [company_name],
                "Corrected Name": [corrected_name],
                "Match Confidence": [f"{match_score:.1f}%"],
                "Industry": [industry],
                "LinkedIn URL": [linkedin_url]
            }
            df = pd.DataFrame(data)
            
            # Display the result
            st.subheader("Result")
            st.dataframe(df, use_container_width=True)
            
            # Add a hyperlink to the LinkedIn URL
            if linkedin_url:
                st.markdown(f"[View {corrected_name} on LinkedIn]({linkedin_url})")

with tab2:
    st.header("Bulk Company Correction")
    st.image("https://images.unsplash.com/photo-1526628953301-3e589a6a8b74", use_column_width=True)
    
    # File upload
    st.markdown("Upload a CSV or Excel file with a column named 'Company' containing company names.")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])
    
    if uploaded_file is not None:
        try:
            # Determine file type and read accordingly
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            # Check if 'Company' column exists
            if 'Company' not in df.columns:
                st.error("The uploaded file must contain a column named 'Company'.")
            else:
                # Display preview of uploaded data
                st.subheader("Preview of uploaded data")
                st.dataframe(df.head(), use_container_width=True)
                
                # Extract company names
                company_names = df['Company'].tolist()
                
                # Limit to 200 companies
                if len(company_names) > 200:
                    st.warning("Only the first 200 companies will be processed. The file contains " + str(len(company_names)) + " companies.")
                    company_names = company_names[:200]
                
                # Process button
                if st.button(f"Process {len(company_names)} Companies"):
                    with st.spinner("Processing companies..."):
                        # Create a progress bar
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Process the companies
                        result_df = process_company_batch(company_names, progress_bar, status_text)
                        
                        # Display the results
                        st.subheader("Results")
                        st.dataframe(result_df, use_container_width=True)
                        
                        # Provide download link
                        csv = result_df.to_csv(index=False)
                        excel_buffer = io.BytesIO()
                        result_df.to_excel(excel_buffer, index=False, engine='openpyxl')
                        excel_data = excel_buffer.getvalue()
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.download_button(
                                label="Download as CSV",
                                data=csv,
                                file_name="corrected_companies.csv",
                                mime="text/csv"
                            )
                        with col2:
                            st.download_button(
                                label="Download as Excel",
                                data=excel_data,
                                file_name="corrected_companies.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )
        
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

# Footer with additional information
st.markdown("---")
st.markdown("""
**How it works:**
1. Enter a company name or upload a file with company names
2. Our system uses fuzzy matching to identify the correct company name
3. We retrieve industry information and LinkedIn URLs
4. Results are displayed in a table and can be downloaded
""")

# Data visualization image at bottom
st.image("https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a", use_column_width=True)
