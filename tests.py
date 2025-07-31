from functions.run_python import run_python_file

# function to test the functionality of run_python_file
def test():
    # test 1: run a Python file in the current directory (should print usage instructions)
    result = run_python_file("calculator", "main.py")
    print("Result for running Python file in current directory:")
    print(result)
    print("-" * 83)

    # test 2: run a Python file with arguments (should evaluate the expression and render the formatted output)
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for running Python file with arguments:")
    print(result)
    print("-" * 83)

    # test 3: run a unittest file (should display unittest output)
    result = run_python_file("calculator", "tests.py")
    print("Result for running unittest file:")
    print(result)
    print("-" * 83)

    # test 4: attempt to run a Python file outside the permitted working directory (should fail)
    result = run_python_file("calculator", "../main.py")
    print("Result for running Python file outside the permitted working directory:")
    print(result)
    print("-" * 83)

    # test 5: attempt to run a Python file that does not exist (should fail)
    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running nonexistent Python file:")
    print(result)
    print("-" * 83)

if __name__ == "__main__":
    test()
