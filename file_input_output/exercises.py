import pathlib

filepath = pathlib.Path.home() / "my_folder/my_file.txt"
check_file = filepath.exists()

print(check_file)
print(filepath.name)
print(filepath.parent.name)