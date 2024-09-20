"""
The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. 
Then your program will compute the tax and tip for the meal. 
Use your local tax rate when computing the amount of tax owing. 
Compute the tip as 18 percent of the meal amount (without the tax). 
The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. 
Format the output so that all of the values are displayed using two decimal places.
"""

meal=float(input("Enter Cost:"))
tax_rate=float(input("Enter Rate:"))/100
tax_amt=meal*tax_rate
tip=(18/100)*meal
grand=meal+tax_amt+tip

print(f"Meal Amount: {meal :.2f}")
print(f"Tax Amount : {tax_amt :.2f}")
print(f"Grand Total : {grand: .2f}")