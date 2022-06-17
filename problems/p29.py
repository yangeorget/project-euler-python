def solve():
    values = {}
    for a in range(2, 101):
        for b in range(2, 101):
            if a**b in values:
                print(values[a**b], f"{a}**{b}")
            else:
                values[a**b] = f"{a}**{b}"
    return len(values)