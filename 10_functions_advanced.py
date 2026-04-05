#!/usr/bin/env python3
"""
Passing Data into Functions and Returning Results

This explores advanced patterns for function inputs and outputs,
essential for building robust data processing pipelines.
"""


def passing_different_types():
    """
    Demonstrate passing different data types to functions.
    """
    print("=" * 70)
    print("PASSING DIFFERENT DATA TYPES TO FUNCTIONS")
    print("=" * 70)
    
    # Example 1: Passing integers and floats
    print("\n1. PASSING NUMERIC TYPES")
    print("-" * 70)
    
    def calculate_total(price, quantity, tax_rate=0.08):
        """Calculate total price with tax."""
        subtotal = price * quantity
        tax = subtotal * tax_rate
        total = subtotal + tax
        return total
    
    print("def calculate_total(price, quantity, tax_rate=0.08):")
    print("    subtotal = price * quantity")
    print("    tax = subtotal * tax_rate")
    print("    total = subtotal + tax")
    print("    return total\n")
    
    total1 = calculate_total(29.99, 3)  # Using default tax rate
    print(f"calculate_total(29.99, 3) = ${total1:.2f}")
    
    total2 = calculate_total(29.99, 3, 0.10)  # Different tax rate
    print(f"calculate_total(29.99, 3, 0.10) = ${total2:.2f}")
    
    # Example 2: Passing strings
    print("\n2. PASSING STRING DATA")
    print("-" * 70)
    
    def format_name(first, middle, last):
        """Format a full name."""
        full_name = f"{first} {middle} {last}"
        return full_name
    
    print("def format_name(first, middle, last):")
    print('    full_name = f"{first} {middle} {last}"')
    print("    return full_name\n")
    
    name = format_name("John", "Michael", "Smith")
    print(f'format_name("John", "Michael", "Smith") = {name}')
    
    # Example 3: Passing lists
    print("\n3. PASSING LIST DATA")
    print("-" * 70)
    
    def sum_list(values):
        """Sum all values in a list."""
        total = sum(values)
        return total
    
    print("def sum_list(values):")
    print("    total = sum(values)")
    print("    return total\n")
    
    data = [10, 20, 30, 40, 50]
    result = sum_list(data)
    print(f"sum_list({data}) = {result}")
    
    # Example 4: Passing dictionaries
    print("\n4. PASSING DICTIONARY DATA")
    print("-" * 70)
    
    def get_student_info(student_dict):
        """Extract and format student information."""
        name = student_dict["name"]
        grade = student_dict["grade"]
        return f"{name} received a grade of {grade}"
    
    print("def get_student_info(student_dict):")
    print('    name = student_dict["name"]')
    print('    grade = student_dict["grade"]')
    print('    return f"{name} received a grade of {grade}"\n')
    
    student = {"name": "Alice", "grade": "A", "id": 123}
    info = get_student_info(student)
    print(f"Result: {info}")


def returning_different_types():
    """
    Demonstrate returning different data types from functions.
    """
    print("\n" + "=" * 70)
    print("RETURNING DIFFERENT DATA TYPES")
    print("=" * 70)
    
    # Example 1: Return a single integer
    print("\n1. RETURNING INTEGER")
    print("-" * 70)
    
    def count_items(items):
        """Count items in a collection."""
        return len(items)
    
    items = ["apple", "banana", "cherry"]
    count = count_items(items)
    print(f"count_items({items}) = {count}")
    
    # Example 2: Return a string
    print("\n2. RETURNING STRING")
    print("-" * 70)
    
    def describe_temperature(celsius):
        """Describe temperature based on Celsius value."""
        if celsius > 25:
            description = "Hot"
        elif celsius > 15:
            description = "Warm"
        elif celsius > 5:
            description = "Cool"
        else:
            description = "Cold"
        return description
    
    temps = [0, 10, 20, 30]
    for temp in temps:
        desc = describe_temperature(temp)
        print(f"describe_temperature({temp}) = '{desc}'")
    
    # Example 3: Return a list
    print("\n3. RETURNING LIST")
    print("-" * 70)
    
    def filter_positive(numbers):
        """Return only positive numbers from a list."""
        positive = []
        for num in numbers:
            if num > 0:
                positive.append(num)
        return positive
    
    test_data = [-5, 10, -2, 15, 0, 20]
    result = filter_positive(test_data)
    print(f"filter_positive({test_data})")
    print(f"  Result: {result}")
    
    # Example 4: Return a dictionary
    print("\n4. RETURNING DICTIONARY")
    print("-" * 70)
    
    def analyze_data(numbers):
        """Return multiple analysis results as a dictionary."""
        analysis = {
            "count": len(numbers),
            "sum": sum(numbers),
            "average": sum(numbers) / len(numbers) if numbers else 0,
            "min": min(numbers) if numbers else None,
            "max": max(numbers) if numbers else None,
        }
        return analysis
    
    data = [10, 25, 15, 30, 20]
    results = analyze_data(data)
    print(f"analyze_data({data})")
    print("  Results:")
    for key, value in results.items():
        if isinstance(value, float):
            print(f"    {key}: {value:.2f}")
        else:
            print(f"    {key}: {value}")
    
    # Example 5: Return a tuple
    print("\n5. RETURNING TUPLE")
    print("-" * 70)
    
    def get_coordinates(point_name):
        """Get x, y coordinates for a named point."""
        points = {
            "origin": (0, 0),
            "a": (10, 20),
            "b": (30, 40),
        }
        return points.get(point_name, (0, 0))
    
    point = get_coordinates("a")
    x, y = point
    print(f"get_coordinates('a') = {point}")
    print(f"Unpacked: x={x}, y={y}")


