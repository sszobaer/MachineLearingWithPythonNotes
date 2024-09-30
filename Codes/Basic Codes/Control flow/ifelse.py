p = int(input("Enter your number p: "))
n = int(input("Enter your number n:"))
if p>n:
    print("Hello World!")
    password = input("Enter a password: ")
    if password == "aiub":
        game = input("Do you want to play game[Y/N]").upper()
        if game == "Y":
            print("Ok, play the game")
        else:
            print("Exit")
else:
    print("Bye Bye")