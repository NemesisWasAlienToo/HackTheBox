import random
from re import T
import time

numbers = [33, 30, 35, 28, 61]
matches = []

start = 0
end = int(time.time())

while end >= start:
    found = True
    matches = []
    random.seed(end)

    for i in range(0,5):
        r = random.randint(1, 90)
        if r == numbers[i]:
            matches.append(r)
        else:
            found = False
            break

    if found == True:
        break

    end -= 1

print("Match found at : " + str(end))
print(matches)
while True:
    input()
    print(str(random.randint(1, 90)))