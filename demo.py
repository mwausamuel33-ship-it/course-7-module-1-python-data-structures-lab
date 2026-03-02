#!/usr/bin/env python3
"""
Student Data Management System Demo
This shows how the system works. I'm learning Python so this is my first project!
"""

# Import all the functions I created
from lib.student_data import students
from lib.filters import filter_students_by_major
from lib.data_processing import format_student_data, display_students
from lib.set_operations import unique_majors
from lib.data_generator import student_generator

def main():
    print("=" * 60)
    print("STUDENT DATA MANAGEMENT SYSTEM DEMO")
    print("This is my first Python project! Hope you like it!")
    print("=" * 60)
    
    # 1. Show all students in the system
    print("\n1. ALL STUDENTS IN THE SYSTEM:")
    print("-" * 40)
    display_students(students)
    
    # 2. Filter students by major
    print("\n2. FILTERING STUDENTS BY MAJOR:")
    print("-" * 40)
    
    # Find Computer Science students
    cs_students = filter_students_by_major(students, "Computer Science")
    print(f"Found {len(cs_students)} Computer Science students:")
    for student in cs_students:
        print(f"  {format_student_data(student)}")
    
    # Find Mathematics students  
    math_students = filter_students_by_major(students, "Mathematics")
    print(f"\nFound {len(math_students)} Mathematics students:")
    for student in math_students:
        print(f"  {format_student_data(student)}")
    
    # 3. Show what different majors we have (using sets)
    print("\n3. UNIQUE MAJORS IN THE SYSTEM:")
    print("-" * 40)
    majors = unique_majors(students)
    print(f"We have students in these majors: {sorted(majors)}")
    
    # 4. Show how generators work (memory efficient way)
    print("\n4. USING GENERATORS (memory efficient):")
    print("-" * 40)
    
    # Create a generator for Physics students
    physics_gen = student_generator(students, "Physics")
    print("Getting Physics students one by one using a generator:")
    student_count = 0
    try:
        while True:
            student = next(physics_gen)
            student_count += 1
            print(f"  Student {student_count}: {format_student_data(student)}")
    except StopIteration:
        print(f"  No more Physics students found. Total: {student_count}")
    
    # 5. Show that filtering works with different cases
    print("\n5. CASE-INSENSITIVE FILTERING:")
    print("-" * 40)
    cs_students_lower = filter_students_by_major(students, "computer science")
    print(f"Filtering by 'computer science' (all lowercase): found {len(cs_students_lower)} students")
    print("This shows the system works even if you type the major in different ways!")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE!")
    print("Thanks for checking out my Student Data Management System!")
    print("I learned a lot about Python data structures making this!")
    print("=" * 60)

# Run the demo when this file is executed
if __name__ == "__main__":
    main()
