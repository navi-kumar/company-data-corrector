import pandas as pd
import time
from rapidfuzz import process, fuzz
from companies_db import get_company_database

# Get the company database
company_db = get_company_database()

def correct_company_name(input_name):
    """
    Uses fuzzy matching to correct a company name
    
    Args:
        input_name (str): The potentially incorrect company name
        
    Returns:
        tuple: (corrected_name, match_score)
    """
    if not input_name or input_name.strip() == "":
        return ("", 0)
    
    # Get all company names from the database
    company_names = list(company_db.keys())
    
    # Find the best match using fuzzy matching
    best_match, score, _ = process.extractOne(
        input_name, 
        company_names, 
        scorer=fuzz.token_sort_ratio
    )
    
    return (best_match, score)

def get_company_info(company_name):
    """
    Retrieves industry and LinkedIn URL for a company
    
    Args:
        company_name (str): The corrected company name
        
    Returns:
        tuple: (industry, linkedin_url)
    """
    if company_name in company_db:
        return (company_db[company_name]["industry"], company_db[company_name]["linkedin"])
    else:
        return ("Unknown", "")

def process_company_batch(company_names, progress_bar=None, status_text=None):
    """
    Process a batch of company names
    
    Args:
        company_names (list): List of company names to process
        progress_bar: Streamlit progress bar
        status_text: Streamlit text element for status updates
        
    Returns:
        DataFrame: Results with corrected names, industries, and LinkedIn URLs
    """
    results = []
    total = len(company_names)
    
    for i, name in enumerate(company_names):
        # Update progress
        if progress_bar is not None:
            progress_bar.progress((i + 1) / total)
        if status_text is not None:
            status_text.text(f"Processing company {i + 1} of {total}: {name}")
        
        # Process the company
        corrected_name, match_score = correct_company_name(name)
        industry, linkedin_url = get_company_info(corrected_name)
        
        # Add to results
        results.append({
            "Input Name": name,
            "Corrected Name": corrected_name,
            "Match Confidence": f"{match_score:.1f}%",
            "Industry": industry,
            "LinkedIn URL": linkedin_url
        })
        
        # Add a small delay to simulate processing time (can be removed in production)
        time.sleep(0.1)
    
    if status_text is not None:
        status_text.text("Processing complete!")
    
    return pd.DataFrame(results)
