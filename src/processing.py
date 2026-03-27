import pandas as pd
import os
import matplotlib.pyplot as plt

def load_telecom_data(file_path: str) -> pd.DataFrame:
    """
    Safely loads the Telco Churn CSV into a Pandas DataFrame.
    
    Args:
        file_path (str): The relative path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded dataset.
        
    Raises:
        FileNotFoundError: If the file does not exist at the given path.
    """
    # Rationale: Checking for file existence prevents the program from 
    # crashing with a confusing 'NoneType' error later.
    if not os.path.exists(file_path):
        print(f"ERROR: File not found at {file_path}")
        raise FileNotFoundError
        
    df = pd.read_csv(file_path)
    
    # Rationale: Business data often has trailing spaces in headers. 
    # Cleaning them now saves hours of debugging later.
    df.columns = [col.strip() for col in df.columns]
    
    return df

def clean_telecom_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the telecom dataframe by fixing data types and handling missing values.
    
    Args:
        df: The raw pandas DataFrame.
        
    Returns:
        pd.DataFrame: A cleaned DataFrame.
    """
    # Rationale: We create a copy so we don't accidentally modify the original 
    # data until we are sure the cleaning worked.
    df_clean = df.copy()

    # Rationale: TotalCharges has empty strings " ". 
    # 'errors=coerce' turns those blanks into 'NaN' (Not a Number) so we can handle them.
    df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')

    # Rationale: If TotalCharges is missing, we'll fill it with 0 for now.
    # In a real business case, we might use the mean or median instead.
    df_clean['TotalCharges'] = df_clean['TotalCharges'].fillna(0)

    return df_clean

def get_churn_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the percentage of customers who stayed vs. left.
    
    Args:
        df: The cleaned DataFrame.
        
    Returns:
        pd.DataFrame: A summary of churn counts and percentages.
    """
    # Rationale: 'value_counts' tells us how many 'Yes' and 'No' are in the Churn column.
    summary = df['Churn'].value_counts(normalize=True) * 100
    
    return summary

def get_contract_churn_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyzes how Churn correlates with Contract types.
    
    Args:
        df: The cleaned DataFrame.
        
    Returns:
        pd.DataFrame: A table showing Churn counts per Contract type.
    """
    # Rationale: 'groupby' splits the data into three buckets: Month-to-month, One year, Two year.
    # We then count how many 'Yes' and 'No' churns are in each bucket.
    analysis = df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack() * 100
    
    return analysis

def prepare_for_modeling(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts categorical text into numbers so an AI can read it.
    
    Args:
        df: The cleaned DataFrame.
        
    Returns:
        pd.DataFrame: A DataFrame with numbers instead of text.
    """
    # Rationale: We only want to encode a few key columns for this example.
    # 'get_dummies' turns "Contract" into three columns: Contract_Month, Contract_OneYear, etc.
    cols_to_encode = ['Contract', 'PaymentMethod', 'InternetService']
    
    df_encoded = pd.get_dummies(df, columns=cols_to_encode)
    
    return df_encoded

def save_churn_chart(analysis_df: pd.DataFrame):
    """
    Creates and saves a bar chart showing Churn by Contract Type.
    """
    # Rationale: We plot the 'Yes' column because that represents the churners.
    analysis_df['Yes'].plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title('Churn Rate by Contract Type')
    plt.ylabel('Churn Percentage (%)')
    plt.tight_layout()
    
    # Rationale: This line physically creates the file in the docs folder.
    plt.savefig('docs/contract_churn_chart.png')
    print("--- SUCCESS: Chart saved to docs/contract_churn_chart.png ---")