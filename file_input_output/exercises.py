import pathlib

filepath = pathlib.Path.home() / "my_folder/my_file.txt"
check_file = filepath.exists()
print(filepath)
print(check_file)