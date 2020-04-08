def problem1(k):
    summation = 0
    for i in range(k+1):
        summation += (3 + (2 * i)) / (2 ** i)
    return round(summation, 2)

def problem2(time):
    hours = int(time / 3600)
    remaining_time = time - (hours * 3600)
    minutes = int(remaining_time / 60)
    seconds = remaining_time - (minutes * 60)
    return [hours, minutes, seconds]
    
