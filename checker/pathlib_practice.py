from pathlib import Path

# Exercise A - Find where python is 

current_path = Path.cwd()
print(f"This is your current path: {current_path}")

# Exercise B - Find your home

home_path = Path.home()
print(f"This is your home path: {home_path}")

# Exercise C - Find Desktop 

desktop_path = Path.home() / "Desktop"
print(f"This is your desktop path: {desktop_path}")

# Exercise D - Does desktop exist?

if desktop_path.exists():
    print(f"{desktop_path} exists.")
else:
    print(f"{desktop_path} does not exists.")

# Exercise E - is_dir()
if home_path.exists():
    print(f"Your home path exists: {home_path}")
    if home_path.is_dir():
        print("True")
    else:
        print("False")
else:
    print(f"Home path doesnt exists: {home_path}")

# Exercise F - Look inside home directory
p = Path.home()
for subdir in p.iterdir():
    if subdir.is_dir():
        print(subdir)

# # print(f"Your current Path is - {Path.cwd()}")