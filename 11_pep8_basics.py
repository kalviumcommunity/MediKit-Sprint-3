#!/usr/bin/env python3
"""
Writing Readable Variable Names and Comments (PEP8 Basics)

PEP8 is the Python Enhancement Proposal #8, which defines style guidelines
for writing Python code. Following these conventions makes code more readable
and maintainable for yourself and other developers.
"""


def variable_naming_conventions():
    """
    Demonstrate proper variable naming conventions according to PEP8.
    """
    print("=" * 70)
    print("VARIABLE NAMING CONVENTIONS (PEP8)")
    print("=" * 70)
    
    # Example 1: Good variable names (descriptive, lowercase with underscores)
    print("\n1. GOOD VARIABLE NAMES")
    print("-" * 70)
    print("Use lowercase with underscores (snake_case):")
    print("  - student_name instead of studentName or sn")
    print("  - total_score instead of totalScore or ts")
    print("  - max_age instead of maxAge or ma\n")
    
    # Good examples
    student_name = "Alice"
    total_score = 95
    max_age = 100
    is_active = True
    user_count = 50
    
    print("Good variable names in use:")
    print(f"  student_name = {student_name}")
    print(f"  total_score = {total_score}")
    print(f"  max_age = {max_age}")
    print(f"  is_active = {is_active}")
    print(f"  user_count = {user_count}")
    
    # Example 2: Poor variable names (avoid these)
    print("\n2. POOR VARIABLE NAMES (AVOID)")
    print("-" * 70)
    print("Avoid:")
    print("  - Single letter variables (except loop counters): x, s, d")
    print("  - Ambiguous names: data, value, thing, stuff")
    print("  - camelCase: studentName (use snake_case instead)")
    print("  - ALL_CAPS for variables (only constants)\n")
    
    # Poor examples (for illustration only)
    sn = "Alice"  # Too cryptic
    ts = 95  # Too cryptic
    val = 50  # Ambiguous
    
    print("Poor variable names (don't use these):")
    print(f"  sn = {sn}  # Too abbreviated")
    print(f"  ts = {ts}  # Too abbreviated")
    print(f"  val = {val}  # Too vague")
    
    # Example 3: Boolean variable naming
    print("\n3. BOOLEAN VARIABLE NAMING")
    print("-" * 70)
    print("Use 'is_', 'has_', or 'can_' prefixes for booleans:")
    print("  - is_active instead of active")
    print("  - has_permission instead of permission")
    print("  - can_edit instead of edit\n")
    
    is_student = True
    has_certificate = False
    can_vote = True
    is_valid = True
    
    print("Boolean variable examples:")
    print(f"  is_student = {is_student}")
    print(f"  has_certificate = {has_certificate}")
    print(f"  can_vote = {can_vote}")
    print(f"  is_valid = {is_valid}")
    
    # Example 4: Constant naming
    print("\n4. CONSTANT NAMING")
    print("-" * 70)
    print("Use ALL_CAPS for constants:\n")
    
    # Constants
    PI = 3.14159
    MAX_USERS = 1000
    DATABASE_URL = "localhost:5432"
    DEFAULT_TIMEOUT = 30
    
    print("Constant examples:")
    print(f"  PI = {PI}")
    print(f"  MAX_USERS = {MAX_USERS}")
    print(f"  DATABASE_URL = {DATABASE_URL}")
    print(f"  DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}")


