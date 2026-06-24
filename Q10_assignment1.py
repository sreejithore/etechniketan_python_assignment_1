name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course = input("Enter Course Name: ")
mark1 = float(input("Enter Marks in Subject 1: "))
mark2 = float(input("Enter Marks in Subject 2: "))
mark3 = float(input("Enter Marks in Subject 3: "))
total = mark1 + mark2 + mark3
percent=(total/300)*100
print("Percentage of the student is ", percent)
