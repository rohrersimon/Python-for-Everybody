print('Type farenheit value you want to convert to celsius:')
farenheit_string = input()
farenheit = float(farenheit_string)
celsius = (farenheit-32)/1.8
print(farenheit_string + ' Farenheit is Celsius:', celsius)