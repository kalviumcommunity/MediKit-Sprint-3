#!/usr/bin/env python3
"""
Working with Python Lists, Tuples, and Dictionaries

These are fundamental collection data types in Python for storing and
organizing multiple values. Essential for data analysis and manipulation.
"""


def lists_demo():
    """
    Demonstrate Python lists - mutable ordered collections.
    
    Lists are:
    - Ordered: Items have a position
    - Mutable: Can be modified after creation
    - Indexed: Access items by position
    - Heterogeneous: Can contain different types
    """
    print("=" * 70)
    print("LISTS - MUTABLE ORDERED COLLECTIONS")
    print("=" * 70)
    
    # Create lists
    print("\n1. CREATING LISTS")
    print("-" * 70)
    empty_list = []
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    students = ["Alice", "Bob", "Charlie"]
    
    print(f"empty_list: {empty_list}")
    print(f"numbers: {numbers}")
    print(f"mixed: {mixed}")
    print(f"students: {students}")
    
    # Accessing elements
    print("\n2. ACCESSING ELEMENTS")
    print("-" * 70)
    print(f"students[0]: {students[0]}")
    print(f"students[1]: {students[1]}")
    print(f"students[-1]: {students[-1]}")  # Last element
    print(f"students[0:2]: {students[0:2]}")  # Slicing
    
    # Modifying lists
    print("\n3. MODIFYING LISTS")
    print("-" * 70)
    scores = [85, 92, 78]
    print(f"Original: {scores}")
    
    scores[0] = 90  # Change element
    print(f"After scores[0] = 90: {scores}")
    
    scores.append(88)  # Add to end
    print(f"After append(88): {scores}")
    
    scores.insert(1, 87)  # Insert at position
    print(f"After insert(1, 87): {scores}")
    
    scores.remove(87)  # Remove specific value
    print(f"After remove(87): {scores}")
    
    popped = scores.pop()  # Remove and return last
    print(f"After pop(): {scores}, popped value: {popped}")
    
    # Common list operations
    print("\n4. COMMON LIST OPERATIONS")
    print("-" * 70)
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original list: {data}")
    print(f"len(data): {len(data)}")
    print(f"min(data): {min(data)}")
    print(f"max(data): {max(data)}")
    print(f"sum(data): {sum(data)}")
    
    sorted_data = sorted(data)
    print(f"sorted(data): {sorted_data}")
    
    data.sort()
    print(f"After sort(): {data}")
    
    reversed_data = list(reversed(data))
    print(f"reversed(): {reversed_data}")
    
    # List comprehension
    print("\n5. LIST COMPREHENSION")
    print("-" * 70)
    numbers = [1, 2, 3, 4, 5]
    squared = [x**2 for x in numbers]
    print(f"Original: {numbers}")
    print(f"Squared [x**2 for x in numbers]: {squared}")
    
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Evens [x for x in numbers if x % 2 == 0]: {evens}")


def tuples_demo():
    """
    Demonstrate Python tuples - immutable ordered collections.
    
    Tuples are:
    - Ordered: Items have a position
    - Immutable: Cannot be modified after creation
    - Indexed: Access items by position
    - Hashable: Can be used as dictionary keys
    """
    print("\n" + "=" * 70)
    print("TUPLES - IMMUTABLE ORDERED COLLECTIONS")
    print("=" * 70)
    
    # Create tuples
    print("\n1. CREATING TUPLES")
    print("-" * 70)
    empty_tuple = ()
    coordinates = (10, 20)
    rgb_color = (255, 128, 0)
    mixed = (1, "hello", 3.14)
    single = (42,)  # Need comma for single element
    
    print(f"empty_tuple: {empty_tuple}")
    print(f"coordinates: {coordinates}")
    print(f"rgb_color: {rgb_color}")
    print(f"mixed: {mixed}")
    print(f"single: {single}")
    
    # Accessing elements
    print("\n2. ACCESSING ELEMENTS")
    print("-" * 70)
    print(f"rgb_color[0]: {rgb_color[0]}")
    print(f"rgb_color[1]: {rgb_color[1]}")
    print(f"rgb_color[-1]: {rgb_color[-1]}")
    print(f"rgb_color[0:2]: {rgb_color[0:2]}")
    
    # Tuple unpacking
    print("\n3. TUPLE UNPACKING")
    print("-" * 70)
    point = (5, 10)
    x, y = point
    print(f"point = {point}")
    print(f"x, y = point")
    print(f"x = {x}, y = {y}")
    
    rgb_tuple = (200, 100, 50)
    r, g, b = rgb_tuple
    print(f"\nrgb_tuple = {rgb_tuple}")
    print(f"r, g, b = {r}, {g}, {b}")
    
    # Tuple operations
    print("\n4. TUPLE OPERATIONS")
    print("-" * 70)
    t1 = (1, 2, 3)
    t2 = (4, 5, 6)
    combined = t1 + t2
    print(f"{t1} + {t2} = {combined}")
    
    repeated = t1 * 3
    print(f"{t1} * 3 = {repeated}")
    
    print(f"len({t1}): {len(t1)}")
    print(f"count 3 in {t1}: {t1.count(3)}")
    
    # Immutability demonstration
    print("\n5. IMMUTABILITY (Cannot modify)")
    print("-" * 70)
    try:
        t = (1, 2, 3)
        t[0] = 10  # This will raise an error
    except TypeError as e:
        print(f"Error: Cannot modify tuple - {e}")


