def find_robot_moves(moves):
    x = 0
    y = 0

    for move in moves:
        if move == "R":
            x += 1
        elif move == "L":
            x -= 1
        elif move == "U":
            y += 1
        elif move == "D":
            y -= 1

    return x == 0 and y == 0


if __name__ == '__main__':
    print(find_robot_moves("UD"))