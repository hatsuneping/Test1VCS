import sys
import os
cwd = os.getcwd() 

sys.path.append(cwd)
#print(sys.path)

from generate_list import printIt
for i in range (0,1001):
    printIt()

