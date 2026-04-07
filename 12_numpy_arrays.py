#!/usr/bin/env python3
"""
Creating NumPy Arrays from Python Lists

NumPy (Numerical Python) is a library for numerical computing.
NumPy arrays are the foundation for data analysis in Python.
This script demonstrates creating arrays from Python lists.
"""

import numpy as np


def creating_arrays_from_lists():
    """
    Demonstrate creating NumPy arrays from Python lists.
    """
    print("=" * 70)
    print("CREATING NUMPY ARRAYS FROM PYTHON LISTS")
    print("=" * 70)
    
    # Example 1: Create 1D array from list
    print("\n1. CREATING 1D ARRAY (single dimension)")
    print("-" * 70)
    
    # Python list
    python_list = [1, 2, 3, 4, 5]
    print(f"Python list: {python_list}")
    print(f"Type: {type(python_list)}\n")
    
    # Convert to NumPy array
    numpy_array = np.array(python_list)
    print(f"NumPy array: {numpy_array}")
    print(f"Type: {type(numpy_array)}")
    print(f"Data type: {numpy_array.dtype}")
    print(f"Shape: {numpy_array.shape}")
    print(f"Size: {numpy_array.size}")
    
    # Example 2: Create 2D array from nested list
    print("\n2. CREATING 2D ARRAY (matrix)")
    print("-" * 70)
    
    # Nested Python list (matrix)
    matrix_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Python nested list (matrix):")
    for row in matrix_list:
        print(f"  {row}")
    
    # Convert to 2D array
    matrix_array = np.array(matrix_list)
    print(f"\nNumPy 2D array:")
    print(matrix_array)
    print(f"Shape: {matrix_array.shape}")  # (3, 3)
    print(f"Dimensions: {matrix_array.ndim}")
    
    # Example 3: Create array from mixed data
    print("\n3. CREATING ARRAY FROM MIXED TYPES")
    print("-" * 70)
    
    mixed_list = [1, 2.5, 3, 4.0, 5]
    print(f"Mixed list: {mixed_list}")
    
    mixed_array = np.array(mixed_list)
    print(f"NumPy array: {mixed_array}")
    print(f"Data type (auto-converted): {mixed_array.dtype}")
    
    # Example 4: Specify data type when creating
    print("\n4. SPECIFYING DATA TYPE")
    print("-" * 70)
    
    list_data = [1, 2, 3, 4, 5]
    
    int_array = np.array(list_data, dtype=int)
    print(f"As integer: {int_array}, dtype: {int_array.dtype}")
    
    float_array = np.array(list_data, dtype=float)
    print(f"As float: {float_array}, dtype: {float_array.dtype}")
    
    string_array = np.array(list_data, dtype=str)
    print(f"As string: {string_array}, dtype: {string_array.dtype}")


