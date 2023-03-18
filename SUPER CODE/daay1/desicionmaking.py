num = int(input("Enter a number"))
if num%3==0 and num%5==0:
    print("its multiple of both 3 and 5")
elif num%3==0:
    print("Its devided by 3 ")
elif num%5 ==0:
    print("its multiple by 5")

else:
    print("invalid")