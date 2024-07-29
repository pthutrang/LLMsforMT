import random


def random30():
    with open("source100.txt") as f:
        lines = random.sample(f.readlines(), 30)
        for l in lines:
            with open("source30.txt", "a") as f2:
                f2.write(l)


random30()
