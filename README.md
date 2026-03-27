# Telecom Customer Churn Pipeline

## Project Overview
This project identifies high-risk customers for a telecommunications provider using the IBM Telco Churn dataset. 

## Business Insights
* **Overall Churn Rate:** ~26.5%
* **Key Finding:** Month-to-month customers churn at 42.7%, compared to only 2.8% for Two-year contracts.

## Project Structure
* `src/`: Core logic for data loading, cleaning, and encoding.
* `tests/`: Automated unit tests using `pytest`.
* `data/`: Raw dataset (CSV).
* `main.py`: The orchestrator for the entire pipeline.

## How to Run
1. Activate virtual environment: `source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Execute pipeline: `python3 main.py`
4. Run tests: `pytest`