
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import json
from menu import menu_principal


print("")



if __name__ == '__main__':
    menu_principal()
