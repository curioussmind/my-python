# everything in a dir is either a file or a subdir. the path.iterdir() method returns
# over Path objects representing each item in the dir

from pathlib import Path

my_dir = Path.home() / "new_dir" # assign new_dir folder to my_dir var
print(my_dir.exists()) 

# iterating over dir contents
for path in my_dir.iterdir():
    print(path)



