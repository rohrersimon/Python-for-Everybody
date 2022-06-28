#Rewrite your pay computation with time-and-a-half for over-
#time and create a function called computepay which takes two parameters
#(hours and rate).

def computepay(c_hours, c_rate):
    if c_hours <= 40:
        c_pay = hours*c_rate
    else:
        c_payone = c_rate*40
        c_paytwo = (c_hours-40)*(c_rate*1.5)
        c_pay = c_payone+c_paytwo
    return c_pay

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

pay = computepay(hours, rate)

print('Pay:', pay)