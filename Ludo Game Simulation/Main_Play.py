import Game_Play
import dev_credits


user_input=input('''Press S to start the Game
Press Q to Quit the Game
Press C to know the Credits : ''')

if user_input.lower() == 's':
    print("Welcome to Ludo Simulation")
    Game_Play.play_game()

elif user_input.lower() == 'q':
    print("Thank you for playing our Game")
    
elif user_input.lower() == 'c':
    dev_credits.developer_credits()