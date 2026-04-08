#!/usr/bin/env python3
"""
Writing Conditional Statements (if, elif, else)

Conditional statements allow code to make decisions based on conditions.
They're essential for data validation, filtering, and flow control.
"""


def simple_if_demo():
    """
    Demonstrate simple if statements.
    """
    print("=" * 70)
    print("SIMPLE IF STATEMENTS")
    print("=" * 70)
    
    # Example 1: Basic if
    print("\n1. BASIC IF STATEMENT")
    print("-" * 70)
    age = 18
    print(f"age = {age}")
    
    if age >= 18:
        print("You are an adult.")
    
    # Example 2: If with variable age
    print("\n2. IF WITH DIFFERENT VALUES")
    print("-" * 70)
    for test_age in [15, 18, 25]:
        print(f"age = {test_age}")
        if test_age >= 18:
            print("  You are an adult.")
    
    # Example 3: If with condition check
    print("\n3. IF WITH MULTIPLE CONDITIONS")
    print("-" * 70)
    score = 85
    print(f"score = {score}")
    
    if score >= 60:
        print("Passed the test!")
    
    # Example 4: Boolean variables
    print("\n4. IF WITH BOOLEAN VALUES")
    print("-" * 70)
    is_student = True
    print(f"is_student = {is_student}")
    
    if is_student:
        print("You are a student.")


def if_else_demo():
    """
    Demonstrate if-else statements.
    """
    print("\n" + "=" * 70)
    print("IF-ELSE STATEMENTS")
    print("=" * 70)
    
    # Example 1: Basic if-else
    print("\n1. BASIC IF-ELSE")
    print("-" * 70)
    age = 15
    print(f"age = {age}")
    
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    
    # Example 2: Even/Odd check
    print("\n2. EVEN/ODD CHECK")
    print("-" * 70)
    for num in [8, 11, 24, 17]:
        print(f"num = {num}")
        if num % 2 == 0:
            print(f"  {num} is even")
        else:
            print(f"  {num} is odd")
    
    # Example 3: Grade classification
    print("\n3. GRADE CLASSIFICATION")
    print("-" * 70)
    score = 72
    print(f"score = {score}")
    
    if score >= 90:
        grade = "A"
    else:
        grade = "Not A"
    
    print(f"Grade: {grade}")
    
    # Example 4: Data validation
    print("\n4. DATA VALIDATION")
    print("-" * 70)
    values = [5, 0, -3, 10]
    for val in values:
        print(f"value = {val}")
        if val > 0:
            print(f"  {val} is positive")
        else:
            print(f"  {val} is not positive")


def if_elif_else_demo():
    """
    Demonstrate if-elif-else statements (multiple conditions).
    """
    print("\n" + "=" * 70)
    print("IF-ELIF-ELSE STATEMENTS")
    print("=" * 70)
    
    # Example 1: Grade assignment
    print("\n1. GRADE ASSIGNMENT")
    print("-" * 70)
    scores = [95, 87, 76, 65, 55]
    
    for score in scores:
        print(f"score = {score}")
        
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"  Grade: {grade}")
    
    # Example 2: Temperature categorization
    print("\n2. TEMPERATURE CATEGORIZATION")
    print("-" * 70)
    temperatures = [35, 20, 10, 0, -5]
    
    for temp in temperatures:
        print(f"temperature = {temp}°C")
        
        if temp > 25:
            category = "Hot"
        elif temp > 15:
            category = "Warm"
        elif temp > 5:
            category = "Cool"
        else:
            category = "Cold"
        
        print(f"  Category: {category}")
    
    # Example 3: Age group classification
    print("\n3. AGE GROUP CLASSIFICATION")
    print("-" * 70)
    ages = [5, 12, 18, 35, 65]
    
    for age in ages:
        print(f"age = {age}")
        
        if age < 13:
            group = "Child"
        elif age < 18:
            group = "Teen"
        elif age < 65:
            group = "Adult"
        else:
            group = "Senior"
        
        print(f"  Group: {group}")


