with open("../res/diag") as f:
    values = [n.strip() for n in f]
    zeros = 0
    ones = 0

    for i, val in enumerate(values):
        if int(val[0]) == 0:
            zeros += 1
        else:
            ones += 1

    print(zeros, ones)
    print(values)
