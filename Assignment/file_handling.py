file = open("student.txt","a")

n = int(input("Enter number of students:"))

for i in range(n):
    print(f"Enter details for {i + 1}")
    student_id = input("Enter id:")
    name = input("Enter name:")
    city = input("Enter city:")

    file.write(f"ID:{student_id}\n")
    file.write(f"Name:{name}\n")
    file.write(f"City:{city}\n")
    print("--------------------")