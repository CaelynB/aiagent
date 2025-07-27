from functions.write_file import write_file

# function to test the functionality of write_file
def test():
    # test 1: write to a file in the current directory (should succeed and overwrite the file if it exists)
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for writing to file in current directory:")
    print(result)
    print("-" * 87)

    # test 2: write to a new file in an existing subdirectory (should succeed)
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for writing to file in 'pkg' directory:")
    print(result)
    print("-" * 87)

    # test 3: attempt to write to a file outside the permitted working directory (should fail)
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for writing to file in '/tmp' directory:")
    print(result)
    print("-" * 87)

if __name__ == "__main__":
    test()
