import sys

shift = int(sys.argv[1])

text = sys.stdin.read()

message = ""

text = text.upper()
for char in text:

    if char.isalpha():
        shifted = ord(char) + shift
        if shifted > ord("Z"):
            shifted -= 26
        new_char = chr(shifted)
        message+= new_char