def numpy_creation_functions():
    """
    Demonstrate NumPy functions for creating arrays.
    """
    print("\n" + "=" * 70)
    print("NUMPY ARRAY CREATION FUNCTIONS")
    print("=" * 70)
    
    # Example 1: arange - similar to range()
    print("\n1. np.arange() - Like range()")
    print("-" * 70)
    
    arr1 = np.arange(5)
    print(f"np.arange(5): {arr1}")
    
    arr2 = np.arange(1, 10, 2)
    print(f"np.arange(1, 10, 2): {arr2}")
    
    # Example 2: linspace - evenly spaced values
    print("\n2. np.linspace() - Evenly spaced values")
    print("-" * 70)
    
    arr3 = np.linspace(0, 10, 5)
    print(f"np.linspace(0, 10, 5): {arr3}")
    
    arr4 = np.linspace(0, 1, 11)
    print(f"np.linspace(0, 1, 11): {arr4}")
    
    # Example 3: zeros - array of zeros
    print("\n3. np.zeros() - Array of zeros")
    print("-" * 70)
    
    zeros_1d = np.zeros(5)
    print(f"np.zeros(5):\n{zeros_1d}")
    
    zeros_2d = np.zeros((3, 4))
    print(f"\nnp.zeros((3, 4)):\n{zeros_2d}")
    
    # Example 4: ones - array of ones
    print("\n4. np.ones() - Array of ones")
    print("-" * 70)
    
    ones_1d = np.ones(5)
    print(f"np.ones(5):\n{ones_1d}")
    
    ones_2d = np.ones((2, 3))
    print(f"\nnp.ones((2, 3)):\n{ones_2d}")
    
    # Example 5: full - array filled with value
    print("\n5. np.full() - Array filled with value")
    print("-" * 70)
    
    filled = np.full(5, 7)
    print(f"np.full(5, 7): {filled}")
    
    filled_2d = np.full((2, 3), 3.14)
    print(f"\nnp.full((2, 3), 3.14):\n{filled_2d}")
    
    # Example 6: eye - identity matrix
    print("\n6. np.eye() - Identity matrix")
    print("-" * 70)
    
    identity = np.eye(3)
    print(f"np.eye(3):\n{identity}")
    
    # Example 7: random - random values
    print("\n7. np.random - Random arrays")
    print("-" * 70)
    
    random_arr = np.random.rand(5)
    print(f"np.random.rand(5): {random_arr}")
    
    random_int = np.random.randint(1, 10, 5)
    print(f"np.random.randint(1, 10, 5): {random_int}")


def array_properties_and_indexing():
    """
    Demonstrate array properties and accessing elements.
    """
    print("\n" + "=" * 70)
    print("ARRAY PROPERTIES AND INDEXING")
    print("=" * 70)
    
    # Create example array
    array_2d = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])
    
    print(f"Array:\n{array_2d}\n")
    
    # Example 1: Shape - dimensions
    print("1. SHAPE (dimensions)")
    print("-" * 70)
    print(f"shape: {array_2d.shape}")  # (3, 3)
    print(f"ndim (number of dimensions): {array_2d.ndim}")
    print(f"size (total elements): {array_2d.size}")
    print(f"dtype (data type): {array_2d.dtype}")
    
    # Example 2: Indexing - single element
    print("\n2. INDEXING - SINGLE ELEMENT")
    print("-" * 70)
    print(f"array[0]: {array_2d[0]}")  # First row
    print(f"array[0, 0]: {array_2d[0, 0]}")  # First element
    print(f"array[1, 2]: {array_2d[1, 2]}")  # Row 1, Column 2
    print(f"array[-1, -1]: {array_2d[-1, -1]}")  # Last element
    
    # Example 3: Slicing
    print("\n3. SLICING - MULTIPLE ELEMENTS")
    print("-" * 70)
    print(f"array[0:2]:\n{array_2d[0:2]}")  # First two rows
    
    print(f"\narray[:, 0]:\n{array_2d[:, 0]}")  # First column
    
    print(f"\narray[1:, 1:] (bottom-right 2x2):\n{array_2d[1:, 1:]}")
    
    # Example 4: Accessing attributes
    print("\n4. COMMON ATTRIBUTES")
    print("-" * 70)
    
    arr = np.array([10, 20, 30, 40, 50])
    print(f"Array: {arr}")
    print(f"  shape: {arr.shape}")
    print(f"  dtype: {arr.dtype}")
    print(f"  itemsize: {arr.itemsize} bytes")
    print(f"  nbytes: {arr.nbytes} total bytes")


