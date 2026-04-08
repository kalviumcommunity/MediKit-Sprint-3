#!/usr/bin/env python3
"""
Defining and Calling Python Functions

Functions are reusable blocks of code that perform specific tasks.
They help organize code, reduce repetition, and make programs maintainable.
"""


def simple_function_demo():
    """
    Demonstrate simple function definition and calling.
    """
    print("=" * 70)
    print("SIMPLE FUNCTION DEFINITION AND CALLING")
    print("=" * 70)
    
    # Example 1: Function with no parameters or return value
    print("\n1. SIMPLE FUNCTION (no parameters, no return)")
    print("-" * 70)
    
    def greet():
        """A simple greeting function."""
        print("Hello, World!")
    
    print("def greet():")
    print('    print("Hello, World!")\n')
    print("Calling greet():")
    greet()
    greet()
    
    # Example 2: Function that performs an action
    print("\n2. FUNCTION THAT PERFORMS AN ACTION")
    print("-" * 70)
    
    def print_separator():
        """Print a line separator."""
        print("-" * 40)
    
    print("def print_separator():")
    print('    print("-" * 40)\n')
    print("Calling print_separator():")
    print_separator()
    
    # Example 3: Multiple function calls
    print("\n3. MULTIPLE FUNCTION CALLS")
    print("-" * 70)
    
    def display_header(title):
        """Display a formatted header."""
        print("=" * 40)
        print(title)
        print("=" * 40)
    
    print("Calling functions sequentially:")
    display_header("Section 1")
    print("Content here")
    display_header("Section 2")
    print("More content")


def function_with_parameters():
    """
    Demonstrate functions with parameters.
    """
    print("\n" + "=" * 70)
    print("FUNCTIONS WITH PARAMETERS")
    print("=" * 70)
    
    # Example 1: Single parameter
    print("\n1. FUNCTION WITH ONE PARAMETER")
    print("-" * 70)
    
    def greet_person(name):
        """Greet a specific person."""
        print(f"Hello, {name}!")
    
    print("def greet_person(name):")
    print('    print(f"Hello, {name}!")\n')
    print("Calling with different arguments:")
    greet_person("Alice")
    greet_person("Bob")
    greet_person("Charlie")
    
    # Example 2: Multiple parameters
    print("\n2. FUNCTION WITH MULTIPLE PARAMETERS")
    print("-" * 70)
    
    def introduce(name, age, city):
        """Introduce someone with multiple details."""
        print(f"My name is {name}, I'm {age} years old, and I live in {city}")
    
    print("def introduce(name, age, city):")
    print('    print(f"My name is {name}, I\'m {age} years old, and I live in {city}")\n')
    print("Calling with multiple arguments:")
    introduce("Alice", 30, "New York")
    introduce("Bob", 25, "Boston")
    
    # Example 3: Default parameters
    print("\n3. FUNCTION WITH DEFAULT PARAMETERS")
    print("-" * 70)
    
    def format_grade(score, subject="General"):
        """Format a grade with optional subject."""
        print(f"{subject} Score: {score}%")
    
    print("def format_grade(score, subject='General'):")
    print('    print(f"{subject} Score: {score}%")\n')
    print("Calling with required parameter only:")
    format_grade(85)
    print("\nCalling with both parameters:")
    format_grade(92, "Math")
    format_grade(88, "English")


def function_with_return():
    """
    Demonstrate functions with return values.
    """
    print("\n" + "=" * 70)
    print("FUNCTIONS WITH RETURN VALUES")
    print("=" * 70)
    
    # Example 1: Return a single value
    print("\n1. RETURN A SINGLE VALUE")
    print("-" * 70)
    
    def add_numbers(a, b):
        """Add two numbers and return the result."""
        result = a + b
        return result
    
    print("def add_numbers(a, b):")
    print("    result = a + b")
    print("    return result\n")
    print("Calling and storing result:")
    sum_result = add_numbers(10, 20)
    print(f"add_numbers(10, 20) = {sum_result}")
    
    sum_result = add_numbers(7, 3)
    print(f"add_numbers(7, 3) = {sum_result}")
    
    # Example 2: Return with conditional
    print("\n2. CONDITIONAL RETURN VALUE")
    print("-" * 70)
    
    def check_pass_fail(score):
        """Check if score is passing (>= 70)."""
        if score >= 70:
            return "PASS"
        else:
            return "FAIL"
    
    print("def check_pass_fail(score):")
    print("    if score >= 70:")
    print('        return "PASS"')
    print("    else:")
    print('        return "FAIL"\n')
    
    test_scores = [85, 65, 92, 68, 75]
    for score in test_scores:
        status = check_pass_fail(score)
        print(f"Score {score}: {status}")
    
    # Example 3: Return multiple values
    print("\n3. RETURN MULTIPLE VALUES")
    print("-" * 70)
    
    def get_min_max(numbers):
        """Return both minimum and maximum from a list."""
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum
    
    print("def get_min_max(numbers):")
    print("    minimum = min(numbers)")
    print("    maximum = max(numbers)")
    print("    return minimum, maximum\n")
    
    data = [10, 25, 5, 30, 15]
    min_val, max_val = get_min_max(data)
    print(f"Data: {data}")
    print(f"Minimum: {min_val}, Maximum: {max_val}")


