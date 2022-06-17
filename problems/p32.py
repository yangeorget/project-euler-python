def pandigital(a,b,c):
    digits = []
    for digit in str(a):
        digits.append(digit)
    for digit in str(b):
        digits.append(digit)
    for digit in str(c):
        digits.append(digit)
    return "".join(sorted(digits)) == "123456789"

def solve():
    pandigitals = set()
    for a in range(2, 8000):
        for b in range(a, 8000):
            if pandigital(a, b, a*b):
                print(a,b, a*b)
                pandigitals.add(a*b)
    sum = 0
    for p in pandigitals:
        sum += p
    return sum
