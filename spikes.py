import time , sys

try:
    while True:
        # drawing line with increasing length
        for i in range (0,10):
            print('$'*(i*i))
            time.sleep(0.1)

        #ow drawing lines with decreasing length
        for j in range (8,1,-1):
            print("$"*(j*j))
            time.sleep(0.1)
except KeyboardInterrupt:
    SystemExit