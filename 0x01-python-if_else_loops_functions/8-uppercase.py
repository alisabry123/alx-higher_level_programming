#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for i in str:
        char = ord(i)
        if ord(i) > 96 and ord(i) < 123:
            char = ord(i) - 32
        str1 += chr(char)
    print(str1)
