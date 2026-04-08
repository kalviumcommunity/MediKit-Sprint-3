#!/usr/bin/env python3
"""
Performing Basic Mathematical Operations on NumPy Arrays

NumPy arrays support element-wise mathematical operations,
enabling efficient numerical computing and data analysis.
"""

import numpy as np


def element_wise_arithmetic():
    """
    Demonstrate element-wise arithmetic operations on arrays.
    """
    print("=" * 70)
    print("ELEMENT-WISE ARITHMETIC OPERATIONS")
    print("=" * 70)
    
    # Create sample arrays
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([2, 2, 2, 2, 2])
    scalar = 3
    
    print(f"array1: {array1}")
    print(f"array2: {array2}")
    print(f"scalar: {scalar}\n")
    
    # Example 1: Addition
    print("1. ADDITION")
    print("-" * 70)
    print(f"array1 + array2: {array1 + array2}")
    print(f"array1 + scalar: {array1 + scalar}")
    
    # Example 2: Subtraction
    print("\n2. SUBTRACTION")
    print("-" * 70)
    print(f"array1 - array2: {array1 - array2}")
    print(f"array1 - scalar: {array1 - scalar}")
    
    # Example 3: Multiplication
    print("\n3. MULTIPLICATION (element-wise)")
    print("-" * 70)
    print(f"array1 * array2: {array1 * array2}")
    print(f"array1 * scalar: {array1 * scalar}")
    
    # Example 4: Division
    print("\n4. DIVISION (element-wise)")
    print("-" * 70)
    print(f"array1 / array2: {array1 / array2}")
    print(f"array1 / scalar: {array1 / scalar}")
    
    # Example 5: Power
    print("\n5. POWER (exponentiation)")
    print("-" * 70)
    print(f"array1 ** 2: {array1 ** 2}")
    print(f"array1 ** scalar: {array1 ** scalar}")
    
    # Example 6: Modulo
    print("\n6. MODULO (remainder)")
    print("-" * 70)
    print(f"array1 % 2: {array1 % 2}")


def array_functions():
    """
    Demonstrate mathematical functions on arrays.
    """
    print("\n" + "=" * 70)
    print("MATHEMATICAL FUNCTIONS")
    print("=" * 70)
    
    # Example 1: Square root
    print("\n1. SQUARE ROOT (sqrt)")
    print("-" * 70)
    array = np.array([16, 25, 36, 49])
    print(f"array: {array}")
    print(f"np.sqrt(array): {np.sqrt(array)}")
    
    # Example 2: Absolute value
    print("\n2. ABSOLUTE VALUE (abs)")
    print("-" * 70)
    array = np.array([-5, -3, 0, 3, 5])
    print(f"array: {array}")
    print(f"np.abs(array): {np.abs(array)}")
    
    # Example 3: Exponential
    print("\n3. EXPONENTIAL (exp)")
    print("-" * 70)
    array = np.array([0, 1, 2, 3])
    print(f"array: {array}")
    print(f"np.exp(array): {np.exp(array)}")
    
    # Example 4: Logarithm
    print("\n4. LOGARITHM (log)")
    print("-" * 70)
    array = np.array([1, 2.718, 10, 100])
    print(f"array: {array}")
    print(f"np.log(array): {np.log(array)}")
    print(f"np.log10(array): {np.log10(array)}")
    
    # Example 5: Trigonometric functions
    print("\n5. TRIGONOMETRIC FUNCTIONS")
    print("-" * 70)
    angles = np.array([0, np.pi/6, np.pi/4, np.pi/2])
    print(f"angles (radians): {angles}")
    print(f"sin(angles): {np.sin(angles)}")
    print(f"cos(angles): {np.cos(angles)}")
    print(f"tan(angles): {np.tan(angles)}")
    
    # Example 6: Rounding functions
    print("\n6. ROUNDING FUNCTIONS")
    print("-" * 70)
    array = np.array([1.234, 5.678, 3.14159, 2.71828])
    print(f"array: {array}")
    print(f"np.round(array, 2): {np.round(array, 2)}")
    print(f"np.floor(array): {np.floor(array)}")
    print(f"np.ceil(array): {np.ceil(array)}")


