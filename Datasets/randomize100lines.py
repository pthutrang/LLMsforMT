import random


def random100():
    with open("generaltest2023.en-cs.src.en.txt") as f:
        lines = random.sample(f.readlines(), 100)
        for l in lines:
            with open("randomoutput.txt", "a") as f2:
                f2.write(l)


random100()
