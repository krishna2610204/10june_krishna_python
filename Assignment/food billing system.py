from datetime import date

bill=open("Food Billing.txt","w")

print("Food Billing System")
print("-------------------")

name = input("Enter name of the customer:")
Mobile = int(input("Enter mobile no:"))
Date = date.today()

print("----------------------")

Food_item = input("Enter your Food item name:")
Price = int(input("Prices:"))
Qty = int(input("Enter qty:"))

print("--------------------")

Total = Price * Qty
Gst = Total * 0.18
print("-----------------")
Grand_total = Total + Gst

bill.write("Food billing System\n")
bill.write(f"Name:{name}\n")
bill.write(f"Mobile no:{Mobile}\n")
bill.write(f"Date:{Date}\n")
bill.write("\n------------------\n")

bill.write(f"Food Item:{Food_item}\n")
bill.write(f"Price:{Price}\n")
bill.write(f"Qty:{Qty}\n")
bill.write("\n-----------------\n")

bill.write(f"Total Bill:{Total}\n")
bill.write(f"Gst:{Gst}\n")
bill.write("\n-----------------\n")

bill.write(f"Grand Total:{Grand_total}\n")
