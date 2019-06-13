num = int(input("Enter a number for factorial calculation"))

fact = 1

for i in range(1, num+1):
    fact *= i

print("The factorial of" + ' ' + "{}".format(num) + ' ' + "is" + ' ' + "{}".format(fact)) 