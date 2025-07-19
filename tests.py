from functions.get_files_info import get_files_info

# funcction to test the functionality of get_files_info
def test():
    # test with working directory "calculator" and target directory "."
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    # test with working directory "calculator" and target directory "pkg"
    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("")

    # test with working directory "calculator" and target directory "/bin"
    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("")

    # test with working directory "calculator" and target directory "../"
    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)

if __name__ == "__main__":
    test()