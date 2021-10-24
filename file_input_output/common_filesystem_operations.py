# GOALS
    # create dir and files
    # search for files within dir
    # move and delete files and folders

# CREATING DIRS AND FILES
from pathlib import Path
new_dir = Path.home() / "new_dir"
new_dir.mkdir()
print(new_dir.exists()) # checking whether the dir is exist or not

# we can do this if we want to create new dir and want to avoid the fileexisterror
new_dir.mkdir(exist_ok=True) # when we run this, it creates the folder it it doesn't exist or nothing happened if it is exist

# to create any parent dirs needed in order to create the target dir, we can set the opt parents parameter of mkdir() to True
nested_dir = new_dir / "folder_a" / "folder_b" # create folder b inside folder a insied new_dir
nested_dir.mkdir(parents=True) # since folder a is not exist yet, we set parent to True so that it'll automatically create folder a
nested_dir.mkdir(parents=True, exist_ok=True) # by putting all if these together, no error will be raised


# WHAT IS THE PATH WILL BE INPUT BY THE USER?

file_path = new_dir / 'file1.txt' # file doesn't exist yet, so we can use the Path.touch() method
file_path.touch()

