""" Write a Python program to calculate grades based on percentage using
if-else ladder."""

percentage = int(input("Enter your percentage:"))

if percentage >= 95:
    print("Grade A+")

elif percentage >= 90:
    print("Grade A")

elif percentage >= 80:
    print("Grade B+")

elif percentage >= 70:
    print("Grade B")

elif percentage >= 60:
    print("Grade C+")

elif percentage >= 50:
    print("Grade C")

elif percentage >= 40:
    print("Grade D+")

elif percentage >= 30:
    print("Grade D")

else:
    print("FAIL")

