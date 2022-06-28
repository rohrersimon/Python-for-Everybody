#Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program.

print('Enter Hours:')
hours_string = input()
try:
    hours = float(hours_string)
except:
    print('Error, please enter numeric input')
    quit()


print('Enter rate per hour:')
rate_string = input()
try:
    rate = float(rate_string)
except:
    print('Error, please enter numeric input')
    quit()


if hours <= 40:
    pay = hours*rate
else:
    payone = rate*40
    paytwo = (hours-40)*(rate*1.5)
    pay = payone+paytwo

print('Pay:', pay)