# This module contains functions for filtering student data.
# I'm learning about list comprehensions so I'm using them here

def filter_students_by_major(student_list, major):
    """
    This function filters students by their major.
    It looks at each student and checks if their major matches what we're looking for.
    I'm using a list comprehension because it's shorter than a for loop.
    """
    # student[2] is the major part of the tuple (ID, Name, Major)
    # .lower() makes it case insensitive so "Computer Science" and "computer science" both work
    filtered_students = []
    for student in student_list:
        if student[2].lower() == major.lower():
            filtered_students.append(student)
    
    return filtered_students
