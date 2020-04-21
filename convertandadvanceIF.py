print('Choose Number')
print('1. Fahrenheit To Celsisus')
print('2. Celsius To Fahrenheit')
x = None
while x not in (1, 2):
    x = int(input('Input Your Number Here : '))
    if  x == 1:
        temperature = float(input('Please enter temperature in fahrenheit : '))
        celsius = (temperature - 32) * 5 / 9
        print("Temperature in celsius : " , celsius)
        break
    elif x == 2:
        celsius = float(input('Please enter temperature in celsius : '))
        fahrenheit = (celsius * 9 / 5) + 32
        print("Temperature in fahrenheit : " , fahrenheit)
        break
    print('Try Again')
    
