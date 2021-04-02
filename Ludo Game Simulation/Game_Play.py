import random
from ShowDice import show_dice


def through_dice():
    return random.randint(1,6)


def play_game():
    is_PlayerOne=True
    is_PlayerTwo=False
    is_PlayerThree=False
    
    print('''Press Enter to transfer control to other player
    or Press Q to exit the game : ''')
    
    while True:
        user=input()
        
        if user=="" and is_PlayerOne:
            print("*** Player 1 is playing ***")
            number = through_dice()
            show_dice(number)
            
            while number==6:
                number = through_dice()
                print("***Player one got 6 ***")
                print("Player 1 is playing again :")
                show_dice(number)
            
            is_PlayerOne = False
            is_PlayerTwo = True
            is_PlayerThree = False
            
        
        
        elif user=="" and is_PlayerTwo:
            print("*** Player 2 is playing ***")
            number = through_dice()
            show_dice(number)
            
            while number==6:
                number = through_dice()
                print("***Player two got 6 ***")
                print("Player 2 is playing again :")
                show_dice(number)
        
            is_PlayerTwo = False
            is_PlayerOne = False
            is_PlayerThree = True
            
        elif user=="" and is_PlayerThree:
            print("*** Player 3 is playing ***")
            number = through_dice()
            show_dice(number)
            
            while number==6:
                number = through_dice()
                print("***Player 3 got 6 ***")
                print("Player 3 is playing again :")
                show_dice(number)
                
            is_PlayerThree=False
            is_PlayerTwo = False
            is_PlayerOne = True
        
        elif user.lower() == "q":
            print("** Thank you for playing our game ***")
            break
    