#!/usr/bin/env python3
"""
Student Data Management System Demo
Demonstrates the functionality of the implemented system.
"""

from lib.student_data import students
from lib.filters import filter_students_by_major
from lib.data_processing import format_student_data, display_students
from lib.set_operations import unique_majors
from lib.data_generator import student_generator

def main():
    print("=" * 60)
    print("STUDENT DATA MANAGEMENT SYSTEM DEMO")
    print("=" * 60)
    
    # 1. Display all students
    print("\n1. ALL STUDENTS:")
    print("-" * 40)
    display_students(students)
    
    # 2. Filter students by major using list comprehensions
    print("\n2. FILTERING STUDENTS BY MAJOR:")
    print("-" * 40)
    
    cs_students = filter_students_by_major(students, "Computer Science")
    print(f"Computer Science students ({len(cs_students)}):")
    for student in cs_students:
        print(f"  {format_student_data(student)}")
    
    math_students = filter_students_by_major(students, "Mathematics")
    print(f"\nMathematics students ({len(math_students)}):")
    for student in math_students:
        print(f"  {format_student_data(student)}")
    
    # 3. Display unique majors using set operations
    print("\n3. UNIQUE MAJORS (using set operations):")
    print("-" * 40)
    majors = unique_majors(students)
    print(f"Available majors: {sorted(majors)}")
    
    # 4. Demonstrate generator expressions for memory efficiency
    print("\n4. GENERATOR EXPRESSIONS (memory efficient):")
    print("-" * 40)
    
    # Create a generator for Physics students
    physics_gen = student_generator(students, "Physics")
    print("Physics students (using generator):")
    try:
        while True:
            student = next(physics_gen)
            print(f"  {format_student_data(student)}")
    except StopIteration:
        print("  (No more Physics students)")
    
    # 5. Demonstrate case-insensitive filtering
    print("\n5. CASE-INSENSITIVE FILTERING:")
    print("-" * 40)
    cs_students_lower = filter_students_by_major(students, "computer science")
    print(f"Filtering by 'computer science' (lowercase): {len(cs_students_lower)} students found")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE - All functionality working correctly!")
    print("=" * 60)

if __name__ == "__main__":
    main()