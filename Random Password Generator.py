# RANDOM PASSWORD GENERATOR

import random

#gather our charactcers
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "1234567890"
symbols = "!@#$%^&*()."
all = lower + upper + numbers + symbols

#set password length
length = 15

#loop through each character
password = ""
for _ in range(length):
    password = "".join([password, random.choice(all)])

print(password)