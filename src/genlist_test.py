import sys
import os
cwd = os.getcwd() 

sys.path.append(cwd)
#print(sys.path)

from generate_list import printIt
printIt()

