#!/usr/bin/env python3
"""
Understanding Python Numeric and String Data Types

This script demonstrates the fundamental numeric and string data types
in Python and how to work with them effectively in data analysis.
"""


def numeric_types_demo():
    """
    Demonstrate Python's numeric data types.
    
    Python has three main numeric types:
    - int: Integers (whole numbers)
    - float: Floating-point numbers (decimals)
    - complex: Complex numbers (rarely used in data science)
    """
    print("=" * 60)
    print("NUMERIC TYPES DEMONSTRATION")
    print("=" * 60)
    
    # Integer type (int)
    print("\n1. INTEGER TYPE (int)")
    print("-" * 60)
    age = 25
    year = 2024
    count = -100
    print(f"age = {age}, type = {type(age)}")
    print(f"year = {year}, type = {type(year)}")
    print(f"count = {count}, type = {type(count)}")
    
    # Operations with integers
    print("\nInteger Operations:")
    num1 = 10
    num2 = 3
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")  # Division (returns float)
    print(f"{num1} // {num2} = {num1 // num2}")  # Floor division (returns int)
    print(f"{num1} % {num2} = {num1 % num2}")  # Modulo (remainder)
    print(f"{num1} ** {num2} = {num1 ** num2}")  # Power/exponent
    
    # Float type (float)
    print("\n2. FLOAT TYPE (float)")
    print("-" * 60)
    temperature = 98.6
    price = 19.99
    percentage = 0.75
    print(f"temperature = {temperature}, type = {type(temperature)}")
    print(f"price = {price}, type = {type(price)}")
    print(f"percentage = {percentage}, type = {type(percentage)}")
    
    # Operations with floats
    print("\nFloat Operations:")
    f1 = 7.5
    f2 = 2.5
    print(f"{f1} + {f2} = {f1 + f2}")
    print(f"{f1} * {f2} = {f1 * f2}")
    print(f"{f1} / {f2} = {f1 / f2}")
    
    # Type conversion
    print("\n3. TYPE CONVERSION")
    print("-" * 60)
    string_num = "42"
    converted_int = int(string_num)
    print(f"str '{string_num}' to int: {converted_int}, type = {type(converted_int)}")
    
    string_float = "3.14"
    converted_float = float(string_float)
    print(f"str '{string_float}' to float: {converted_float}, type = {type(converted_float)}")
    
    int_to_float = float(10)
    print(f"int 10 to float: {int_to_float}, type = {type(int_to_float)}")
    
    float_to_int = int(7.9)
    print(f"float 7.9 to int: {float_to_int}, type = {type(float_to_int)}")


def string_types_demo():
    """
    Demonstrate Python's string data type and operations.
    
    Strings are sequences of characters. They're used for text data
    and are fundamental in data processing.
    """
    print("\n" + "=" * 60)
    print("STRING TYPE DEMONSTRATION")
    print("=" * 60)
    
    # String creation
    print("\n1. CREATING STRINGS")
    print("-" * 60)
    single_quote = 'Hello'
    double_quote = "World"
    triple_quote = """This is a
    multi-line
    string"""
    
    print(f"single_quote: {single_quote}")
    print(f"double_quote: {double_quote}")
    print(f"triple_quote: {repr(triple_quote)}")
    
    # String length
    print("\n2. STRING LENGTH")
    print("-" * 60)
    text = "Data Science"
    print(f"Text: '{text}'")
    print(f"Length: {len(text)}")
    
    # String concatenation
    print("\n3. STRING CONCATENATION")
    print("-" * 60)
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Full name: {full_name}")
    
    # String repetition
    print("\n4. STRING REPETITION")
    print("-" * 60)
    symbol = "*"
    repeated = symbol * 10
    print(f"'{symbol}' * 10 = '{repeated}'")
    
    # String indexing
    print("\n5. STRING INDEXING")
    print("-" * 60)
    word = "Python"
    print(f"Word: {word}")
    print(f"Index 0: {word[0]}")
    print(f"Index 1: {word[1]}")
    print(f"Index -1 (last): {word[-1]}")
    print(f"Index -2 (second to last): {word[-2]}")
    
    # String slicing
    print("\n6. STRING SLICING")
    print("-" * 60)
    text = "DataScience"
    print(f"Text: {text}")
    print(f"text[0:4]: {text[0:4]}")
    print(f"text[4:]: {text[4:]}")
    print(f"text[::2]: {text[::2]}")  # Every 2nd character
    
    # String methods
    print("\n7. USEFUL STRING METHODS")
    print("-" * 60)
    text = "hello world"
    print(f"Original: '{text}'")
    print(f"upper(): '{text.upper()}'")
    print(f"title(): '{text.title()}'")
    print(f"replace(): '{text.replace('world', 'Python')}'")
    print(f"split(): {text.split()}")
    print(f"count('l'): {text.count('l')}")
    
    # String formatting
    print("\n8. STRING FORMATTING")
    print("-" * 60)
    name = "Alice"
    age = 30
    score = 95.5
    
    # F-strings (modern, recommended)
    print(f"F-string: {name} is {age} years old with score {score:.1f}")
    
    # format() method
    print("format(): {} is {} years old with score {:.1f}".format(name, age, score))
    
    # % operator (old style)
    print("%% operator: %s is %d years old" % (name, age))


def combined_demo():
    """
    Demonstrate working with mixed numeric and string data.
    
    This is common in data analysis - combining numbers and text.
    """
    print("\n" + "=" * 60)
    print("MIXED NUMERIC AND STRING DATA")
    print("=" * 60)
    
    # Sample data
    print("\nSample Student Records:")
    print("-" * 60)
    
    records = [
        ("Alice", 95, 3.8),
        ("Bob", 87, 3.6),
        ("Charlie", 92, 3.9),
    ]
    
    for name, score, gpa in records:
        # Converting to string for display
        display = f"{name}: Score {score}, GPA {gpa:.2f}"
        print(display)
    
    # Data analysis with mixed types
    print("\nData Analysis:")
    print("-" * 60)
    total_score = 0
    for name, score, gpa in records:
        total_score += score
        print(f"Analyzing {name}: {score} points")
    
    average = total_score / len(records)
    print(f"Average Score: {average:.2f}")


if __name__ == "__main__":
    print("Python Numeric and String Data Types Tutorial\n")
    
    # Run demonstrations
    numeric_types_demo()
    string_types_demo()
    combined_demo()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("- int: Whole numbers (positive, negative, zero)")
    print("- float: Decimals for precise calculations")
    print("- str: Text data for labels, descriptions, categories")
    print("- Type conversion: Convert between types as needed")
    print("- String methods: Powerful tools for text processing")
    print("=" * 60)
