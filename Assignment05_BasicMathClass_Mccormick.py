class BasicMathOperations:
    def greet_user(self, first_name, last_name):
        return f"Hello, {first_name} {last_name}!"

    def add_numbers(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1 + num2

    def perform_operation(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            return "Invalid operator"

    def square_number(self, number):
        return number ** 2

    def factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number-1)

    def counting(self, start, end):
        for i in range(start, end+1):
            print(i)

    def calculateSquare(self, number):
        return number ** 2

    def calculateHypotenuse(self, side1, side2):
        return (self.calculateSquare(side1) + self.calculateSquare(side2)) ** 0.5

    def area_of_rectangle(self, width, height):
        return width * height

    def power_of_number(self, base, exponent):
        return base ** exponent

    def type_of_argument(self, arg):
        return type(arg).__name__
