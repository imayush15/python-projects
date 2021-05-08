x = int(input("Enter the Number to get its digit sum : "))
ones = x%10
x = x - ones
tens = x/10
print(ones + tens)