import re
import os

f = open("multiplied_file.txt", "w")
f.close()

def multiply_values(file_name, value):
    with open(file_name, "r+") as sr_var:
        for line in sr_var:
            number = re.findall("\d+.\d+", line) #extract float from line
            if len(number) < 1:
                number = re.findall("\d+", line) # extract int from line
            try:
                new_number = float(number[0]) * value # extracted number is multiplied by value
                new_line = line[0:line.find("=") + 2] # splicing of the line from index 0 until "=" + 2 Spaces
                new_line += str(new_number) # new line + new number
                write(new_line, True) #new_line gets written to the file
            except IndexError:
                write(line, False)
            

def write(new_line, nl):
    with open("multiplied_file.txt", "a") as sr_var:
        if nl:
            sr_var.write(new_line + "\n")
        else:
            sr_var.write(new_line)


file_name = input("File Name = ")
mult_value = int(input("Multiply by = "))
multiply_values(file_name, mult_value)
print("File saved at " + os.getcwd() + "\multiplied_file.txt")
        
