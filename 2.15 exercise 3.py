print ('Enter Hours:')
hours_string = input()
print ('Enter rate per hour:')
rate_string = input()
hours = float(hours_string)
rate = float(rate_string)
pay = hours*rate
print('Pay:', pay)