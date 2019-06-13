import random
guess = int(input("Enter a number"));
rNum = random.randint(1, 101);
print(rNum)

while(guess != rNum):
    guess = int(input("Enter a number"));
    print("Please try again");
else:
    print("Good guess")
