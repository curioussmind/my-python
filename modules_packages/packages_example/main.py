#import mypackage as mp
from mypackage.module1 import greet
from mypackage.mysubpackage.module3 import people
#from mypackage import module1
#from mypackage import module2
for person in people:
    greet(person)

#mp.module1.greet("Pythonista")
#mp.module2.depart("Pythonista")
