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
ignored = {
    ".git",
    ".venv",
    ".vscode",
    "node_modules",
    "uploads",
    "cache",
    "static",
    "staticfiles",
    "media",
}

def django_validator(project_path):

    manage_path = project_path / "manage.py"
    settings_path = project_path / "settings.py"
    urls_path = project_path / "urls.py"
    
    evidence = {}
    
    for entry in project_path.iterdir():
        if entry.is_dir() and entry.name not in ignored:
            evidence[entry] = {
                'settings_py': path_inspector(entry / "settings.py"),
                'views_py': path_inspector(entry / "views.py"),
                'urls_py': path_inspector(entry / "urls.py"),
                'models_py': path_inspector(entry / "models.py"),
            }
    return evidence

print(django_validator(Path("C:/Users/guill/job_board")))