def function_documentation():
    """
    Demonstrate function documentation (docstrings).
    """
    print("\n" + "=" * 70)
    print("FUNCTION DOCUMENTATION")
    print("=" * 70)
    
    def calculate_average(numbers):
        """
        Calculate the average of a list of numbers.
        
        Args:
            numbers (list): List of numeric values
        
        Returns:
            float: The average of the numbers
        """
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    
    print("\n1. ACCESSING DOCSTRING")
    print("-" * 70)
    print("Function docstring:")
    print(calculate_average.__doc__)
    
    print("\n2. USING THE FUNCTION")
    print("-" * 70)
    test_scores = [85, 92, 78, 88, 95]
    avg = calculate_average(test_scores)
    print(f"Scores: {test_scores}")
    print(f"Average: {avg:.2f}")


def real_world_functions():
    """
    Real-world function examples for data analysis.
    """
    print("\n" + "=" * 70)
    print("REAL-WORLD DATA ANALYSIS FUNCTIONS")
    print("=" * 70)
    
    # Example 1: Data validation function
    print("\n1. DATA VALIDATION FUNCTION")
    print("-" * 70)
    
    def is_valid_age(age):
        """Check if an age is valid (between 0 and 150)."""
        return 0 <= age <= 150
    
    test_ages = [25, -5, 150, 200, 0]
    for age in test_ages:
        valid = is_valid_age(age)
        print(f"Age {age}: {'Valid' if valid else 'Invalid'}")
    
    # Example 2: Data transformation function
    print("\n2. DATA TRANSFORMATION FUNCTION")
    print("-" * 70)
    
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius temperature to Fahrenheit."""
        return (celsius * 9/5) + 32
    
    temps_c = [0, 10, 20, 25, 30]
    print("Temperature conversion:")
    for celsius in temps_c:
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"  {celsius}°C = {fahrenheit:.1f}°F")
    
    # Example 3: Data analysis function
    print("\n3. DATA ANALYSIS FUNCTION")
    print("-" * 70)
    
    def analyze_scores(scores):
        """Analyze a list of scores."""
        if not scores:
            return None
        
        average = sum(scores) / len(scores)
        highest = max(scores)
        lowest = min(scores)
        
        return {
            "average": average,
            "highest": highest,
            "lowest": lowest,
            "count": len(scores)
        }
    
    student_scores = [85, 92, 78, 88, 95, 91, 89]
    analysis = analyze_scores(student_scores)
    
    print(f"Scores: {student_scores}")
    print(f"Analysis Results:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")


def variable_scope():
    """
    Explain variable scope in functions.
    """
    print("\n" + "=" * 70)
    print("VARIABLE SCOPE")
    print("=" * 70)
    
    global_var = "I'm global"
    
    print(f"\nGlobal variable: {global_var}")
    
    def demo_scope():
        """Demonstrate local vs global variables."""
        local_var = "I'm local to this function"
        print(f"Local variable (inside function): {local_var}")
        print(f"Global variable (inside function): {global_var}")
    
    print("\nInside function:")
    demo_scope()
    
    print(f"\nOutside function (global still accessible): {global_var}")
    # print(local_var)  # This would cause an error


if __name__ == "__main__":
    print("Python Functions Tutorial\n")
    
    simple_function_demo()
    function_with_parameters()
    function_with_return()
    function_documentation()
    real_world_functions()
    variable_scope()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("- Define functions with 'def' keyword")
    print("- Functions can have parameters (inputs)")
    print("- Functions can return values (outputs)")
    print("- Use docstrings to document functions")
    print("- Functions reduce code repetition and improve organization")
    print("=" * 70)
