import time , sys

indent = 0 #this is for how many indentation you have to give
indent_increase = True #for confirming whether the indentation is increasing or not

try :
    while True: #the main program loop
        print(' ' * indent,end = '')
        print("*******")
        time.sleep(0.1) #for pause of 1/10th of a second

        if indent_increase:
            # for increasing indent
            indent += 1
            if indent == 20:
                #change the direction for indentation
                indent_increase = False
        else:
            #now decreasing the spaces to form the zig zag
            indent -= 1
            if indent == 0:
                #now change direction for snake
                indent_increase = True
except KeyboardInterrupt:
    sys.exit()