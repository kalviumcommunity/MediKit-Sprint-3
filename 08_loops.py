#!/usr/bin/env python3
"""
Using for and while Loops

Loops allow us to repeat code multiple times, which is essential for
iterating over data, processing collections, and automating tasks.
"""


def for_loop_basics():
    """
    Demonstrate basic for loops.
    
    For loops iterate over sequences like lists, strings, or ranges.
    """
    print("=" * 70)
    print("FOR LOOP BASICS")
    print("=" * 70)
    
    # Example 1: Loop through a list
    print("\n1. LOOP THROUGH A LIST")
    print("-" * 70)
    fruits = ["apple", "banana", "cherry"]
    print(f"fruits = {fruits}\n")
    
    print("for fruit in fruits:")
    for fruit in fruits:
        print(f"  {fruit}")
    
    # Example 2: Loop with range()
    print("\n2. LOOP WITH range()")
    print("-" * 70)
    print("for i in range(5):")
    for i in range(5):
        print(f"  i = {i}")
    
    # Example 3: range() with start and stop
    print("\n3. RANGE WITH START AND STOP")
    print("-" * 70)
    print("for i in range(2, 6):")
    for i in range(2, 6):
        print(f"  i = {i}")
    
    # Example 4: range() with step
    print("\n4. RANGE WITH STEP")
    print("-" * 70)
    print("for i in range(0, 10, 2):")
    for i in range(0, 10, 2):
        print(f"  i = {i}")


def for_loop_advanced():
    """
    Demonstrate advanced for loop patterns.
    """
    print("\n" + "=" * 70)
    print("ADVANCED FOR LOOP PATTERNS")
    print("=" * 70)
    
    # Example 1: Loop through string
    print("\n1. LOOP THROUGH CHARACTERS IN A STRING")
    print("-" * 70)
    word = "PYTHON"
    print(f"word = '{word}'\n")
    print("for char in word:")
    for char in word:
        print(f"  {char}")
    
    # Example 2: Loop with enumerate() - get index and value
    print("\n2. LOOP WITH enumerate() - INDEX AND VALUE")
    print("-" * 70)
    students = ["Alice", "Bob", "Charlie"]
    print(f"students = {students}\n")
    print("for index, student in enumerate(students):")
    for index, student in enumerate(students):
        print(f"  {index}: {student}")
    
    # Example 3: Loop through dictionary
    print("\n3. LOOP THROUGH DICTIONARY")
    print("-" * 70)
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
    print(f"scores = {scores}\n")
    
    print("for name, score in scores.items():")
    for name, score in scores.items():
        print(f"  {name}: {score}")
    
    # Example 4: Nested loops
    print("\n4. NESTED LOOPS")
    print("-" * 70)
    print("for i in range(3):")
    print("  for j in range(3):")
    for i in range(3):
        for j in range(3):
            print(f"  i={i}, j={j}")
    
    # Example 5: Break statement
    print("\n5. BREAK STATEMENT (exit loop early)")
    print("-" * 70)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"numbers = {numbers}\n")
    print("for num in numbers:")
    print("  if num == 5:")
    print("    break")
    for num in numbers:
        if num == 5:
            print(f"  Found 5! Breaking...")
            break
        print(f"  {num}")
    
    # Example 6: Continue statement
    print("\n6. CONTINUE STATEMENT (skip current iteration)")
    print("-" * 70)
    print("for num in range(1, 6):")
    print("  if num == 3:")
    print("    continue")
    for num in range(1, 6):
        if num == 3:
            continue
        print(f"  {num}")


def while_loop_basics():
    """
    Demonstrate basic while loops.
    
    While loops repeat code while a condition is true.
    """
    print("\n" + "=" * 70)
    print("WHILE LOOP BASICS")
    print("=" * 70)
    
    # Example 1: Simple while loop
    print("\n1. SIMPLE WHILE LOOP")
    print("-" * 70)
    print("count = 0")
    print("while count < 5:")
    print("  print(count)")
    print("  count += 1")
    count = 0
    while count < 5:
        print(f"  {count}")
        count += 1
    
    # Example 2: While with user-like condition
    print("\n2. WHILE LOOP WITH CONDITION CHECK")
    print("-" * 70)
    password = ""
    correct_password = "secret123"
    attempts = 0
    
    print(f"Correct password: '{correct_password}'")
    print(f"Let's simulate password attempts:\n")
    
    # Simulate 3 attempts
    test_passwords = ["wrong", "secret", "secret123"]
    for test_pwd in test_passwords:
        attempts += 1
        print(f"Attempt {attempts}: trying '{test_pwd}'")
        if test_pwd == correct_password:
            print("  Password correct!")
            break
        else:
            print("  Wrong password.")


