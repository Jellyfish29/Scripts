from random import choice
from time import sleep

dic = {
    "1": "128",
    "2": "64",
    "3": "32",
    "4": "16",
    "5": "8",
    "6": "4",
    "7": "2",
    "8": "1"
}


def get_num():
    return choice([key for key in dic])


def check(h, b):
    if b == "q":
        exit()
    if b == dic[h]:
        print("Richtig")
        sleep(0.5)
    else:
        print(f"Falsch --> {dic[h]}")


print("StepTrainer")

while True:
    h = get_num()
    print(h)
    check(h, input(">"))
