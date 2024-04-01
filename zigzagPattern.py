# zigzag program

import time, sys
indent = 0  # how many spaces to indent

indentIncrease = True   # whether the indentation is increasing or not

try:
    while True:     # main loop of the program
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)     # pause for 1/10 of a second
        if indentIncrease:    # increase number of spaces
            indent = indent + 1
            if indent == 20:    # change direction
                indentIncrease = False
        else:   # decrease the number of spaces
            indent = indent - 1
            if indent == 0:     # change direction
                indentIncrease = True

except KeyboardInterrupt:
    sys.exit()
