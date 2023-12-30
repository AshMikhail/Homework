
def hello():
    print("Добро пожаловать в игру Крестики Нолики")
    print("  Ввод осуществляется по координатам")
    print("")
def array():
    print("    | 0 | 1 | 2 |")
    for i, row in enumerate(motion):
        i = f"  {i} | {' | '.join(row)} | "
        print(i)
def step():
    while True:
        a = input("Введите 2 координаты: ").split()

        if len(a) != 2:
            print("Введенно не 2 координаты")
            continue

        x, y = a

        if not(x.isdigit()) or not(y.isdigit()):
            print("Надо вводить цифры")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Введите координаты от 0 до 2")
            continue

        if motion[x][y] != " ":
            print("Клетка занята! ")
            continue

        return x, y

def win_check():
    win_comb = [((0, 2), (1, 1), (2, 0)),((0, 0), (1, 1), (2, 2)),((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]

    for c in win_comb:
        a = c[0]
        b = c[1]
        c = c[2]

        if motion[a[0]][a[1]] == motion[b[0]][b[1]] == motion[c[0]][c[1]] != " ":
            print(f"Выиграл {motion[a[0]][a[1]]}!")
            return True
    return False

motion = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]
        ]

hello()
num = 0
while True:
    num += 1
    array()
    if num % 2 == 1:
        print(" Ходит Игрок Х ")
    else:
        print(" Ходит Игрок 0 ")

    x, y = step()
    if num % 2 == 1:
        motion[x][y] = "X"
    else:
        motion[x][y] = "0"

    if win_check():
        break

    if num == 9:
        print(" Ничья ")
        break
