from random import randint, choice

ip = ""
for j in range(4):
    ip += str(randint(0, 255))
    if j == 3:
        ip += f"/{randint(0, 32)}"
    else:
        ip += ":"
ip += f"   Subnetze = {choice([2 ** i for i in range(8)])}"

print(ip)
