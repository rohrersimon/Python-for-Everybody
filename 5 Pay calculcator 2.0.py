#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

print ('Enter Hours:')
hours_string = input()
print ('Enter rate per hour:')
rate_string = input()
hours = float(hours_string)
rate = float(rate_string)

if hours <= 40:
    pay = hours*rate
else:
    payone = rate*40
    paytwo = (hours-40)*(rate*1.5)
    pay = payone+paytwo

print('Pay:', pay)