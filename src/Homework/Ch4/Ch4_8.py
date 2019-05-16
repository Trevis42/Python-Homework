#Exercise 8
nums = int(input('Enter any positive number to add to the sum(-555 to close): '))
total = 0
while nums > 0:
    total += nums
    nums = int(input('Enter any positive number to add to the sum(-555 to close): '))
print('\nTotal sum:', total)
