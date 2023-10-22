print ("Welcome to the bill contributor interface\n")
Total_bill = int(input("What was the total bill?\n"))
No_of_people_bill_split = int(input("How many people to split a bill\n"))
bill= Total_bill/ No_of_people_bill_split
# print(bill)

print(f"Each person should pay= INR {bill}")
