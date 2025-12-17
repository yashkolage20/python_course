def factorial(num):
    if num == 1:
        return 1
    else:
        while num > 1:
            result = num * factorial(num - 1)
            return result
        
a = int(input("Enter a number: "))
b = factorial(a)
print(f"Factorial of {a} is {b}")