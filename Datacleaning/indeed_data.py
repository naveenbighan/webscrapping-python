import pandas as pd
import random 
import numpy as np

df =pd.read_csv("indeed1_jobs.csv")
df.drop_duplicates(inplace=True)
pd.options.display.max_rows=50999
type_list = ['part-time', 'Full-time', 'Permanent', 'Internship']

# Fill NaN values in the 'type' column with random choices from type_list
df['type'] = df['type'].apply(lambda x: random.choice(type_list) if pd.isna(x) else x)

salary_range =(30000, 100000)

# Fill NaN values with random numbers within the salary range
df['salary_package'] = df['salary_package'].apply(
    lambda x:f" {np.random.randint(salary_range[0], salary_range[1]) if pd.isna(x) else x}"
    
)
import re

# Function to add '₹' if not already present
def add_currency_symbol(value):
    # Check if '₹' is already present in the value using regex
    if isinstance(value, str) and re.search(r'₹', value):
        return value  # Return as is if '₹' is already present
    else:
        # Convert numerical values and add '₹' in front, while formatting with commas
        return f"₹{int(value):,}" if pd.notna(value) else '₹0'

# Apply the function to the salary_package column
df['salary_package'] = df['salary_package'].apply(add_currency_symbol)
print(df['salary_package'])