def comment_conventions():
    """
    Demonstrate proper use of comments according to PEP8.
    """
    print("\n" + "=" * 70)
    print("COMMENTING CONVENTIONS (PEP8)")
    print("=" * 70)
    
    # Example 1: Inline comments
    print("\n1. INLINE COMMENTS")
    print("-" * 70)
    print("Use inline comments to explain non-obvious code:")
    print("  - Place comments on same line or line before")
    print("  - Use # followed by space")
    print("  - Keep concise\n")
    
    # Example: Inline comment
    age = 25  # Age of the user in years
    print(f"age = 25  # Age of the user in years")
    
    # Example 2: Block comments
    print("\n2. BLOCK COMMENTS")
    print("-" * 70)
    print("Use block comments for larger explanations:")
    print("  - Start each line with # followed by space")
    print("  - Separate from code with blank line\n")
    
    # This block explains the calculation
    # We multiply the score by the weight factor
    # and then add bonus points for participation
    score = 90
    weight = 0.8
    bonus = 5
    final_score = (score * weight) + bonus
    
    print("Block comment example:")
    print("# This block explains the calculation")
    print("# We multiply the score by weight factor")
    print("# and add bonus points for participation")
    print(f"final_score = {final_score}")
    
    # Example 3: Docstrings
    print("\n3. DOCSTRINGS")
    print("-" * 70)
    print("Use docstrings for functions, classes, and modules:")
    print("  - Use triple quotes")
    print("  - First line is short summary")
    print("  - Longer explanation follows\n")
    
    def calculate_grade(score):
        """
        Calculate letter grade from numeric score.
        
        Args:
            score (int): Numeric score 0-100
            
        Returns:
            str: Letter grade A-F
        """
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        else:
            return "F"
    
    print("Docstring example:")
    print("def calculate_grade(score):")
    print('    """')
    print("    Calculate letter grade from numeric score.")
    print("    ")
    print("    Args:")
    print("        score (int): Numeric score 0-100")
    print("    Returns:")
    print("        str: Letter grade A-F")
    print('    """')


def code_formatting_pep8():
    """
    Demonstrate PEP8 code formatting rules.
    """
    print("\n" + "=" * 70)
    print("CODE FORMATTING (PEP8)")
    print("=" * 70)
    
    # Example 1: Line length
    print("\n1. LINE LENGTH")
    print("-" * 70)
    print("Keep lines under 79 characters for code (88 for Black formatter)")
    print("Break long lines appropriately\n")
    
    # Good - breaks long line
    message = (
        "This is a long message that exceeds the line "
        "length limit and should be split across multiple lines"
    )
    print(f"Message: {message}")
    
    # Example 2: Spacing rules
    print("\n2. SPACING RULES")
    print("-" * 70)
    print("Spacing conventions:")
    print("  - 4 spaces per indentation level")
    print("  - 2 blank lines between functions")
    print("  - 1 blank line between methods in class")
    print("  - Spaces around operators: x = 5 (not x=5)")
    print("  - No space around keyword argument: func(x=5)\n")
    
    # Good spacing
    x = 10  # Space around operator
    y = x + 5  # Space around operator
    print(f"x = {x}, y = {y}")
    
    # Function call with keyword argument (no space)
    result = max(5, 10)
    print(f"max(5, 10) = {result}")
    
    # Example 3: Import statements
    print("\n3. IMPORT STATEMENTS")
    print("-" * 70)
    print("PEP8 import rules:")
    print("  - Imports at top of file")
    print("  - Separate groups: stdlib, third-party, local")
    print("  - One import per line (except 'from x import a, b')\n")
    
    print("Proper import order:")
    print("  import sys")
    print("  import os")
    print("  import json")
    print("")
    print("  import numpy as np")
    print("  import pandas as pd")
    print("")
    print("  from . import local_module")


def function_naming_conventions():
    """
    Demonstrate function and class naming conventions.
    """
    print("\n" + "=" * 70)
    print("FUNCTION AND CLASS NAMING (PEP8)")
    print("=" * 70)
    
    # Example 1: Function names
    print("\n1. FUNCTION NAMING")
    print("-" * 70)
    print("Use lowercase with underscores (snake_case):")
    print("  - calculate_total() instead of calculateTotal()")
    print("  - get_user_age() instead of getUserAge()")
    print("  - is_valid_email() instead of isValidEmail()\n")
    
    def calculate_total(items):
        """Calculate total of items."""
        return sum(items)
    
    def get_user_age(birth_year):
        """Get user age from birth year."""
        return 2024 - birth_year
    
    print("Function examples:")
    print("  calculate_total([10, 20, 30])")
    print("  get_user_age(1990)")
    
    # Example 2: Class names
    print("\n2. CLASS NAMING")
    print("-" * 70)
    print("Use CapWords (PascalCase) for class names:")
    print("  - StudentRecord instead of studentRecord")
    print("  - DataProcessor instead of dataProcessor\n")
    
    class StudentRecord:
        """Represents a student record."""
        pass
    
    class DataProcessor:
        """Processes data."""
        pass
    
    print("Class naming examples:")
    print("  class StudentRecord: ...")
    print("  class DataProcessor: ...")


