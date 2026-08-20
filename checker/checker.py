from pathlib import Path

# Create a function in your checker package that:
# Receives a Path.
# Determines whether it exists.
# Determines whether it is a file.
# Determines whether it is a directory.
# Returns those three facts in a dictionary.
# Does not print anything.

def checker(user_path):
    result = {
        "exists": user_path.exists(),
        "is_file": user_path.is_file(),
        "is_directory": user_path.is_dir(),
    }
    return result
    
# some_path = Path(input("Enter a path:\n").strip())

job_board = Path('C:/Users/guill/job_board')
manage_py = Path("C:/Users/guill/job_board/manage.py")
nonexistent = Path.home() / "Desktop"

# print(checker(some_path))
print(checker(job_board))
print(checker(manage_py))
print(checker(nonexistent))