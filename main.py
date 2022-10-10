#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
#get the total bill amount

tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
#get the tip percent they would like to do

split = input("How many people to split the bill? ")
#get how many people they want to split the bill with

total_bill_float = float(total_bill)
#turn string from total_bill and turn it into a float

tip_percent_float = float(tip_percent)
#turn the string of the tip percent input into a float

tip2 = tip_percent_float / 100
#turn the whole number into a percent by diving by 100

split_float = float(split)
#turn split input into a float

result = (total_bill_float / split_float) * (1 + tip2)
#create result variable to to math operations to find out how much each person pays

result = round(result, 2)
#round the result by 2 decimal places

final_formatted = "{:.2f}".format(result)
#adding "{:.2f}".format(result) will display the second decimal when it is a zero. Ex. 33.60

print(f"Each person should pay: ${final_formatted}")
#this prints out the phrase and insert the result variable to find out how much each person will pay
