from functions.get_files_info import get_files_info

# function to test the functionality of get_files_info
def test():
    # test 1: list files in the current directory (should succeed)
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("-" * 74)

    # test 2: list files in a subdirectory (should succeed)
    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("-" * 74)

    # test 3: attempt to list files in a directory outside the permitted working directory (should fail)
    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("-" * 74)

    # test 4: attempt to list files in the parent directory (should fail)
    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print("-" * 74)

if __name__ == "__main__":
    test()