def multiple_return_values():
    """
    Demonstrate returning multiple values from a function.
    """
    print("\n" + "=" * 70)
    print("RETURNING MULTIPLE VALUES")
    print("=" * 70)
    
    # Example 1: Return tuple with multiple values
    print("\n1. RETURN TUPLE - MULTIPLE VALUES")
    print("-" * 70)
    
    def calculate_stats(numbers):
        """Calculate min, max, and average."""
        minimum = min(numbers)
        maximum = max(numbers)
        average = sum(numbers) / len(numbers)
        return minimum, maximum, average
    
    print("def calculate_stats(numbers):")
    print("    return minimum, maximum, average\n")
    
    data = [10, 45, 23, 67, 34]
    min_val, max_val, avg = calculate_stats(data)
    print(f"Data: {data}")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Average: {avg:.2f}")
    
    # Example 2: Return dictionary with named values
    print("\n2. RETURN DICTIONARY - NAMED VALUES")
    print("-" * 70)
    
    def process_text(text):
        """Analyze text and return multiple metrics."""
        results = {
            "original": text,
            "length": len(text),
            "uppercase": text.upper(),
            "word_count": len(text.split()),
        }
        return results
    
    print("def process_text(text):")
    print("    results = {")
    print('        "original": text,')
    print('        "length": len(text),')
    print('        "uppercase": text.upper(),')
    print('        "word_count": len(text.split()),')
    print("    }")
    print("    return results\n")
    
    output = process_text("Hello Data Science")
    for key, value in output.items():
        print(f"  {key}: {value}")
    
    # Example 3: Return with conditional multiple values
    print("\n3. CONDITIONAL MULTIPLE RETURNS")
    print("-" * 70)
    
    def validate_and_convert(value):
        """Try to convert to int, return status and result."""
        try:
            converted = int(value)
            return True, converted
        except ValueError:
            return False, None
    
    test_values = ["42", "hello", "100", "3.14"]
    for val in test_values:
        is_valid, result = validate_and_convert(val)
        if is_valid:
            print(f"{val}: Valid -> {result}")
        else:
            print(f"{val}: Invalid")


def chaining_functions():
    """
    Demonstrate using output of one function as input to another.
    """
    print("\n" + "=" * 70)
    print("CHAINING FUNCTIONS (Output -> Input)")
    print("=" * 70)
    
    def double_value(x):
        """Double a value."""
        return x * 2
    
    def add_ten(x):
        """Add ten to a value."""
        return x + 10
    
    def square(x):
        """Square a value."""
        return x ** 2
    
    print("\n1. SEQUENTIAL FUNCTION CHAINING")
    print("-" * 70)
    
    value = 5
    print(f"Starting value: {value}")
    
    step1 = double_value(value)
    print(f"After double_value(): {step1}")
    
    step2 = add_ten(step1)
    print(f"After add_ten(): {step2}")
    
    step3 = square(step2)
    print(f"After square(): {step3}")
    
    # Example 2: Direct chaining
    print("\n2. DIRECT FUNCTION CHAINING")
    print("-" * 70)
    
    result = square(add_ten(double_value(5)))
    print(f"square(add_ten(double_value(5))) = {result}")


def real_world_data_pipeline():
    """
    Real-world data processing pipeline using functions.
    """
    print("\n" + "=" * 70)
    print("REAL-WORLD DATA PIPELINE")
    print("=" * 70)
    
    def load_scores(names, scores_list):
        """Create a dataset."""
        data = []
        for name, score in zip(names, scores_list):
            data.append({"name": name, "score": score})
        return data
    
    def filter_passing(data, min_score=70):
        """Filter only passing scores."""
        passing = [item for item in data if item["score"] >= min_score]
        return passing
    
    def calculate_average(data):
        """Calculate average score."""
        if not data:
            return 0
        scores = [item["score"] for item in data]
        return sum(scores) / len(scores)
    
    def create_report(data):
        """Create a report from data."""
        if not data:
            return "No data to report"
        
        avg = calculate_average(data)
        report = f"Students: {len(data)}, Average: {avg:.2f}"
        return report
    
    # Pipeline execution
    print("\nExecuting data pipeline:")
    print("-" * 70)
    
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    scores = [95, 72, 68, 88, 92]
    
    # Step 1: Load data
    data = load_scores(names, scores)
    print(f"Step 1 - Loaded {len(data)} records")
    
    # Step 2: Filter data
    passing_data = filter_passing(data, 70)
    print(f"Step 2 - Filtered to {len(passing_data)} passing students")
    
    # Step 3: Generate report
    report = create_report(passing_data)
    print(f"Step 3 - Report: {report}")


if __name__ == "__main__":
    print("Passing Data and Returning Results\n")
    
    passing_different_types()
    returning_different_types()
    multiple_return_values()
    chaining_functions()
    real_world_data_pipeline()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("- Pass any Python type to functions (int, str, list, dict)")
    print("- Return single or multiple values")
    print("- Use tuples or dicts for returning multiple values")
    print("- Chain functions for data pipelines")
    print("- Functions are building blocks for data processing")
    print("=" * 70)
