def problem1(rows, columns):
    for i in range(rows):
        print("*" * columns)

def problem2(num_hours, wage):
    overtime_counter = 0
    for item in num_hours:
        if item <= 40:
            regular_pay = item * wage
            overtime_pay = 0
        else:
            regular_pay = 40 * wage
            overtime_pay = (item - 40) * wage * 1.5
            overtime_counter += 1
        gross_pay = regular_pay + overtime_pay
        print("Gross pay: " + str(gross_pay))
    return overtime_counter
    
    
