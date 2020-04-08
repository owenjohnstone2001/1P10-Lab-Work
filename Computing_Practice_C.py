def problem1():
    summation = 0
    for counter in range(0,30):
        summation += (counter + 1) / (30 - counter)
    return round(summation, 2)

def problem2(int_values):
    total_savings = 0
    for item in int_values:
        if item >= 100:
            cost = 0.7 * item * 99
            print("Total cost: " + str(cost))
            total_savings += 0.3 * item * 99
        elif item >= 50:
            cost = 0.8 * item * 99
            print("Total cost: " + str(cost))
            total_savings += 0.2 * item * 99
        elif item >= 10:
            cost = 0.9 * item * 99
            print("Total cost: " + str(cost))
            total_savings += 0.1 * item * 99
        else:
            cost = item * 99
            print("Total cost: " + str(cost))
    return total_savings
