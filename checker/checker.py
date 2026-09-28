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

# job_board = Path('C:/Users/guill/job_board')
# manage_py = Path("C:/Users/guill/job_board/manage.py")
# nonexistent = Path.home() / "Desktop"

# print(path_inspector(some_path))
# print(path_inspector(job_board))
# print(path_inspector(manage_py))
# print(path_inspector(nonexistent))

def django_validator(project_path):

    manage_path = project_path / "manage.py"
    settings_path = project_path / "settings.py"
    urls_path = project_path / "urls.py"
    
    for entry in project_path.iterdir():
        if entry.is_dir():
            path_inspector(entry / "settings.py")
            path_inspector(entry / "urls.py")
            path_inspector(entry / "models.py")
            path_inspector(entry / "views.py")
        else:
            print(f"NOT DIR: {entry}")
        
    evidence = {
                "manage_py": path_inspector(manage_path),
                "settings_py": path_inspector(settings_path),
                "urls_py": path_inspector(urls_path),
            } 
    
    return evidence

print(django_validator(Path("C:/Users/guill/job_board")))