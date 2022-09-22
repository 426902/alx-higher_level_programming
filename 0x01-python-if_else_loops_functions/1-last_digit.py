#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#digit = abs(number) % 10
if number < 0:
    last = ((number * -1) % 10) * -1
   #digit = -digit
#print("Last digit of {} is {} and is ".format(number, digit), end="")
else:
    last = number % 10
if digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
   #print("greater than 5")
elif last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
    #print("0")
elif last < 6 and last != 0:
    print("Last digit of {} is {} and is less\
            than 6 and not 0".format(number, last))
#else:
 #   print("less than 6 and not 0")
