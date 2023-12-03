def list_to_tuple(l):
    return (int(l[0]), l[1])

def process_lines(lines):
    no_game = [l.split(':')[1].strip() for l in lines]
    return [[[list_to_tuple(datapoint.strip().split(' ')) for datapoint in draw.strip().split(',')] for draw in l.split(';')] for l in no_game]

def valid_game(game):
    for draw in game:
        for count, color in draw:
            if color == 'red' and count > 12:
                return False
            elif color == 'green' and count > 13:
                return False
            elif color == 'blue' and count > 14:
                return False
    return True
 
with open("./day2/input.txt") as f:
    data = process_lines(f.readlines())
    acc = 0
    for idx, game in enumerate(data):
        if valid_game(game):
            acc += (idx + 1)
    print(acc)


