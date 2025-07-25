import sys
from pkg.calculator import Calculator
from pkg.render import render

def main():
    # create a new instance of the Calculator
    calculator = Calculator()

    # if no command line arguments are provided, print usage instructions and return
    if len(sys.argv) <= 1:
        print("Usage: python main.py <expression>")
        return

    # join the command line arguments after the script name to form the expression
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
