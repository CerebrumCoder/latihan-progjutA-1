class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo by zero.")
        return a % b
    
    def power(self, a, b):
        return a ** b

if __name__ == "__main__":
    calc = Calculator()
    print("Addition: 5 + 3 =", calc.add(5, 3))
    print("Subtraction: 5 - 3 =", calc.subtract(5, 3))
    print("Multiplication: 5 * 3 =", calc.multiply(5, 3))
    print("Division: 5 / 2 =", calc.divide(5, 2))
    print("Modulo: 5 % 3 =", calc.modulo(5, 3))