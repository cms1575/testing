import random

random_numbers = []
for _ in range(200):
    number = random.randint(1, 100)
    random_numbers.append(number)

random_numbers.sort()

for index in range(0, 200, 10):
    line = random_numbers[index:index + 10]
    for num in line:
        print(f"{num:2}", end=" ")
    print()

print("------------------------------------")

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for number in random_numbers:
    if 1 <= number <= 20:
        count1 += 1
    elif 21 <= number <= 40:
        count2 += 1
    elif 41 <= number <= 60:
        count3 += 1
    elif 61 <= number <= 80:
        count4 += 1
    elif 81 <= number <= 100:
        count5 += 1

print(" 1 -  20:", "*" * count1, count1)
print("21 -  40:", "*" * count2, count2)
print("41 -  60:", "*" * count3, count3)
print("61 -  80:", "*" * count4, count4)
print("81 - 100:", "*" * count5, count5)
