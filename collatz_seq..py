def collatz(n):
    if n%2 == 0:
        return n//2 
    else :
        return n*3+1


print("enter yoyr number for collatz sequence")
num1 = int(input('>'))
while True:
    num1 = collatz(num1)
    print(num1)
    if num1 == 1:
        break

    
