import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate large dummy dataset (100,000 records)
n_records = 100000

print(f"Generating dataset with {n_records:,} records...")

# Generate data
data = {
    'employee_id': range(1, n_records + 1),
    'first_name': [random.choice(['John', 'Jane', 'Michael', 'Sarah', 'David', 'Emily', 'Robert', 'Lisa', 'James', 'Maria', 'William', 'Jennifer', 'Richard', 'Patricia', 'Charles', 'Linda', 'Thomas', 'Barbara', 'Christopher', 'Elizabeth']) for _ in range(n_records)],
    'last_name': [random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin']) for _ in range(n_records)],
    'department': np.random.choice(['Engineering', 'Sales', 'Marketing', 'Finance', 'HR', 'Operations', 'IT', 'Legal'], n_records, p=[0.25, 0.2, 0.15, 0.15, 0.1, 0.05, 0.05, 0.05]),
    'job_title': np.random.choice(['Manager', 'Senior', 'Junior', 'Lead', 'Director', 'Analyst', 'Specialist', 'Coordinator'], n_records),
    'salary': np.random.normal(75000, 25000, n_records).astype(int),
    'age': np.random.randint(22, 65, n_records),
    'years_experience': np.random.randint(0, 40, n_records),
    'performance_score': np.random.uniform(1.0, 5.0, n_records).round(2),
    'bonus_percentage': np.random.uniform(0, 20, n_records).round(2),
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'], n_records),
    'state': np.random.choice(['NY', 'CA', 'IL', 'TX', 'AZ', 'PA'], n_records),
    'hire_date': [datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1460)) for _ in range(n_records)],
    'is_remote': np.random.choice([True, False], n_records, p=[0.3, 0.7]),
    'education_level': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_records, p=[0.2, 0.5, 0.25, 0.05]),
    'project_count': np.random.poisson(3, n_records),
    'customer_satisfaction': np.random.uniform(1.0, 10.0, n_records).round(1)
}

# Create DataFrame
df = pd.DataFrame(data)

# Ensure salary is positive and reasonable
df['salary'] = np.abs(df['salary'])
df['salary'] = np.where(df['salary'] < 30000, 30000, df['salary'])

print(f'Generated dataset with {len(df):,} records and {len(df.columns)} columns')
print(f'Dataset shape: {df.shape}')
print(f'Memory usage: {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB')

# Save as CSV
print('Saving as CSV...')
df.to_csv('employee_data.csv', index=False)

# Save as Parquet
print('Saving as Parquet...')
df.to_parquet('employee_data.parquet', index=False)

# Get file sizes
csv_size = os.path.getsize('employee_data.csv') / 1024 / 1024
parquet_size = os.path.getsize('employee_data.parquet') / 1024 / 1024

print('Files created successfully!')
print(f'CSV file size: {csv_size:.2f} MB')
print(f'Parquet file size: {parquet_size:.2f} MB')
print(f'Parquet is {csv_size/parquet_size:.1f}x smaller than CSV')

# Display sample data
print('\n' + '='*50)
print('SAMPLE DATA:')
print('='*50)
print(df.head(10))

print('\n' + '='*50)
print('DATA TYPES:')
print('='*50)
print(df.dtypes)

print('\n' + '='*50)
print('BASIC STATISTICS:')
print('='*50)
print(df.describe())

print('\n' + '='*50)
print('DEPARTMENT DISTRIBUTION:')
print('='*50)
print(df['department'].value_counts())