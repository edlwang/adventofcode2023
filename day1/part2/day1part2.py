text_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_num(s):
    for (k, v) in text_to_num.items():
        if k in s:
            return v
    return 0

with open("day1/input.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        nums = []
        cur = ""
        for c in line:
            if c.isnumeric():
                sum += 10*int(c)
                break
            else:
                cur += c

            if get_num(cur):
                sum += 10*get_num(cur)
                break
        cur = ""
        for c in reversed(line):
            if c.isnumeric():
                sum += int(c)
                break
            else:
                cur = c + cur
            if get_num(cur):
                sum += get_num(cur)
                break
    print(sum)