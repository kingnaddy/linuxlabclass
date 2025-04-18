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

n = len(message)

blocks = []
for i in range(0,n,5):
    blocks.append(message[i:i+5])

for i in range(0,len(blocks),10):
    print(' '.join(blocks[i:i+10]), end='\n')
