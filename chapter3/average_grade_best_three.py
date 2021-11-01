def average_grade_best_three(grade1, grade2, grade3, grade4):
    """
    Calculates the average grade between the 3 grades given between 0 and 100

    example:
    average_grade_best_three(37.5, 4, 5.2, 4)
    15.57
    """
    total_grade = grade1 + grade2 + grade3 + grade4 
    lowest_grade = min(grade1, grade2, grade3, grade4)
    
    return round((total_grade - lowest_grade) / 3, 2)


