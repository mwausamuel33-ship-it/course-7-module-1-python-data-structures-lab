# This module contains functions to lazily generate student data.
# I'm learning about generators and how they save memory

def student_generator(student_list, major):
    """
    This function creates a generator that gives us students one by one.
    Generators are good for memory because they don't create the whole list at once.
    """
    # Using a generator function with yield
    for student in student_list:
        # Check if this student's major matches what we want
        if student[2].lower() == major.lower():
            yield student