def logical_operators_demo():
    """
    Demonstrate logical operators: and, or, not
    """
    print("\n" + "=" * 70)
    print("LOGICAL OPERATORS (and, or, not)")
    print("=" * 70)
    
    # Example 1: AND operator
    print("\n1. AND OPERATOR (both conditions must be True)")
    print("-" * 70)
    age = 20
    has_license = True
    print(f"age = {age}, has_license = {has_license}")
    
    if age >= 18 and has_license:
        print("You can drive.")
    else:
        print("You cannot drive.")
    
    # Example 2: OR operator
    print("\n2. OR OPERATOR (at least one condition must be True)")
    print("-" * 70)
    is_teacher = False
    is_student = True
    print(f"is_teacher = {is_teacher}, is_student = {is_student}")
    
    if is_teacher or is_student:
        print("You are connected to the school.")
    else:
        print("You are not connected to the school.")
    
    # Example 3: NOT operator
    print("\n3. NOT OPERATOR (reverses boolean value)")
    print("-" * 70)
    is_raining = False
    print(f"is_raining = {is_raining}")
    
    if not is_raining:
        print("It's not raining. We can go out!")
    else:
        print("It's raining. Better stay inside.")
    
    # Example 4: Complex conditions
    print("\n4. COMPLEX CONDITIONS")
    print("-" * 70)
    score = 85
    attendance = 95
    print(f"score = {score}, attendance = {attendance}")
    
    if score >= 80 and attendance >= 90:
        print("Excellent performance!")
    elif score >= 70 or attendance >= 85:
        print("Good performance.")
    else:
        print("Needs improvement.")


def comparison_operators():
    """
    Demonstrate comparison operators.
    """
    print("\n" + "=" * 70)
    print("COMPARISON OPERATORS")
    print("=" * 70)
    
    print("\nComparison operators in Python:")
    print("  ==  : Equal to")
    print("  !=  : Not equal to")
    print("  >   : Greater than")
    print("  <   : Less than")
    print("  >=  : Greater than or equal")
    print("  <=  : Less than or equal")
    
    print("\n" + "-" * 70)
    a = 10
    b = 20
    print(f"a = {a}, b = {b}\n")
    
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")
    print(f"a > b: {a > b}")
    print(f"a < b: {a < b}")
    print(f"a >= b: {a >= b}")
    print(f"a <= b: {a <= b}")


def real_world_example():
    """
    Real-world conditional example: Student grade and feedback.
    """
    print("\n" + "=" * 70)
    print("REAL-WORLD EXAMPLE: Student Grade Feedback")
    print("=" * 70)
    
    students = [
        {"name": "Alice", "score": 95, "attendance": 100},
        {"name": "Bob", "score": 78, "attendance": 85},
        {"name": "Charlie", "score": 65, "attendance": 60},
        {"name": "Diana", "score": 88, "attendance": 95},
    ]
    
    print("\nGrade Analysis and Feedback:\n")
    
    for student in students:
        name = student["name"]
        score = student["score"]
        attendance = student["attendance"]
        
        # Determine grade
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "F"
        
        # Generate feedback
        if score >= 90 and attendance >= 90:
            feedback = "Excellent! Keep it up!"
        elif score >= 80 and attendance >= 80:
            feedback = "Good work. Continue improving."
        elif score >= 70:
            feedback = "Satisfactory. Needs improvement."
        else:
            feedback = "Please seek help. Improve attendance too."
        
        print(f"{name}: Grade {grade}, Attendance {attendance}%")
        print(f"  Feedback: {feedback}\n")


if __name__ == "__main__":
    print("Python Conditional Statements Tutorial\n")
    
    simple_if_demo()
    if_else_demo()
    if_elif_else_demo()
    logical_operators_demo()
    comparison_operators()
    real_world_example()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("- if: Execute code if condition is True")
    print("- else: Execute code if condition is False")
    print("- elif: Check multiple conditions")
    print("- and, or, not: Combine and negate conditions")
    print("- Conditionals are key to data validation and flow control")
    print("=" * 70)
