p = int(input ("Enter a number: "))
n = int(input("Enter another number: "))

if p>n:
    print("Hello")
    password = int(input("Enter a password in numeric: "))
    if password == 1234:
        game = input("Do you want to play the game? [Y/N]").upper()
        if game == "Y":
            print("Ok, play the game")
        else:
            print("Exit")
    else:
        print("Wrong Password. Please try again")
else:
    print("Bye")
count = int(input("Please enter a number: "))
while count>=5:
    print(count)
    count+=1 #count = count+1