def dictionaries_demo():
    """
    Demonstrate Python dictionaries - mutable key-value pairs.
    
    Dictionaries are:
    - Mutable: Can be modified after creation
    - Unordered (in older Python) / Ordered (Python 3.7+)
    - Key-Value pairs: Access by key, not index
    - Flexible keys: Keys must be hashable
    """
    print("\n" + "=" * 70)
    print("DICTIONARIES - KEY-VALUE COLLECTIONS")
    print("=" * 70)
    
    # Create dictionaries
    print("\n1. CREATING DICTIONARIES")
    print("-" * 70)
    empty_dict = {}
    person = {"name": "Alice", "age": 30, "city": "New York"}
    scores = {"math": 95, "english": 88, "science": 92}
    mixed_keys = {1: "one", "two": 2, 3.0: "three"}
    
    print(f"empty_dict: {empty_dict}")
    print(f"person: {person}")
    print(f"scores: {scores}")
    print(f"mixed_keys: {mixed_keys}")
    
    # Accessing values
    print("\n2. ACCESSING VALUES")
    print("-" * 70)
    print(f"person['name']: {person['name']}")
    print(f"person['age']: {person['age']}")
    print(f"scores['math']: {scores['math']}")
    
    # Safe access with get()
    print(f"person.get('name'): {person.get('name')}")
    print(f"person.get('phone', 'Not provided'): {person.get('phone', 'Not provided')}")
    
    # Modifying dictionaries
    print("\n3. MODIFYING DICTIONARIES")
    print("-" * 70)
    student = {"name": "Bob", "grade": 85}
    print(f"Original: {student}")
    
    student["grade"] = 90  # Update value
    print(f"After updating grade: {student}")
    
    student["email"] = "bob@email.com"  # Add new key-value
    print(f"After adding email: {student}")
    
    del student["email"]  # Delete key-value
    print(f"After deleting email: {student}")
    
    # Dictionary methods
    print("\n4. DICTIONARY METHODS")
    print("-" * 70)
    data = {"x": 10, "y": 20, "z": 30}
    print(f"Dictionary: {data}")
    print(f"keys(): {list(data.keys())}")
    print(f"values(): {list(data.values())}")
    print(f"items(): {list(data.items())}")
    
    # Dictionary iteration
    print("\n5. ITERATING DICTIONARIES")
    print("-" * 70)
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
    print(f"Dictionary: {scores}")
    
    print("\nIterating keys:")
    for name in scores:
        print(f"  {name}: {scores[name]}")
    
    print("\nIterating items:")
    for name, score in scores.items():
        print(f"  {name}: {score}")


def data_structure_examples():
    """
    Real-world data structure examples.
    """
    print("\n" + "=" * 70)
    print("REAL-WORLD DATA STRUCTURE EXAMPLES")
    print("=" * 70)
    
    # Student records as list of dictionaries
    print("\n1. STUDENT RECORDS (List of Dictionaries)")
    print("-" * 70)
    students = [
        {"id": 1, "name": "Alice", "scores": [95, 92, 98]},
        {"id": 2, "name": "Bob", "scores": [87, 90, 85]},
        {"id": 3, "name": "Charlie", "scores": [92, 94, 91]},
    ]
    
    for student in students:
        avg_score = sum(student["scores"]) / len(student["scores"])
        print(f"{student['name']}: Average score = {avg_score:.1f}")


if __name__ == "__main__":
    print("Python Collections: Lists, Tuples, and Dictionaries\n")
    
    lists_demo()
    tuples_demo()
    dictionaries_demo()
    data_structure_examples()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("- Lists: Mutable, ordered, use for changing collections")
    print("- Tuples: Immutable, ordered, use for fixed data")
    print("- Dictionaries: Key-value pairs, use for structured data")
    print("- Combine them for complex data structures")
    print("=" * 70)
