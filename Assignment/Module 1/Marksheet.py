Sub1 = int(input("Enter marks of Sub1:"))
Sub2 = int(input("Enter marks of Sub2:"))
Sub3 = int(input("Enter marks of Sub3:"))
Sub4 = int(input("Enter marks of Sub4:"))

Total = Sub1 + Sub2 + Sub3 + Sub4
print("Total",Total)

Percentage = Total/4
print("Percentage:",Percentage)


if Percentage>=70:
    print("DIST")

elif Percentage >= 60:
    print("First Class")

elif Percentage >=50:
    print("Second Class")

elif Percentage >=40:
    print("Pass")

else:
    print("FAIL")