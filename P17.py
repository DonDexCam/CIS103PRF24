import random

def generate_powerball():
    numbers = set()
    while len(numbers) < 5:
        num = random.randint(1, 69) 
        numbers.add(num)
    return sorted(numbers)

def generate_mega_million():
    numbers = set()
    while len(numbers) < 5:
        num = random.randint(1, 70)
        numbers.add(num)
    return sorted(numbers)

def generate_lucky_day_lotto():
    numbers = set()
    while len(numbers) < 5:
        num = random.randint(1, 45)
        numbers.add(num)
    return sorted(numbers)

def generate_lotto():
    numbers = set()
    while len(numbers) < 6:
        num = random.randint(1, 52) 
        numbers.add(num)
    return sorted(numbers)

def display_menu():
    print("\n--- Illinois Lottery Number Generator ---")
    print("1. Powerball")
    print("2. Mega Million")
    print("3. Lucky Day Lotto")
    print("4. Lotto")
    print("9. Quit")

def main():
    while True:
        display_menu()
        choice = input("Please select a game (1-4) or 9 to quit: ")
        
        if choice == '1':
            numbers = generate_powerball()
            print(f"Powerball numbers: {', '.join(map(str, numbers))}")
        elif choice == '2':
            numbers = generate_mega_million()
            print(f"Mega Million numbers: {', '.join(map(str, numbers))}")
        elif choice == '3':
            numbers = generate_lucky_day_lotto()
            print(f"Lucky Day Lotto numbers: {', '.join(map(str, numbers))}")
        elif choice == '4':
            numbers = generate_lotto()
            print(f"Lotto numbers: {', '.join(map(str, numbers))}")
        elif choice == '9':
            print("Thank you for using the Lottery Number Generator. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

        input("Hit enter key to return to menu...")

if __name__ == "__main__":
    main()
