def simple_nav():
    with open("../res/navigation") as f:
        hor, depth = 0, 0
        #navigation = dict((nav.split(" ")[0], nav.split(" ")[1].strip("\n")) for nav in f)
        #print(navigation)
        for nav in f:
            val = int(nav.split(" ")[1])
            if "forward" in nav:
                hor += val
            elif "up" in nav:
                depth -= val
            else:
                depth += val

        print(f"Simple navigation values:\nHorizontal: {hor} | Depth: {depth}")
        print(f"Multiplied result: {hor * depth}\n")


def correct_nav():
    with open("../res/navigation") as f:
        hor, depth, aim = 0, 0, 0
        for nav in f:
            val = int(nav.split(" ")[1])
            if "forward" in nav:
                hor += val
                depth += aim * val
            elif "up" in nav:
                aim -= val
            else:
                aim += val

        print(f"Correct navigation values:\nHorizontal: {hor} | Depth: {depth} | Aim: {aim}")
        print(f"Multiplied result: {hor * depth}")


if __name__ == "__main__":
    simple_nav()
    correct_nav()
