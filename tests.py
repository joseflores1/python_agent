
from config import SEPARATOR
from functions.run_python import run_python_file
def test():

    print_separator = lambda func: print(func, f"\n{SEPARATOR}")

    print_separator(run_python_file("calculator", "main.py") )
    print_separator(run_python_file("calculator", "main.py", ["3 + 5"]))
    print_separator(run_python_file("calculator", "tests.py"))
    print_separator(run_python_file("calculator", "../main.py"))
    print_separator(run_python_file("calculator", "nonexistent.py")) 
if __name__ == "__main__":
    test()