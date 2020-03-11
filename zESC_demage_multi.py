import re
import os

def write(fname, line):
    with open("mulit " + fname, "a") as file:
        file.write(line)

files = os.listdir()
print(files)

for filename in files:
    with open(filename, "r+") as sr_var:
        for line in sr_var:
            new_nums = []
            if "damage = { min" in line:
                nums = re.findall("\d+", line)
                for num in nums:
                    new_nums.append(int(num)*2)
                new_line = "         damage = { min = " + str(new_nums[0]) +  " max = " + str(new_nums[1]) + " }\n"
                write(filename, new_line)
            else: 
                write(filename, line)

    
