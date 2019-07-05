

mark = int(input("enter your num"));

if (mark >= 80) & (mark<=100):
    print("Result of : A+  =",mark)

elif (mark >= 70) & (mark<=79):
    print("Result of : A  =",mark)

elif (mark >= 60) & (mark<=69):
    print("Result of : A - =", mark)

elif (mark >=50) & (mark<=59):
    print("Result of : B = ", mark)

elif (mark >=40) & (mark<=49):
    print("Result of : C ", mark)

elif (mark >= 33) & (mark<=39):
    print("Result of : D = ", mark)

else:
    print("Fail = ", mark)
