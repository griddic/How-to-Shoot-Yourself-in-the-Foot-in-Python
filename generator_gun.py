if __name__ == '__main__':
    with open('bullet.txt') as inn:
        lines = (line.lower() for line in inn)

    for line in lines:
        print(line.split())
