def IsPrim(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



count = 0       
current = 2    
purpose = int(input("What is the prime number at rank: "))

while True:
    if IsPrim(current):
        count += 1
        if count == purpose:
            print(f"The prime number is {current}")
            break
    current += 1
