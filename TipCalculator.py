print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

total_per_person = (bill / people) * (1 + (tip / 100))

print('Each person will pay: $' + str(total_per_person) + '0')
