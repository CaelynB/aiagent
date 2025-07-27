from functions.get_file_content import get_file_content

# function to test the functionality of get_file_content
def test():
    # test 1: read a file in the current directory (should succeed)
    result = get_file_content("calculator", "main.py")
    print("Result for file in current directory:")
    print(result)
    print("-" * 97)

    # test 2: read a file in a subdirectory (should succeed)
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for file in 'pkg' directory:")
    print(result)
    print("-" * 97)

    # test 3: attempt to read a file outside the permitted working directory (should fail)
    result = get_file_content("calculator", "/bin/cat")
    print("Result for file in '/bin' directory:")
    print(result)
    print("-" * 97)

    # test 4: attempt to read a file that does not exist (should fail)
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for non-existent file in 'pkg' directory:")
    print(result)
    print("-" * 97)

if __name__ == "__main__":
    test()
