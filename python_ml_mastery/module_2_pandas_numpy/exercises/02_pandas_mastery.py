"""
Module 2 - Exercise 2: Pandas Mastery
=====================================

Master pandas operations for real-world data manipulation and analysis.
Focus on efficiency, readability, and practical applications.

Run this file with: python 02_pandas_mastery.py
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
from typing import Dict, List, Any


def exercise_1_dataframe_basics():
    """
    Exercise 1: DataFrame Creation and Basic Operations
    
    TODO: Complete the following tasks:
    1. Create a DataFrame from a dictionary
    2. Set and reset index
    3. Select columns and rows using different methods
    4. Add new calculated columns
    5. Handle basic data types
    """
    print("=== Exercise 1: DataFrame Basics ===")
    
    # Sample data for a monitoring system
    data = {
        'timestamp': pd.date_range('2024-01-01', periods=100, freq='1H'),
        'server_id': np.random.choice(['srv-001', 'srv-002', 'srv-003'], 100),
        'cpu_usage': np.random.normal(50, 15, 100),
        'memory_usage': np.random.normal(60, 20, 100),
        'disk_io': np.random.exponential(10, 100),
        'network_traffic': np.random.gamma(2, 5, 100)
    }
    
    # TODO: Create DataFrame and explore
    # df = pd.DataFrame(data)
    
    # TODO: Basic operations
    # 1. Set timestamp as index
    # 2. Display basic info about the DataFrame
    # 3. Calculate a new column: total_load = cpu_usage + memory_usage
    # 4. Select high usage periods (cpu_usage > 70)
    
    # Test your code (uncomment when ready)
    # print(f"DataFrame shape: {df.shape}")
    # print(f"Column types:\n{df.dtypes}")
    # print(f"High CPU usage periods: {len(df[df['cpu_usage'] > 70])}")


def exercise_2_data_cleaning():
    """
    Exercise 2: Data Cleaning and Preprocessing
    
    TODO: Complete the following tasks:
    1. Handle missing values with different strategies
    2. Remove duplicates
    3. Convert data types appropriately
    4. Handle outliers
    5. Standardize string data
    """
    print("\n=== Exercise 2: Data Cleaning ===")
    
    # Create messy data (typical real-world scenario)
    np.random.seed(42)
    dirty_data = {
        'user_id': ['USR_001', 'usr_002', 'USR_003', 'usr_002', 'USR_004', 'usr_005'],
        'email': ['user1@test.com', 'USER2@TEST.COM', 'user3@test.com', 
                 'USER2@TEST.COM', None, 'user5@invalid'],
        'age': [25, 30, None, 30, 45, 999],  # 999 is an outlier
        'signup_date': ['2024-01-15', '2024/01/20', '2024-01-25', 
                       '2024/01/20', '2024-02-01', 'invalid_date'],
        'plan': ['Basic', 'PREMIUM', 'basic', 'Premium', 'Enterprise', '']
    }
    
    # TODO: Create DataFrame and clean it
    # df_dirty = pd.DataFrame(dirty_data)
    
    # TODO: Cleaning steps
    # 1. Standardize user_id format (all uppercase)
    # 2. Handle missing emails (maybe forward fill or drop)
    # 3. Convert age outliers (999) to NaN and handle appropriately
    # 4. Convert signup_date to datetime, handle invalid dates
    # 5. Standardize plan names (title case)
    # 6. Remove duplicate rows
    
    # Test your cleaning (uncomment when ready)
    # print("Before cleaning:")
    # print(df_dirty)
    # print("\nAfter cleaning:")
    # print(df_cleaned)


def exercise_3_groupby_aggregation():
    """
    Exercise 3: GroupBy Operations and Aggregation
    
    TODO: Complete the following tasks:
    1. Group by categorical variables
    2. Apply multiple aggregation functions
    3. Create custom aggregation functions
    4. Pivot tables and cross-tabulations
    5. Transform and filter groups
    """
    print("\n=== Exercise 3: GroupBy and Aggregation ===")
    
    # Generate sales data
    np.random.seed(42)
    n_records = 1000
    
    sales_data = {
        'date': pd.date_range('2024-01-01', periods=n_records, freq='D'),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_records),
        'product': np.random.choice(['Product_A', 'Product_B', 'Product_C'], n_records),
        'salesperson': np.random.choice([f'Sales_{i:02d}' for i in range(1, 11)], n_records),
        'revenue': np.random.gamma(2, 1000, n_records),
        'units_sold': np.random.poisson(10, n_records)
    }
    
    # TODO: Create DataFrame and perform aggregations
    # sales_df = pd.DataFrame(sales_data)
    
    # TODO: Aggregation tasks
    # 1. Total revenue by region
    # 2. Average units sold by product and region
    # 3. Top 5 salespeople by total revenue
    # 4. Monthly revenue trends
    # 5. Custom aggregation: calculate profit margin (assume cost = 60% of revenue)
    
    # TODO: Pivot table
    # Create a pivot table showing revenue by region and product
    
    # Test your aggregations (uncomment when ready)
    # print("Revenue by region:")
    # print(revenue_by_region)
    
    # print("\nTop salespeople:")
    # print(top_salespeople)


def exercise_4_time_series_operations():
    """
    Exercise 4: Time Series Data Handling
    
    TODO: Complete the following tasks:
    1. Work with datetime index
    2. Resample time series data
    3. Rolling window calculations
    4. Handle time zones
    5. Extract time-based features
    """
    print("\n=== Exercise 4: Time Series Operations ===")
    
    # Generate time series sensor data
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 3, 31)
    freq = '5min'  # 5-minute intervals
    
    dates = pd.date_range(start=start_date, end=end_date, freq=freq)
    n_points = len(dates)
    
    # Simulate realistic sensor patterns
    np.random.seed(42)
    base_temp = 20 + 10 * np.sin(2 * np.pi * np.arange(n_points) / (24 * 12))  # Daily cycle
    noise = np.random.normal(0, 2, n_points)
    
    sensor_data = pd.DataFrame({
        'timestamp': dates,
        'temperature': base_temp + noise,
        'humidity': np.random.uniform(30, 90, n_points),
        'pressure': np.random.normal(1013, 10, n_points)
    })
    
    # TODO: Set timestamp as index
    # sensor_data.set_index('timestamp', inplace=True)
    
    # TODO: Time series operations
    # 1. Resample to hourly averages
    # 2. Calculate 24-hour rolling averages
    # 3. Detect missing data periods
    # 4. Extract time-based features (hour, day_of_week, month)
    # 5. Calculate temperature change rate (difference between consecutive readings)
    
    # TODO: Advanced operations
    # 1. Find periods of rapid temperature change (>5°C in 1 hour)
    # 2. Calculate daily temperature range (max - min)
    # 3. Identify outliers using rolling statistics
    
    # Test your time series operations (uncomment when ready)
    # print(f"Original data shape: {sensor_data.shape}")
    # print(f"Hourly resampled shape: {hourly_data.shape}")
    # print(f"Rapid changes detected: {rapid_changes.sum()}")


def exercise_5_merging_joining():
    """
    Exercise 5: Merging, Joining, and Combining DataFrames
    
    TODO: Complete the following tasks:
    1. Inner, outer, left, right joins
    2. Merge on multiple columns
    3. Handle overlapping column names
    4. Concatenate DataFrames
    5. Combine data from different sources
    """
    print("\n=== Exercise 5: Merging and Joining ===")
    
    # Create related datasets (typical in monitoring systems)
    
    # Server information
    servers = pd.DataFrame({
        'server_id': ['srv-001', 'srv-002', 'srv-003', 'srv-004'],
        'datacenter': ['DC-East', 'DC-East', 'DC-West', 'DC-West'],
        'server_type': ['web', 'database', 'web', 'cache'],
        'capacity': [100, 500, 150, 50]
    })
    
    # Performance metrics
    metrics = pd.DataFrame({
        'server_id': ['srv-001', 'srv-001', 'srv-002', 'srv-003', 'srv-005'],
        'metric_time': pd.date_range('2024-01-01', periods=5, freq='1H'),
        'cpu_usage': [45, 52, 78, 33, 67],
        'response_time': [120, 150, 300, 90, 200]
    })
    
    # Alert information
    alerts = pd.DataFrame({
        'server_id': ['srv-002', 'srv-003', 'srv-001'],
        'alert_time': pd.to_datetime(['2024-01-01 02:00', '2024-01-01 03:00', '2024-01-01 04:00']),
        'alert_type': ['high_cpu', 'slow_response', 'disk_full'],
        'severity': ['high', 'medium', 'critical']
    })
    
    # TODO: Merging operations
    # 1. Inner join servers and metrics
    # 2. Left join to include all servers even without metrics
    # 3. Merge alerts with server information
    # 4. Create a comprehensive dashboard dataset
    # 5. Handle the server that appears in metrics but not in servers table
    
    # TODO: Concatenation
    # Create additional metrics for different time periods and concatenate
    
    # Test your merging operations (uncomment when ready)
    # print("Servers with metrics:")
    # print(server_metrics.head())
    
    # print("\nAlert summary:")
    # print(alert_summary)


def exercise_6_performance_optimization():
    """
    Exercise 6: Performance Optimization Techniques
    
    TODO: Complete the following tasks:
    1. Compare different filtering approaches
    2. Optimize memory usage with appropriate data types
    3. Use vectorized operations vs apply
    4. Efficient string operations
    5. Index optimization
    """
    print("\n=== Exercise 6: Performance Optimization ===")
    
    # Create large dataset for performance testing
    np.random.seed(42)
    n_rows = 100000
    
    large_df = pd.DataFrame({
        'id': range(n_rows),
        'category': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
        'value1': np.random.randn(n_rows),
        'value2': np.random.randn(n_rows),
        'text': [f'item_{i}' for i in range(n_rows)],
        'date': pd.date_range('2020-01-01', periods=n_rows, freq='1H')
    })
    
    # TODO: Performance comparisons
    
    # 1. Compare filtering methods
    def method1_query(df):
        return df.query("category == 'A' and value1 > 0")
    
    def method2_boolean(df):
        return df[(df['category'] == 'A') & (df['value1'] > 0)]
    
    def method3_loc(df):
        return df.loc[(df['category'] == 'A') & (df['value1'] > 0)]
    
    # TODO: Time each method
    # methods = [method1_query, method2_boolean, method3_loc]
    # for method in methods:
    #     start_time = time.time()
    #     result = method(large_df)
    #     end_time = time.time()
    #     print(f"{method.__name__}: {end_time - start_time:.4f} seconds")
    
    # TODO: Memory optimization
    # 1. Convert category to categorical data type
    # 2. Optimize numeric types based on value ranges
    # 3. Compare memory usage before and after
    
    # TODO: Vectorized vs apply comparison
    # Calculate a complex transformation and compare approaches
    
    print("Performance optimization exercises - implement timing comparisons!")


def challenge_real_time_data_processor():
    """
    Challenge: Real-time Data Processor Simulation
    
    Create a function that simulates processing streaming data in batches.
    This combines all the skills from previous exercises.
    
    TODO: Implement a data processor that:
    1. Accepts streaming data in batches
    2. Performs data validation and cleaning
    3. Calculates rolling statistics
    4. Detects anomalies
    5. Generates alerts
    6. Maintains performance metrics
    """
    print("\n=== Challenge: Real-time Data Processor ===")
    
    class StreamDataProcessor:
        def __init__(self, window_size: int = 100):
            self.window_size = window_size
            self.data_buffer = pd.DataFrame()
            self.stats = {}
            
        def process_batch(self, batch_data: pd.DataFrame) -> Dict[str, Any]:
            """
            Process a batch of incoming data
            
            Args:
                batch_data: New data batch with columns [timestamp, sensor_id, value]
                
            Returns:
                Dictionary with processing results and alerts
            """
            # TODO: Implement batch processing logic
            # 1. Validate incoming data
            # 2. Add to buffer (keep only last window_size records)
            # 3. Calculate statistics
            # 4. Detect anomalies
            # 5. Generate alerts if needed
            # 6. Return summary
            
            pass
        
        def detect_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
            """Detect anomalies using statistical methods"""
            # TODO: Implement anomaly detection
            # Use z-score or IQR method
            pass
        
        def calculate_stats(self, df: pd.DataFrame) -> Dict[str, float]:
            """Calculate rolling statistics"""
            # TODO: Calculate mean, std, min, max for the current window
            pass
    
    # TODO: Test the processor with simulated streaming data
    # processor = StreamDataProcessor(window_size=50)
    
    # Simulate 10 batches of data
    # for batch_num in range(10):
    #     # Generate batch data
    #     batch = generate_batch_data(batch_num)
    #     result = processor.process_batch(batch)
    #     print(f"Batch {batch_num}: {result}")
    
    print("Implement the StreamDataProcessor class!")


def generate_batch_data(batch_num: int) -> pd.DataFrame:
    """Generate simulated batch data for testing"""
    np.random.seed(batch_num)
    batch_size = 20
    
    return pd.DataFrame({
        'timestamp': pd.date_range(
            start=datetime.now() + timedelta(minutes=batch_num*5),
            periods=batch_size,
            freq='15s'
        ),
        'sensor_id': np.random.choice(['sensor_1', 'sensor_2', 'sensor_3'], batch_size),
        'value': np.random.normal(50, 10, batch_size)
    })


if __name__ == "__main__":
    print("Pandas Mastery Exercises")
    print("=" * 50)
    print("Complete each exercise to master pandas operations.\n")
    
    exercise_1_dataframe_basics()
    exercise_2_data_cleaning()
    exercise_3_groupby_aggregation()
    exercise_4_time_series_operations()
    exercise_5_merging_joining()
    exercise_6_performance_optimization()
    challenge_real_time_data_processor()
    
    print("\n" + "=" * 50)
    print("Excellent work! You're building strong pandas skills.")
    print("Remember: Practice with real data when possible!")
    print("Next: Move on to efficient Python programming patterns.")