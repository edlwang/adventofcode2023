with open("day1/input.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        ptr = 0
        while not line[ptr].isnumeric():
            ptr += 1
        sum += 10 * int(line[ptr])
        ptr = len(line) - 1
        while not line[ptr].isnumeric():
            ptr -= 1
        sum += int(line[ptr])
    print(sum)
