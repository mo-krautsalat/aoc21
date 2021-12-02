def single_sonar():
    with open("../res/sonar") as f:
        depths = f.readlines()
        count = 0
        for i, d in enumerate(depths):
            count += int(d) > int(depths[i - 1])
        return count


def sum_of_three_sonar():
    with open("../res/sonar") as f:
        depths = f.readlines()
        count = 0
        sums = [int(d) + int(depths[j + 1]) + int(depths[j + 2]) for j, d in enumerate(depths) if j + 2 < len(depths)]
        for i, d3 in enumerate(sums):
            count += d3 > sums[i - 1]
        return count


if __name__ == "__main__":
    print(f"Single measurements that are greater than the previous: {single_sonar()}")
    print(f"Sum of three measurements that are greater than the previous: {sum_of_three_sonar()}")
