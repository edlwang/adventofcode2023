def list_to_tuple(l):
    return (int(l[0]), l[1])

def process_lines(lines):
    no_game = [l.split(':')[1].strip() for l in lines]
    return [[[list_to_tuple(datapoint.strip().split(' ')) for datapoint in draw.strip().split(',')] for draw in l.split(';')] for l in no_game]

 
with open("./day2/input.txt") as f:
    data = process_lines(f.readlines())
    acc = 0
    for idx, game in enumerate(data):
        min_r = 0
        min_g = 0
        min_b = 0
        for draw in game:
            for count, color in draw:
                if color == 'red':
                    min_r = max(min_r, count)
                elif color == 'green':
                    min_g = max(min_g, count)
                elif color == 'blue':
                    min_b = max(min_b, count)
        acc += min_r * min_g * min_b
    print(acc)
        


