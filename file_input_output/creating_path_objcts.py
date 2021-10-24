from os import pathconf
import pathlib

# CREATING PATH OBJECT FROM A STRING
path = pathlib.Path("Documents/Diabetes.pdf")

# WE CAN ALSO USE A CLASS METHOD THAT RETURN PATH OBJ OF SPECIEAL DIR
# TWO OF THEM ARE Path.home() and Path.cwd()
path = 'C:\Users<username' # windows
path = '/Users/<username>' # macOS
path = '/home/<username' # Ubuntu linux

# ABSOLUTE VS RELATIVE PATH
windows = pathlib.Path(r"Photos/image.jpg") #relative
macOs = pathlib.Path("Photos/image.jpg") # relatif



