# Animate zig zag patterns with characters
# hit ctrl + c in terminal to quit

import time
import sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='') 
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent + 1
            if indent == 10:
                indentIncreasing = False

        else:
            indent = indent- 1
            if indent == 0:
                indentIncreasing = True


except KeyboardInterrupt:
    sys.exit()
