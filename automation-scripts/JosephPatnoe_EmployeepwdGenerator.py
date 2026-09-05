# Joseph Patnoe
# CIS188

"""
A program that creates a new CSV file named employees_pwd.csv which contains the first 
name, last name, email and a new randomly generated password for each employee.
"""

import random
import string


# Length of the generated password
pass_length = 16

# Number of passwords to generate
NUM_PASS = 10


# Generate a password of size length using all ascii letters, numbers 0-9 and a subset of special characters
def gen_pass(length):
    all = string.ascii_letters + string.digits + '!@#$%^&*()-_+=~[]{}<>?/\|'
    password = "".join(random.sample(all, length))
    return password


# Open employees.csv and write to new file
infile = open("employees.csv", "r")
infile.readline()
outfile = open("employees_pwd.csv", "w")
outfile.write("fname,lname,email,password\n")

# Loop through each line
for line in infile:

    # Remove empty spaces
    line = line.strip()
    if line == "":
        continue
    values = line.split(",")

    # Get first name, last name and email
    fname = values[0]
    lname = values[1]
    email = values[3]
    
    # Generate random password
    pwd = gen_pass(pass_length)

    # Write to employees_pwd
    outfile.write(f"{fname},{lname},{email},{pwd}\n")

# Close file
infile.close()
outfile.close()

print("Please check employees_pwd.csv for employee passwords")
