# Rainfall program

# -------------------------
# Subprograms
# -------------------------
def analyse1(data):
    count = 0
    average = 0
    highest = 0
    for value in data:
        if value == 0:
            count = count + 1
        average = average + value
        if value > highest:
            highest = value
    average = average / len(data)
    return count, average, highest


def analyse2(data):
    count = 0
    for index in range(len(data)):
        if data[index] == 0:
            count = count + 1
    return count


# -------------------------
# Main program
# -------------------------
daily_rainfall_mm = [0.1, 0.0, 0.2, 0.4, 0.1, 0.0, 0.0,
                     0.0, 0.3, 0.3, 0.2, 0.0, 0.0, 0.1]
analyse = analyse1(daily_rainfall_mm)
print(f"days weith no rain: {analyse[0]}")
print(f"average: {analyse[1]}")
print(f"highest: {analyse[2]}")