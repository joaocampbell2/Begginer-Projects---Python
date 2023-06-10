
max = int(input("Set the maximum number of digits in the binary number: "))

flag = False
while flag == False:
    flag = True
    bin = input("Enter the binary: ")
    size = len(bin)
    for i in bin:
        if i != '0' and i !='1':
            print("The binary number has a digit different than 0 or 1, try again!")
            flag = False
            break
    
    if size > max:
        print("Binary digits bigger than expected, try again!")
        flag = False
    
dec = 0
for i in bin:
    
    if size ==  1:
        dec += int(i) * 1
        break

    multiplier = 1
    for pow in range (1,size):
        multiplier *= 2
    
    
    dec += int(i) * multiplier
    size -= 1


print(dec)