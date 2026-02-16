print("Welcome to the tip calculator :")
total_bill = float(input("enter your total bill :"))
total_person = int(input("enter total number of people :"))
total_tip = float(input("what percentage tip you want to give :"))

tip_percentage = total_tip / 100
total_tip_percentage = total_bill * tip_percentage
total_bill_after_tip = total_bill + total_tip_percentage
bill_per_person = total_bill_after_tip / total_person
final_amount = round(bill_per_person, 2)

print(f"total bill per person ${final_amount}")