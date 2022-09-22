#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{:s}".format(char), end="")
    print('')
   # alp = list(str)
    #for i in range(len(alp)):
     #   if (ord(alp[i]) > 96 and ord(alp[i]) < 123):
    #        alp[i] = chr(ord(alp[i]) - 32)
     #   print("{}".format("".join(alp)))
