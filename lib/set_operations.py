# This module contains operations related to sets.
# I'm learning about sets and how they only keep unique values

def unique_majors(student_list):
    """
    This function finds all the different majors that students have.
    Sets automatically remove duplicates, so we only get each major once.
    """
    # Create an empty set to store the majors
    unique_majors_set = set()
    
    # Go through each student and add their major to the set
    for student in student_list:
        major = student[2]  # The major is the third item in the tuple
        unique_majors_set.add(major)
    
    return unique_majors_set
