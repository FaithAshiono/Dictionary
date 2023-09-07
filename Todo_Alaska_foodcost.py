food_cost = float(input("Enter the cost of food you ordered:"))

tip_percent = 18
tip_amount = (tip_percent/100)*food_cost

tax_percent = 7
tax_amount =(tax_percent/100)* food_cost

Total_cost = food_cost + tip_amount + tax_amount


print(f"Tip amount (18%): ${tip_amount:.2f}")
print(f"Sales tax amount (7%): ${tax_amount:.2f}")
print(f"Total amount: ${Total_cost:.2f}")