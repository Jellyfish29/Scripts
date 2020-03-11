from random import randint, choice

ip = ""
for j in range(8):
    ip += "".join([chr(choice([randint(48, 57), randint(97, 102)])) for i in range(4)])

    if j == 7:
        ip += f"/{randint(0, 128)}"
    else:
        ip += ":"

print(ip)
