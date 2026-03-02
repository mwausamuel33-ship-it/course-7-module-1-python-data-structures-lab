# This module contains functions to process student data.
# I'm learning how to format strings and display information

def format_student_data(student):
    """
    This function formats student data to look nice when printed.
    It takes a student tuple and makes it into a readable string.
    """
    # Unpacking the tuple into separate variables
    student_id = student[0]
    name = student[1]
    major = student[2]
    
    # Using f-string to format the output nicely
    formatted_string = f"ID: {student_id} | Name: {name} | Major: {major}"
    return formatted_string

def display_students(student_list):
    """
    This function shows all the students in the list.
    It goes through each student and prints their information.
    """
    # Loop through each student in the list
    for student in student_list:
        # Format the student data and print it
        student_info = format_student_data(student)
        print(student_info)
