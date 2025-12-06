def box_print(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('lode padna nhi aata kya')
    if width <= 2:
        raise Exception('lode padna nhi aata kya')
    if   height <= 2:
        raise Exception('lode padna nhi aata kya')
    
    print(symbol*width)
    for i in range (height-2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


sym = str(input("enter your single character  symbol ---->"))
wid = int(input("enter the width of the box(must be greater than 2) ---->"))
hei = int(input("enter the  height of the box(must be greater than 2) ---->"))
try:
     box_print(sym, wid, hei)
except Exception as err:
    print('An exception happend: ' + str(err))


# try:
#     box_print('*', 4, 4)
#     box_print('O', 20, 5)
#     box_print('x', 10, 30)
#     box_print('ZZ', 3, 3)
# except Exception as err:
#     print('An exception happend: ' + str(err))