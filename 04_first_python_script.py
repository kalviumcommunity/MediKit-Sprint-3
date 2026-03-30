#!/usr/bin/env python3
"""
First Python Script for Data Analysis

This is a beginner-friendly introduction to writing Python scripts
for data analysis. We'll load some sample data and perform basic analysis.
"""

import json


def load_sample_data():
    """
    Load sample student data for analysis.
    
    Returns:
        list: A list of dictionaries containing student information
    """
    # Sample student data
    students = [
        {"name": "Alice", "math_score": 85, "science_score": 90, "english_score": 88},
        {"name": "Bob", "math_score": 92, "science_score": 88, "english_score": 85},
        {"name": "Charlie", "math_score": 78, "science_score": 82, "english_score": 95},
        {"name": "Diana", "math_score": 88, "science_score": 91, "english_score": 89},
        {"name": "Eva", "math_score": 95, "science_score": 94, "english_score": 91},
    ]
    return students


def calculate_average_score(students):
    """
    Calculate the average score for each subject.
    
    Args:
        students (list): List of student dictionaries
    
    Returns:
        dict: Dictionary with average scores for each subject
    """
    if not students:
        return {"math": 0, "science": 0, "english": 0}
    
    # Initialize totals
    total_math = 0
    total_science = 0
    total_english = 0
    
    # Sum all scores
    for student in students:
        total_math += student["math_score"]
        total_science += student["science_score"]
        total_english += student["english_score"]
    
    # Calculate averages
    num_students = len(students)
    averages = {
        "math": total_math / num_students,
        "science": total_science / num_students,
        "english": total_english / num_students,
    }
    
    return averages


def find_top_student(students):
    """
    Find the student with the highest average score.
    
    Args:
        students (list): List of student dictionaries
    
    Returns:
        tuple: (student_name, average_score)
    """
    if not students:
        return None, 0
    
    top_student = None
    top_average = 0
    
    for student in students:
        # Calculate average score for this student
        average = (
            student["math_score"] +
            student["science_score"] +
            student["english_score"]
        ) / 3
        
        # Update top student if this one is better
        if average > top_average:
            top_average = average
            top_student = student["name"]
    
    return top_student, top_average


def print_analysis_report(students):
    """
    Print a formatted analysis report of student data.
    
    Args:
        students (list): List of student dictionaries
    """
    print("=" * 60)
    print("STUDENT DATA ANALYSIS REPORT")
    print("=" * 60)
    
    # Print individual student scores
    print("\n1. INDIVIDUAL STUDENT SCORES:")
    print("-" * 60)
    for student in students:
        name = student["name"]
        math = student["math_score"]
        science = student["science_score"]
        english = student["english_score"]
        average = (math + science + english) / 3
        
        print(f"{name:12} | Math: {math:3} | Science: {science:3} | "
              f"English: {english:3} | Avg: {average:.1f}")
    
    # Print subject averages
    print("\n2. SUBJECT AVERAGES:")
    print("-" * 60)
    averages = calculate_average_score(students)
    print(f"Math Average:     {averages['math']:.2f}")
    print(f"Science Average:  {averages['science']:.2f}")
    print(f"English Average:  {averages['english']:.2f}")
    
    # Print top student
    print("\n3. TOP PERFORMER:")
    print("-" * 60)
    top_name, top_avg = find_top_student(students)
    print(f"Student: {top_name}")
    print(f"Average Score: {top_avg:.2f}")
    
    print("\n" + "=" * 60)


def main():
    """
    Main function to execute the data analysis script.
    
    This is the entry point of our script. It:
    1. Loads sample data
    2. Analyzes the data
    3. Prints results
    """
    print("Starting Data Analysis Script...\n")
    
    # Load the data
    print("Step 1: Loading sample student data...")
    students = load_sample_data()
    print(f"Loaded {len(students)} student records.\n")
    
    # Perform analysis
    print("Step 2: Analyzing the data...")
    print("Running calculations...\n")
    
    # Generate and print report
    print("Step 3: Generating analysis report...\n")
    print_analysis_report(students)
    
    print("\nData analysis complete!")
    print("This is a basic demonstration of Python script structure.")


# Script execution
if __name__ == "__main__":
    # This ensures the main() function only runs when the script is executed directly,
    # not when it's imported as a module by another script
    main()
