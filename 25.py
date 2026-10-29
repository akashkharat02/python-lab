
def display_highest_and_lowest():
    if student_grades:
        print(f"Highest grade: {max(student_grades)}")
        print(f"Lowest grade: {min(student_grades)}")
    else:
        print("No grades available.")

add_student("Akash", 60)
add_student("vijay", 100)
add_student("Ranjit", 66)

update_grade("Akash", 60)

remove_student("Ranjit")

display_average_grade()

display_highest_and_lowest()