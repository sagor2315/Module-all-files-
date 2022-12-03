#write a program to calculate electricity bill (accept number of unit from user) according to following criteria. For first 100 units- no charge, next 100 units 5/- per unit, after 200 units- 10/- per unit. example if input is 350 unit then total bill 2000/-

# total_units = float(input("Enter Your Total Unites: "))
# if total_units > 200:
#     total_bill = (total_units - 200)
#     payable_bill = (100 * 5 + total_bill * 10)
#     print("Amount To Pay", payable_bill, "Taka")
# elif total_units > 100:
#     total_bill = (total_units - 100)
#     payable_bill = (total_bill * 5)
#     print("Amount To Pay", payable_bill, "Taka")
# else:
#     print("No Charge")

amount = 0
total = float(input("Enter The Total Units: "))
if total <= 100:
    amount = 0
elif total > 100 or total <= 200:
    amount = (total - 100) * 5
    vat = amount + amount * 20 / 100
    miter_rent = 50
    total_bill = amount + vat + miter_rent
else:
    amount = 100 * 5 + (total - 200) * 10
    vat = amount + amount * 20 / 100
    miter_rent = 50
    total_bill = amount + vat + miter_rent
print("The Total Bill is", total_bill, "Taka")