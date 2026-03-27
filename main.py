from src.processing import load_telecom_data, clean_telecom_data, get_churn_summary, get_contract_churn_analysis, prepare_for_modeling, save_churn_chart

def run_pipeline():
    """
    The orchestrator: Loads, cleans, summarizes, and visualizes the data.
    """
    data_path = "data/raw_churn_data.csv"
    print("--- Starting Telecom Churn Pipeline ---")
    
    try:
        # Step A: Load
        df_raw = load_telecom_data(data_path)
        
        # Step B: Clean
        df_clean = clean_telecom_data(df_raw)
        
        # Step C: Basic Stats
        print(f"Verification - TotalCharges Type: {df_clean['TotalCharges'].dtype}")
        
        # Step D: Churn Analysis
        churn_pct = get_churn_summary(df_clean)
        print("\n--- OVERALL CHURN RATE ---")
        print(churn_pct)
        
        # Step E: Contract Analysis
        contract_analysis = get_contract_churn_analysis(df_clean)
        print("\n--- CHURN BY CONTRACT TYPE ---")
        print(contract_analysis)

        # Step F: Visualization (The missing piece!)
        # Rationale: This actually triggers the chart-saving logic.
        save_churn_chart(contract_analysis)

        # Step G: AI Prep
        df_final = prepare_for_modeling(df_clean)
        print("\n--- AI-READY DATA PREVIEW ---")
        print(df_final.filter(like='Contract_').head())

    except Exception as e:
        # Rationale: This is the mandatory "safety net" for the try block.
        print(f"CRITICAL ERROR: {e}")

if __name__ == "__main__":
    run_pipeline()