import math

class ScientificCalculator:

    def __init__(self):
        self.display = ""
        self.operator = ""

    def enter_number(self, number):
        self.display += number

    def clear(self):
        self.display = ""
        self.operator = ""

    def get_result(self):
        if self.operator == "+":
            return float(self.display.split("+")[0]) + float(self.display.split("+")[1])
        elif self.operator == "-":
            return float(self.display.split("-")[0]) - float(self.display.split("-")[1])
        elif self.operator == "*":
            return float(self.display.split("*")[0]) * float(self.display.split("*")[1])
        elif self.operator == "/":
            return float(self.display.split("/")[0]) / float(self.display.split("/")[1])
        elif self.operator == "^":
            return math.pow(float(self.display.split("^")[0]), float(self.display.split("^")[1]))
        elif self.operator == "sin":
            return math.sin(float(self.display))
        elif self.operator == "cos":
            return math.cos(float(self.display))
        elif self.operator == "tan":
            return math.tan(float(self.display))
        elif self.operator == "log":
            return math.log(float(self.display))
        elif self.operator == "sqrt":
            return math.sqrt(float(self.display))

    def add(self):
        self.operator = "+"

    def subtract(self):
        self.operator = "-"

    def multiply(self):
        self.operator = "*"

    def divide(self):
        self.operator = "/"

    def power(self):
        self.operator = "^"

    def sine(self):
        self.operator = "sin"

    def cosine(self):
        self.operator = "cos"

    def tangent(self):
        self.operator = "tan"

    def logarithm(self):
        self.operator = "log"

    def square_root(self):
        self.operator = "sqrt"

    def calculate(self):
        result = self.get_result()
        self.display = str(result)

def main():
    calculator = ScientificCalculator()

    while True:
        print(calculator.display)
        command = input("Enter command: ")

        if command == "clear":
            calculator.clear()
        elif command in ["+", "-", "*", "/", "^", "sin", "cos", "tan", "log", "sqrt"]:
            calculator.operator = command
        elif command.isdigit():
            calculator.enter_number(command)
        elif command == "=":
            calculator.calculate()

main()
