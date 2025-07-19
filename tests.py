
from functions.get_file_content import get_file_content

def test():
    print("main.py TEST:")
    print(get_file_content("calculator", "main.py"))

    print("\npkg/calculator.py TEST\n")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\n/bin/cat TEST\n")
    print(get_file_content("calculator", "/bin/cat"))

    print("\npkg/does_not_exist,py TEST\n")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

    print(get_file_content("calculator", "lorem.txt"))
if __name__ == "__main__":
    test()