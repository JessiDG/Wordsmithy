import random
print("Hello World")


def sing_a_song():
    print("The hills are alive -- aaaahhh!")


def index():
    str = "*"
    r = random.randrange(0, 5)
    for j in range(5):
        str += "\n"
        r = random.randrange(1, 10)
        for i in range(r):
            str += "*"
    return str


sing_a_song()
print(index())