def while_loop_patterns():
    """
    Demonstrate common while loop patterns.
    """
    print("\n" + "=" * 70)
    print("WHILE LOOP PATTERNS")
    print("=" * 70)
    
    # Example 1: Countdown
    print("\n1. COUNTDOWN")
    print("-" * 70)
    print("Countdown from 5:\n")
    countdown = 5
    while countdown > 0:
        print(f"  {countdown}...")
        countdown -= 1
    print("  Blastoff!")
    
    # Example 2: Sum until condition
    print("\n2. SUM UNTIL CONDITION")
    print("-" * 70)
    total = 0
    number = 1
    print("Summing numbers from 1 until sum exceeds 20:\n")
    while total <= 20:
        total += number
        print(f"  Added {number}, total: {total}")
        number += 1
    
    # Example 3: While with break
    print("\n3. WHILE WITH BREAK")
    print("-" * 70)
    print("Finding first even number starting from 1:\n")
    n = 1
    while True:
        print(f"  Checking {n}...")
        if n % 2 == 0:
            print(f"  Found even number: {n}")
            break
        n += 1
    
    # Example 4: While with continue
    print("\n4. WHILE WITH CONTINUE (skip to next iteration)")
    print("-" * 70)
    print("Printing numbers 1-10, skipping even numbers:\n")
    num = 0
    while num < 10:
        num += 1
        if num % 2 == 0:
            continue
        print(f"  {num}")


def practical_examples():
    """
    Practical real-world examples using loops.
    """
    print("\n" + "=" * 70)
    print("PRACTICAL EXAMPLES")
    print("=" * 70)
    
    # Example 1: Calculate average
    print("\n1. CALCULATE AVERAGE OF SCORES")
    print("-" * 70)
    scores = [85, 92, 78, 88, 95]
    total = 0
    count = 0
    
    for score in scores:
        total += score
        count += 1
    
    average = total / count if count > 0 else 0
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    
    # Example 2: Filter data
    print("\n2. FILTER PASSING GRADES (>= 80)")
    print("-" * 70)
    test_scores = [75, 85, 92, 78, 88, 95, 70]
    passing_scores = []
    
    for score in test_scores:
        if score >= 80:
            passing_scores.append(score)
    
    print(f"All scores: {test_scores}")
    print(f"Passing scores: {passing_scores}")
    
    # Example 3: Transform data
    print("\n3. TRANSFORM CELSIUS TO FAHRENHEIT")
    print("-" * 70)
    celsius_temps = [0, 10, 20, 30, 40]
    fahrenheit_temps = []
    
    for celsius in celsius_temps:
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_temps.append(fahrenheit)
    
    print("Celsius -> Fahrenheit conversion:")
    for c, f in zip(celsius_temps, fahrenheit_temps):
        print(f"  {c}°C = {f:.1f}°F")
    
    # Example 4: Process nested data
    print("\n4. PROCESS STUDENT DATA")
    print("-" * 70)
    students = [
        {"name": "Alice", "scores": [95, 92, 98]},
        {"name": "Bob", "scores": [87, 90, 85]},
        {"name": "Charlie", "scores": [92, 94, 91]},
    ]
    
    for student in students:
        average = sum(student["scores"]) / len(student["scores"])
        print(f"{student['name']}: Average = {average:.1f}")


if __name__ == "__main__":
    print("Python Loops Tutorial: for and while\n")
    
    for_loop_basics()
    for_loop_advanced()
    while_loop_basics()
    while_loop_patterns()
    practical_examples()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("- for loop: Iterate over sequences (list, string, range)")
    print("- while loop: Repeat while a condition is true")
    print("- break: Exit loop immediately")
    print("- continue: Skip current iteration")
    print("- Loops are essential for data processing and automation")
    print("=" * 70)