def practical_examples():
    """
    Practical examples of creating arrays for data analysis.
    """
    print("\n" + "=" * 70)
    print("PRACTICAL EXAMPLES")
    print("=" * 70)
    
    # Example 1: Convert test scores
    print("\n1. CONVERT TEST SCORES TO ARRAY")
    print("-" * 70)
    
    test_scores = [85, 92, 78, 88, 95, 91, 89, 87]
    print(f"Python list: {test_scores}")
    
    scores_array = np.array(test_scores)
    print(f"NumPy array: {scores_array}")
    print(f"Array info: dtype={scores_array.dtype}, shape={scores_array.shape}")
    
    # Example 2: Create matrix of student data
    print("\n2. CREATE STUDENT DATA MATRIX")
    print("-" * 70)
    
    student_data = [
        [101, "Alice", 95, 0],  # id, name, score, absences
        [102, "Bob", 87, 2],
        [103, "Charlie", 92, 1],
    ]
    print("Student data (list of lists):")
    for row in student_data:
        print(f"  {row}")
    
    data_array = np.array(student_data)
    print(f"\nAs NumPy array:")
    print(data_array)
    print(f"Shape: {data_array.shape}")
    
    # Example 3: Create time series data
    print("\n3. CREATE TIME SERIES DATA")
    print("-" * 70)
    
    # Daily temperatures for a week
    temps_fahrenheit = [72.5, 75.3, 71.8, 73.2, 76.1, 78.5, 79.3]
    print(f"Daily temperatures: {temps_fahrenheit}")
    
    temps_array = np.array(temps_fahrenheit)
    print(f"As array: {temps_array}")
    
    # Example 4: Create identity matrix for linear algebra
    print("\n4. CREATE IDENTITY MATRIX")
    print("-" * 70)
    
    identity_matrix = np.eye(3)
    print(f"3x3 Identity matrix:")
    print(identity_matrix)
    
    # Example 5: Create array of repeated values
    print("\n5. CREATE REPEATED VALUES")
    print("-" * 70)
    
    # Repeat a value 10 times
    repeated = np.array([1] * 10)
    print(f"np.array([1] * 10): {repeated}")
    
    # Using full function
    filled = np.full(8, 3.14)
    print(f"np.full(8, 3.14): {filled}")


def array_conversion_examples():
    """
    Demonstrate various array conversions and creations.
    """
    print("\n" + "=" * 70)
    print("ARRAY CONVERSION EXAMPLES")
    print("=" * 70)
    
    # Example 1: Convert Python range to array
    print("\n1. CONVERT RANGE TO ARRAY")
    print("-" * 70)
    
    python_range = range(1, 6)
    print(f"Range object: {python_range}")
    
    range_array = np.array(list(python_range))
    print(f"As array: {range_array}")
    
    # But arange is better
    better_way = np.arange(1, 6)
    print(f"Better way - np.arange(1, 6): {better_way}")
    
    # Example 2: Convert tuple to array
    print("\n2. CONVERT TUPLE TO ARRAY")
    print("-" * 70)
    
    tuple_data = (10, 20, 30, 40, 50)
    print(f"Tuple: {tuple_data}")
    
    tuple_array = np.array(tuple_data)
    print(f"As array: {tuple_array}")
    
    # Example 3: Extract data from list of dictionaries
    print("\n3. EXTRACT DATA FROM LIST OF DICTIONARIES")
    print("-" * 70)
    
    students = [
        {"name": "Alice", "score": 95},
        {"name": "Bob", "score": 87},
        {"name": "Charlie", "score": 92},
    ]
    
    print("List of dictionaries:")
    for student in students:
        print(f"  {student}")
    
    # Extract scores
    scores = [student["score"] for student in students]
    scores_array = np.array(scores)
    print(f"\nExtracted scores as array: {scores_array}")


if __name__ == "__main__":
    print("Creating NumPy Arrays from Python Lists\n")
    
    creating_arrays_from_lists()
    numpy_creation_functions()
    array_properties_and_indexing()
    practical_examples()
    array_conversion_examples()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("- Use np.array() to convert Python lists to NumPy arrays")
    print("- NumPy offers specialized functions: arange, linspace, zeros, etc.")
    print("- Arrays have properties: shape, dtype, ndim, size")
    print("- Access elements and slices using indexing")
    print("- NumPy arrays enable efficient numerical computing")
    print("=" * 70)
