def main():
    operations = BasicMathOperations()
    tasks = {
        1: 'Greet User',
        2: 'Add Numbers',
        3: 'Perform Operation',
        4: 'Square Number',
        5: 'Factorial',
        6: 'Counting',
        7: 'Compute Hypotenuse',
        8: 'Area of Rectangle',
        9: 'Power of Number',
        10: 'Type of Argument'
    }
    while True:
        print("\
Available tasks:")
        for key, value in tasks.items():
            print(f"{key}. {value}")
        try:
            choice = int(input("Select a task by entering its number (or enter 0 to exit): "))
            if choice == 0:
                break
            elif choice in tasks:
                print(f"You selected: {tasks[choice]}")
                # Example of handling one case, others can be implemented similarly
                if choice == 1:
                    first_name = input("Enter your first name: ")
                    last_name = input("Enter your last name: ")
                    print(operations.greet_user(first_name, last_name))
                # Add other cases here
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
