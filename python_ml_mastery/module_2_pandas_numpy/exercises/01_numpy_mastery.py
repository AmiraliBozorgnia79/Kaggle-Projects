"""
Module 2 - Exercise 1: NumPy Array Mastery
==========================================

Complete each exercise without using AI assistance. 
Focus on understanding the underlying concepts and performance implications.

Run this file with: python 01_numpy_mastery.py
"""

import numpy as np
import time
from typing import Tuple, List


def exercise_1_array_creation():
    """
    Exercise 1: Array Creation and Basic Operations
    
    TODO: Complete the following tasks:
    1. Create a 1D array with numbers 0 to 99
    2. Create a 3x3 matrix filled with zeros
    3. Create a 5x5 identity matrix
    4. Create a random array of shape (4, 6) with values between 0 and 1
    5. Create an array with evenly spaced values from 0 to 10 (20 points)
    """
    print("=== Exercise 1: Array Creation ===")
    
    # TODO: Your code here
    # arr_1d = 
    # zeros_matrix = 
    # identity_matrix = 
    # random_array = 
    # linspace_array = 
    
    # Test your arrays (uncomment when ready)
    # print(f"1D array shape: {arr_1d.shape}")
    # print(f"Zeros matrix:\n{zeros_matrix}")
    # print(f"Identity matrix:\n{identity_matrix}")
    # print(f"Random array shape: {random_array.shape}")
    # print(f"Linspace array: {linspace_array}")


def exercise_2_indexing_slicing():
    """
    Exercise 2: Advanced Indexing and Slicing
    
    TODO: Complete the following tasks:
    1. Create a 6x6 array with values 1-36
    2. Extract the middle 4x4 subarray
    3. Extract every second row and every second column
    4. Use boolean indexing to get values > 20
    5. Use fancy indexing to get specific rows [0, 2, 4]
    """
    print("\n=== Exercise 2: Indexing and Slicing ===")
    
    # TODO: Your code here
    # arr = np.arange(1, 37).reshape(6, 6)
    # middle_subarray = 
    # every_second = 
    # boolean_mask = 
    # fancy_indexed = 
    
    # Test your results (uncomment when ready)
    # print(f"Original array:\n{arr}")
    # print(f"Middle 4x4:\n{middle_subarray}")
    # print(f"Every second:\n{every_second}")
    # print(f"Values > 20: {boolean_mask}")
    # print(f"Rows [0,2,4]:\n{fancy_indexed}")


def exercise_3_mathematical_operations():
    """
    Exercise 3: Mathematical Operations and Broadcasting
    
    TODO: Complete the following tasks:
    1. Create two arrays: a (3x4) and b (1x4)
    2. Add them using broadcasting
    3. Calculate element-wise square root of the result
    4. Calculate the dot product of a with its transpose
    5. Find the mean along different axes
    """
    print("\n=== Exercise 3: Mathematical Operations ===")
    
    # TODO: Your code here
    # a = np.random.randint(1, 10, (3, 4))
    # b = np.random.randint(1, 5, (1, 4))
    # broadcast_result = 
    # sqrt_result = 
    # dot_product = 
    # mean_axis0 = 
    # mean_axis1 = 
    
    # Test your results (uncomment when ready)
    # print(f"Array a:\n{a}")
    # print(f"Array b:\n{b}")
    # print(f"Broadcasting result:\n{broadcast_result}")
    # print(f"Square root:\n{sqrt_result}")
    # print(f"Dot product shape: {dot_product.shape}")


def exercise_4_performance_comparison():
    """
    Exercise 4: Performance Analysis
    
    TODO: Compare the performance of:
    1. Pure Python loop vs NumPy operations
    2. Different ways to calculate matrix multiplication
    3. Memory usage of different data types
    """
    print("\n=== Exercise 4: Performance Comparison ===")
    
    # Setup data
    size = 1000
    a = np.random.random(size)
    b = np.random.random(size)
    
    # TODO: Implement pure Python version
    def python_dot_product(x: List[float], y: List[float]) -> float:
        """Calculate dot product using pure Python"""
        # Your implementation here
        pass
    
    # TODO: Time both approaches
    # Convert to list for Python version
    a_list = a.tolist()
    b_list = b.tolist()
    
    # Time pure Python
    # start_time = time.time()
    # python_result = python_dot_product(a_list, b_list)
    # python_time = time.time() - start_time
    
    # Time NumPy
    # start_time = time.time()
    # numpy_result = np.dot(a, b)
    # numpy_time = time.time() - start_time
    
    # print(f"Python time: {python_time:.6f} seconds")
    # print(f"NumPy time: {numpy_time:.6f} seconds")
    # print(f"Speed improvement: {python_time/numpy_time:.2f}x")


def exercise_5_real_world_application():
    """
    Exercise 5: Real-world Application - Sensor Data Processing
    
    Simulate processing sensor data for a monitoring system.
    
    TODO: Complete the following tasks:
    1. Generate simulated sensor data (temperature, humidity, pressure)
    2. Calculate rolling averages
    3. Detect anomalies (values beyond 2 standard deviations)
    4. Create summary statistics
    """
    print("\n=== Exercise 5: Real-world Application ===")
    
    # TODO: Generate sensor data
    np.random.seed(42)  # For reproducible results
    n_readings = 1000
    
    # Temperature: normal around 20°C, std=5
    # temperature = 
    
    # Humidity: normal around 60%, std=10
    # humidity = 
    
    # Pressure: normal around 1013 hPa, std=20
    # pressure = 
    
    # TODO: Calculate rolling averages (window size 10)
    def rolling_average(data: np.ndarray, window: int) -> np.ndarray:
        """Calculate rolling average"""
        # Your implementation here
        pass
    
    # TODO: Detect anomalies
    def detect_anomalies(data: np.ndarray) -> np.ndarray:
        """Return boolean array marking anomalies (>2 std from mean)"""
        # Your implementation here
        pass
    
    # TODO: Apply functions and print results
    # temp_rolling = rolling_average(temperature, 10)
    # temp_anomalies = detect_anomalies(temperature)
    
    # print(f"Temperature anomalies detected: {np.sum(temp_anomalies)}")
    # print(f"Average temperature: {np.mean(temperature):.2f}°C")
    # print(f"Temperature range: {np.min(temperature):.2f}°C to {np.max(temperature):.2f}°C")


def bonus_challenge():
    """
    Bonus Challenge: Advanced NumPy
    
    TODO: Implement these advanced operations:
    1. Custom universal function (ufunc)
    2. Structured arrays for heterogeneous data
    3. Memory-mapped arrays for large datasets
    """
    print("\n=== Bonus Challenge ===")
    
    # TODO: Create a custom ufunc for normalized difference
    # def normalized_difference(a, b):
    #     return (a - b) / (a + b)
    
    # vectorized_norm_diff = np.vectorize(normalized_difference)
    
    # TODO: Create structured array for mixed data types
    # dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('salary', 'f8')])
    # employees = np.array([...], dtype=dt)
    
    print("Bonus exercises - implement when ready!")


if __name__ == "__main__":
    print("NumPy Mastery Exercises")
    print("=" * 50)
    print("Complete each exercise step by step.")
    print("Focus on understanding concepts, not just getting results.\n")
    
    exercise_1_array_creation()
    exercise_2_indexing_slicing()
    exercise_3_mathematical_operations()
    exercise_4_performance_comparison()
    exercise_5_real_world_application()
    bonus_challenge()
    
    print("\n" + "=" * 50)
    print("Great job! Move on to the next exercise when ready.")
    print("Remember: Understanding > Completion Speed")