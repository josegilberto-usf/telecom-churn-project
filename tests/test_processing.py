import pandas as pd
import pytest
from src.processing import clean_telecom_data

def test_clean_telecom_data_handles_blanks():
    """
    Test that empty strings in TotalCharges are converted to 0.
    """
    # 1. Setup: Create a "fake" tiny dataframe with a blank space
    data = {'TotalCharges': [" ", "100.5"]}
    df_fake = pd.DataFrame(data)
    
    # 2. Action: Run our cleaning function
    df_result = clean_telecom_data(df_fake)
    
    # 3. Assert: Check if the first value is now 0.0 (float)
    # Rationale: This 'assert' is the heartbeat of the test. 
    # If this isn't true, the test fails.
    assert df_result['TotalCharges'][0] == 0.0
    assert df_result['TotalCharges'].dtype == 'float64'