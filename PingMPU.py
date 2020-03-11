import subprocess

i = 0
target = input("Ziel: ")
start_value = int(input("Startwert in Byte: "))
precession = int(input("Präzision: "))

output = subprocess.run(["ping", "-f", "-l", str(start_value), "-n", "1", target], capture_output=True)
if b"fragmentiert" in output.stdout.split():
    print("")
    print("Startwert zu Groß")
else:
    while b"fragmentiert" not in output.stdout.split():
        i += precession
        print(f"{start_value + i} Byte")
        output = subprocess.run(["ping", "-f", "-l", str(start_value + i), "-n", "1", target], capture_output=True)

    print("")

    print(f"MPU= {start_value + i - precession}")
