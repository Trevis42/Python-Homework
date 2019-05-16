#Exercise 6
tempC = 0
print('Celsius','Fahrenheit', sep='\t\t')
while tempC <= 20:
    tempF = 9/5 * tempC + 32
    print(tempC, format(tempF,'10.1f'), sep='\t\t')
    tempC += 1
