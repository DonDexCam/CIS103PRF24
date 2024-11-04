def recursive_sum(n):
    
    if n == 0:
        return 0
    
    else:
        return n + recursive_sum(n - 1)

number = 5
result = recursive_sum(number)
print(f"The sum of numbers from {number} to 1 is: {result}")