def aggregation_functions():
    """
    Demonstrate aggregation and reduction functions.
    """
    print("\n" + "=" * 70)
    print("AGGREGATION FUNCTIONS (reduce to single value)")
    print("=" * 70)
    
    array = np.array([10, 20, 30, 40, 50])
    print(f"array: {array}\n")
    
    # Example 1: Sum
    print("1. SUM (total)")
    print("-" * 70)
    print(f"np.sum(array): {np.sum(array)}")
    print(f"array.sum(): {array.sum()}")
    
    # Example 2: Mean (average)
    print("\n2. MEAN (average)")
    print("-" * 70)
    print(f"np.mean(array): {np.mean(array)}")
    print(f"array.mean(): {array.mean()}")
    
    # Example 3: Median (middle value)
    print("\n3. MEDIAN (middle value)")
    print("-" * 70)
    print(f"np.median(array): {np.median(array)}")
    
    # Example 4: Standard deviation
    print("\n4. STANDARD DEVIATION (spread)")
    print("-" * 70)
    print(f"np.std(array): {np.std(array)}")
    
    # Example 5: Variance
    print("\n5. VARIANCE (squared spread)")
    print("-" * 70)
    print(f"np.var(array): {np.var(array)}")
    
    # Example 6: Min and Max
    print("\n6. MINIMUM AND MAXIMUM")
    print("-" * 70)
    print(f"np.min(array): {np.min(array)}")
    print(f"np.max(array): {np.max(array)}")
    print(f"array.min(): {array.min()}")
    print(f"array.max(): {array.max()}")
    
    # Example 7: Argmin and Argmax (indices)
    print("\n7. INDICES OF MIN AND MAX")
    print("-" * 70)
    print(f"np.argmin(array): {np.argmin(array)} (index of minimum)")
    print(f"np.argmax(array): {np.argmax(array)} (index of maximum)")
    
    # Example 8: Cumulative sum
    print("\n8. CUMULATIVE SUM")
    print("-" * 70)
    print(f"np.cumsum(array): {np.cumsum(array)}")


def operations_on_2d_arrays():
    """
    Demonstrate operations on 2D arrays and matrices.
    """
    print("\n" + "=" * 70)
    print("OPERATIONS ON 2D ARRAYS (MATRICES)")
    print("=" * 70)
    
    # Create 2D arrays
    matrix1 = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    
    matrix2 = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    
    print("matrix1:")
    print(matrix1)
    print("\nmatrix2:")
    print(matrix2)
    
    # Example 1: Element-wise operations
    print("\n1. ELEMENT-WISE OPERATIONS")
    print("-" * 70)
    print("matrix1 + matrix2:")
    print(matrix1 + matrix2)
    
    print("\nmatrix1 * 2:")
    print(matrix1 * 2)
    
    # Example 2: Matrix multiplication
    print("\n2. MATRIX MULTIPLICATION (dot product)")
    print("-" * 70)
    matrix_a = np.array([
        [1, 2],
        [3, 4]
    ])
    matrix_b = np.array([
        [5, 6],
        [7, 8]
    ])
    print("matrix_a:")
    print(matrix_a)
    print("\nmatrix_b:")
    print(matrix_b)
    
    result = np.dot(matrix_a, matrix_b)
    print("\nnp.dot(matrix_a, matrix_b):")
    print(result)
    
    # Example 3: Transpose
    print("\n3. TRANSPOSE (swap rows and columns)")
    print("-" * 70)
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print("Original matrix:")
    print(matrix)
    print("\nTranspose (matrix.T):")
    print(matrix.T)
    
    # Example 4: Aggregation along axis
    print("\n4. AGGREGATION ALONG AXIS")
    print("-" * 70)
    matrix = np.array([
        [10, 20, 30],
        [40, 50, 60]
    ])
    print("matrix:")
    print(matrix)
    
    print(f"\nSum along axis 0 (down columns): {np.sum(matrix, axis=0)}")
    print(f"Sum along axis 1 (across rows): {np.sum(matrix, axis=1)}")
    print(f"Mean along axis 0: {np.mean(matrix, axis=0)}")


