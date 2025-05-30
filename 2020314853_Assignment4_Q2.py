def recur_sum(n):
    if n <= 1:
        return 0
    return (n - 1) + recur_sum(n - 1)

while True:
    user_input = input("Insert a number: ")
    
    if user_input.lower() == "exit":
        print("Exit")
        break
    
    if user_input.isdigit():
        number = int(user_input)
        result = recur_sum(number)
        print(f"The sum of all numbers recurive sum  is: {result}")
    