def real_world_code_example():
    """
    Show a real-world code example following PEP8.
    """
    print("\n" + "=" * 70)
    print("REAL-WORLD CODE EXAMPLE (PEP8 COMPLIANT)")
    print("=" * 70)
    
    print("\nGood PEP8 compliant code:\n")
    
    code_example = '''
# Student grade processor module

# Constants
PASSING_GRADE = 70
EXCELLENT_THRESHOLD = 90

def process_student_grades(student_name, scores):
    """
    Process student grades and determine performance level.
    
    Args:
        student_name (str): Name of the student
        scores (list): List of test scores
        
    Returns:
        dict: Dictionary with results
    """
    # Calculate average score
    average_score = sum(scores) / len(scores)
    
    # Determine performance level
    if average_score >= EXCELLENT_THRESHOLD:
        performance_level = "Excellent"
    elif average_score >= PASSING_GRADE:
        performance_level = "Passing"
    else:
        performance_level = "Needs Improvement"
    
    # Create and return result dictionary
    result = {
        "name": student_name,
        "average": average_score,
        "level": performance_level,
        "is_passing": average_score >= PASSING_GRADE,
    }
    
    return result


# Example usage
if __name__ == "__main__":
    student_data = process_student_grades("Alice", [95, 92, 98])
    print(f"Student: {student_data['name']}")
    print(f"Average: {student_data['average']:.1f}")
    print(f"Level: {student_data['level']}")
    '''
    
    print(code_example)


def anti_patterns():
    """
    Demonstrate code anti-patterns to avoid.
    """
    print("\n" + "=" * 70)
    print("ANTI-PATTERNS TO AVOID")
    print("=" * 70)
    
    print("\n1. AVOID SHORT VARIABLE NAMES")
    print("-" * 70)
    print("Bad:  n = 10  # Unclear what n represents")
    print("Good: student_count = 10  # Clear purpose\n")
    
    print("2. AVOID UNCLEAR ABBREVIATIONS")
    print("-" * 70)
    print("Bad:  stu_dts = []  # What does stu_dts mean?")
    print("Good: student_data = []  # Clear purpose\n")
    
    print("3. AVOID MISSING COMMENTS FOR COMPLEX CODE")
    print("-" * 70)
    print("Bad:  result = [x for x in data if x > 10 and x < 100]")
    print("Good: # Filter outliers between 10 and 100")
    print("      result = [x for x in data if x > 10 and x < 100]\n")
    
    print("4. AVOID VERY LONG LINES")
    print("-" * 70)
    print("Bad:  total = sum([student['grades'] for student in all_students if student['active']])")
    print("Good: active_students = [s for s in all_students if s['active']]")
    print("      total = sum([s['grades'] for s in active_students])\n")


if __name__ == "__main__":
    print("PEP8: Writing Readable Python Code\n")
    
    variable_naming_conventions()
    comment_conventions()
    code_formatting_pep8()
    function_naming_conventions()
    real_world_code_example()
    anti_patterns()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("- Use snake_case for variables and functions")
    print("- Use UPPER_CASE for constants")
    print("- Use PascalCase for class names")
    print("- Write clear, descriptive variable names")
    print("- Add meaningful comments and docstrings")
    print("- Keep lines under 79-88 characters")
    print("- Follow PEP8 for professional, readable code")
    print("=" * 70)
