# Day 2 Codes

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
split_no = int(input("How many people to split the bill?"))
tip = int(input("What percentage of bill would you like to give? 10, 12, or 15"))
# To calculate the percentage divide the original amount by the percentage divide
# by 100
bill_with_tip = total_bill + (total_bill*tip/100)
individual_share = (bill_with_tip)/split_no
print(f"Each person should pay: {individual_share}")

