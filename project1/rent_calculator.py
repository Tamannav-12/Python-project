food=int(input("Enter total food amount="))
rent=int(input("Enter rent amount="))
electricity_bill_unit=int(input("Enter total units="))
as_per_unit=int(input("Enter per unit amount= "))
persons=int(input("Enter total no. of persons="))

#firstly calculate bill
total_bill= electricity_bill_unit * as_per_unit

total_amount= (food+rent+total_bill) / persons

print("Each person pay rupees=",total_amount)