def comparison_and_logical():
    """
    Demonstrate comparison and logical operations.
    """
    print("\n" + "=" * 70)
    print("COMPARISON AND LOGICAL OPERATIONS")
    print("=" * 70)
    
    array = np.array([10, 20, 30, 40, 50])
    print(f"array: {array}\n")
    
    # Example 1: Comparison operators
    print("1. COMPARISON OPERATORS")
    print("-" * 70)
    print(f"array > 25: {array > 25}")
    print(f"array == 30: {array == 30}")
    print(f"array < 40: {array < 40}")
    
    # Example 2: Logical operations
    print("\n2. LOGICAL OPERATIONS")
    print("-" * 70)
    condition1 = array > 15
    condition2 = array < 45
    print(f"array > 15: {condition1}")
    print(f"array < 45: {condition2}")
    print(f"(array > 15) & (array < 45): {condition1 & condition2}")
    print(f"(array < 20) | (array > 40): {(array < 20) | (array > 40)}")
    
    # Example 3: Filtering with boolean indexing
    print("\n3. FILTERING (boolean indexing)")
    print("-" * 70)
    mask = array > 25
    filtered = array[mask]
    print(f"Values greater than 25: {filtered}")
    
    mask2 = (array >= 20) & (array <= 40)
    filtered2 = array[mask2]
    print(f"Values between 20 and 40: {filtered2}")


def practical_data_analysis():
    """
    Practical example: analyzing test scores.
    """
    print("\n" + "=" * 70)
    print("PRACTICAL EXAMPLE: TEST SCORE ANALYSIS")
    print("=" * 70)
    
    # Sample test scores
    scores = np.array([75, 82, 90, 85, 78, 92, 88, 76, 95, 80])
    
    print(f"Test scores: {scores}\n")
    
    # Calculate statistics
    print("STATISTICS:")
    print("-" * 70)
    print(f"Count: {len(scores)}")
    print(f"Sum: {np.sum(scores)}")
    print(f"Mean: {np.mean(scores):.2f}")
    print(f"Median: {np.median(scores):.2f}")
    print(f"Minimum: {np.min(scores)}")
    print(f"Maximum: {np.max(scores)}")
    print(f"Standard Deviation: {np.std(scores):.2f}")
    print(f"Range: {np.max(scores) - np.min(scores)}")
    
    # Classify scores
    print("\nCLASSIFICATION:")
    print("-" * 70)
    high_scorers = scores[scores >= 90]
    low_scorers = scores[scores < 80]
    
    print(f"High scorers (>=90): {high_scorers} (count: {len(high_scorers)})")
    print(f"Low scorers (<80): {low_scorers} (count: {len(low_scorers)})")
    
    # Improvement needed
    print("\nIMPROVEMENT ANALYSIS:")
    print("-" * 70)
    target_score = 85
    improvements_needed = target_score - scores
    max_improvements = np.where(improvements_needed > 0, improvements_needed, 0)
    print(f"Points needed to reach {target_score}:")
    for i, points in enumerate(max_improvements):
        if points > 0:
            print(f"  Score {scores[i]}: needs {int(points)} points")


def performance_comparison():
    """
    Show performance advantage of NumPy over Python lists.
    """
    print("\n" + "=" * 70)
    print("WHY USE NUMPY? EFFICIENCY EXAMPLE")
    print("=" * 70)
    
    # Create data
    size = 1000
    data = np.arange(size)
    
    print(f"\nOperating on array of size {size}:")
    print("-" * 70)
    
    # NumPy is fast for operations
    result1 = data * 2  # Element-wise multiplication
    print(f"NumPy array * 2: First 5 results: {result1[:5]}")
    
    result2 = data ** 2  # Element-wise square
    print(f"NumPy array ** 2: First 5 results: {result2[:5]}")
    
    result3 = np.sum(data)
    print(f"NumPy sum: {result3}")
    
    result4 = np.mean(data)
    print(f"NumPy mean: {result4:.2f}")
    
    print("\nNumPy is optimized for:")
    print("  - Large numerical datasets")
    print("  - Fast mathematical operations")
    print("  - Memory efficiency")
    print("  - Scientific computing")


if __name__ == "__main__":
    print("Basic Mathematical Operations on NumPy Arrays\n")
    
    element_wise_arithmetic()
    array_functions()
    aggregation_functions()
    operations_on_2d_arrays()
    comparison_and_logical()
    practical_data_analysis()
    performance_comparison()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("- NumPy supports element-wise operations: +, -, *, /, **")
    print("- Mathematical functions: sqrt, exp, log, sin, cos, etc.")
    print("- Aggregation functions: sum, mean, median, std, etc.")
    print("- Matrix operations: dot product, transpose, multiply")
    print("- Comparison and filtering for data selection")
    print("- NumPy is much faster than Python lists for large data")
    print("=" * 70)
