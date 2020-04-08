def problem1(lower_bound, upper_bound, num_inc):
    for speed in range(lower_bound, upper_bound + num_inc, num_inc):
        kmh = speed
        mph = speed * 0.6214
        print("Kph: " + str(kmh) + "    Mph: " + str(mph))

def problem2(grades, average):
    student_average = 0.15 * grades[0] + 0.15 * grades[1] + 0.3 * grades[2] + 0.4 * grades[3]
    if student_average > average:
        print("The student's grade is above the class average.")
    elif student_average < average:
        print("The student's grade is below the class average.")
    else:
        print("The student's grade is equal to the class average.")
    return student_average
    
