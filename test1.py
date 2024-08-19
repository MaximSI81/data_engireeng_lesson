def standard_deviation(data):
    data = data.split()
    average_value = sum(map(int, data)) / len(data)
    n = 0
    for i in data:
        n += (int(i) - average_value)**2
    sd = (n / (len(data) - 1)) ** 0.5
    return round(sd, 2)

print(standard_deviation('1 5 2 7 1 9 3 8 5 9'))