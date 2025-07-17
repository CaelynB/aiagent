import sys
from pkg.calculator import Calculator
from pkg.render import render

def main():
    # create an instance of the Calculator class
    calculator = Calculator()

    # if no expression is provided, print usage instructions and return
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    # join the command line arguments (excluding the script name) to form the expression
    expression = " ".join(sys.argv[1:])

    # attempt to evaluate the expression and render the result
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
