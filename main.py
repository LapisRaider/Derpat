from pet import *
from snatchMouse import *

import sys
print(sys.executable)

if __name__ == "__main__":
    mainPet = pet()

    while True:
        snatchMouseUpdate(mainPet)
        mainPet.updateRender()

        
    