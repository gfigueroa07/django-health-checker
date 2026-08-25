from pathlib import Path

# Create a function in your checker package that:
# Receives a Path.
# Determines whether it exists.
# Determines whether it is a file.
# Determines whether it is a directory.
# Returns those three facts in a dictionary.
# Does not print anything.

def path_inspector(user_path):
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

# print(path_inspector(some_path))
print(path_inspector(job_board))
print(path_inspector(manage_py))
print(path_inspector(nonexistent))

def django_validator(project_path):
    evidence = {
            "exists": project_path.exists(),
            "is_file": project_path.is_file(),
            "is_directory": project_path.is_dir(),
        }
    
    manage_path = Path(project_path) / "manage.py"
    settings_path = Path(project_path) / "settings.py"
    urls_path = Path(project_path) / "urls.py"
    print(path_inspector(manage_path))
    print(path_inspector(settings_path))
    print(path_inspector(urls_path))
    
    
project_path = Path(input('path\n'))
print(django_validator(project_path))