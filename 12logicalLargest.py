
num1 = int(input("Enter fast num"))
num2 = int(input("Enter second num"))
num3 = int(input("Enter Third num"))

if(num1>num2) & (num1>num3 ):
    print("largest num of ",num1)

elif(num2>num1) & (num2>num3):
    print("largest num of ",num2)

elif(num3>num1) & (num3>num2):
    print("largest num of ",num3)

else: print("wrong answer")


