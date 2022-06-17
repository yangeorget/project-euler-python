def solve():
    nb = 0
    for l2 in range(0, 2):
        remainder = 200 - l2 * 200
        if remainder == 0:
            print(f"l2={l2}")
            nb += 1
        else:
            for l1 in range(0, 1 + remainder//100):
                remainder = 200 - l2 * 200 - l1 * 100
                if remainder == 0:
                    print(f"l2={l2},l1={l1}")
                    nb += 1
                else:
                    for p50 in range(0, 1 + remainder // 50):
                        remainder = 200 - l2 * 200 - l1 * 100 - p50 * 50
                        if remainder == 0:
                            print(f"l2={l2},l1={l1},p50={p50}")
                            nb += 1
                        else:
                            for p20 in range(0,  1 + remainder // 20):
                                remainder = 200 - l2 * 200 - l1 * 100 - p50 * 50 - p20 * 20
                                if remainder == 0:
                                    print(f"l2={l2},l1={l1},p50={p50},p20={p20}")
                                    nb += 1
                                else:
                                    for p10 in range(0, 1 + remainder // 10):
                                        remainder = 200 - l2 * 200 - l1 * 100 - p50 * 50 - p20 * 20 - p10 * 10
                                        if remainder == 0:
                                            print(f"l2={l2},l1={l1},p50={p50},p20={p20},p10={p10}")
                                            nb += 1
                                        else:
                                            for p5 in range(0, 1 + remainder // 5):
                                                remainder = 200 - l2 * 200 - l1 * 100 - p50 * 50 - p20 * 20 - p10 * 10 - p5 * 5
                                                if remainder == 0:
                                                    print(f"l2={l2},l1={l1},p50={p50},p20={p20},p10={p10},p5={p5}")
                                                    nb += 1
                                                else:
                                                    for p2 in range(0, 1 + remainder // 2):
                                                        remainder = 200 - l2 * 200 - l1 * 100 - p50 * 50 - p20 * 20 - p10 * 10 - p5 * 5 - p2*2
                                                        p1 = remainder
                                                        print(f"l2={l2},l1={l1},p50={p50},p20={p20},p10={p10},p5={p5},p2={p2},p1={p1}")
                                                        nb += 1
    return nb