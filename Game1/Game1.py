
def Level3():
    Lvl3 = input("Select the Odd One out: Elephant, Snake, Cows, Humans: ")
    if Lvl3 == "Snake":
        print("Great! Correct")
    else:
        print("Oops! Wrong Answer, Try Again!")
        Level3()
def Level2():
    Lvl2 = input("Select the Odd One out: Boat, Lawnmower, Car, Airplane: ")
    if Lvl2 == "Lawnmower":
        print("Thats the right answer!")
        Level3()
    else:
        print("Oops! Try Again!")
        Level2()
def Level1():
    Lvl1 = input("Select the Odd One out: Wood, Beef, Steak, Chicken: ")
    if Lvl1 == "Wood":
        print("Well Done, Correct!")
        Level2()
    else:
        print("Oops! Thats the wrong answer, try again!")
        Level1()
def MainMenu():
    print("Welcome to the Odd One Out!")
    print("Classic Mode (1)")
    print("Exit (2)")
    choice = input()
    if choice =="1":
        Level1()
    
    else:
        print("Enter a valid Choice")
        MainMenu()
print("Welcome to the Odd One Out!")
print("Made by Aditya Pilania")
name = input("Enter your name: ")
MainMenu()





 




         
        


    