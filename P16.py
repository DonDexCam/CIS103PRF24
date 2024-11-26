#Donavan Bryant recursion problem
def recursive_sum(n):
    
    if n == 0:
        return 0
   
    else:
        return n + recursive_sum(n - 1)

def get_input():
    while True:
        try:
            
            user_input = input("Enter a positive integer: ")
            
            if user_input.strip() == "":
                raise ValueError("Input cannot be blank.")
                
           
            number = int(user_input)
            
            if number < 0:
                raise ValueError("Input cannot be negative.")
            
            return number
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    number = get_input()
    result = recursive_sum(number)
    
    addition = '+'.join(str(i) for i in range(number, 0, -1))
    
    print(f"The sum of numbers from {number} to 1 is: {result} ({addition})")

if __name__ == "__main__":
    main()
