import random

Pass = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890abcdefghijklmnopqrstuvwxyz@#₹_&-+()/*\"':;!?$¢©%[]"

Len = int(input("ENTER LENGTH OF PASSWORD: "))

a = "".join(random.sample(Pass, Len))
print(f"Your password is: {a}")
