def solve():
    sum_of_numbers = 0
    for a in range(2, 295246):
        sum = 0
        for digit in str(a):
            sum += int(digit)**5
        if sum == a:
            print(a)
            sum_of_numbers += a
    return sum_of_numbers