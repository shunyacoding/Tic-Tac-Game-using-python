# function to print Tic Tac Toe Board
def print_tic_t_t(values):
    print("\n")
    print("\t    |  |")
    print("\t { } | {} | {}".format(values[0], values[1], values[2]))
    print('\t__|__|__')

    print("\t    |  |")
    print("\t {} | {} | {}".format(values[3],values[4],values[5]))
    print('\t__|__|__')
          
    print("\t   |   |")      
    print("\t {} | {}  {}".format(values[6],values[7],values[8]))
    print("\t    |  |")
    print("\n")

    # function to print the score-board for the game
    def print_scoreboard(score_board):
        print("\t--------------------------------------------------")
        print("\t        SCOREBOARD FOR  TIC TAC TOE               ")
        print("\t---------------------------------------------------")

        players =list(score_board.keys())
        print("\t  ", players[0], "\t      ", score_board[players[0]])
        print("\t  ", players[1], "\t      ",score_board[players[1]])
        print("\t---------------------------------------------------\n")

        # function to check if any player has won the game 
        def check_winer(player_position,current_player):
            
            # All possible winning combinations for the players
            solution=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[1,6,9],[3,5,7]]

            # Loop to check if any winning combination is not satisfied or not
            for x in solution:
                if all(y in player_position[current_player]for y in x):  
                    # Return True if any winning combination satiesfies in the iteration
                    return True
                    # Return false if the above combination is not satisfied
                    return False
                
                # function to check if the game is draw
             # def check_draw(player_position):
                if len(player_position['x']) + len(player_position['o']) ==9:
                   return True 
               #  return False
            
            # function for a single Tic Tac Toe Game
          #
          #   def single_game(current_player) :

            # Represents the Tic Tac Toe     
           # values =['' for x in range(9)]

            # stores the position occupied by x and 0
          #  player_position ={'x' :[],   'o' :[]}

            # Game Loop for a single game of Tic Tac Toe
         # while True:
                   print_tic_t_t(values)

                   # Try exception block for MOVE input
                   try:
                    #   print("player",current_player, "turn,which box:",ends"")
                       move=int(input())
                   except  ValueError:
                       print("wrong input!!! Try Again")
                       continue
                   
                   # Sanity check  for move inout
                 # if move < 1 or move > 9 :
               # print("please choose the right number between 1to 9")   
             #  continue

             # check if the cell is occupied or not
             # if value[move-1] != '  ' : 
           #  print("The place you have chosen is already filled.Try again!!")
           # continue

           # update game status
           # updating board status
          # values[move-1] = current_player
        
        # updating player_positions
        player_position[current_player].append(move)

        # functional cell for checking winner
        if check_winer(player_position,current_player):
            print_tic_t_t(values)
            print("player",current_player,"has won the game!!")
            print("\n")
            return current_player
        
        # function cell for checking draw game 
      #  if check_draw(player_position):
    #  print_tic_t_t(values)
     #  print("Game is a Draw")
      # print("\n")
     # return 'D'

# switch player moves
#if current_player =='x'
    current_player='o'
# else:     current_player='x'


     
  #   if __name__=="_main_"
   #  print("player 1 Details")
   #  play1 =input("Enter the name of the player:")
   #  print("\n")
    #  print("player 2 details")
     #   print("\n")

# stores the player who choose x and o
    current_player=play1

# stores the choice of players character
player_choice= {'x' : "" , 'o ':  ""}

# stores the option
options=['x','o']

# stores the scoreboard details
   # score_board={play1: 0,play2: 0}
 #  print_scoreboard(score_board)

# Game Loop for a series of Tic Tac Toe 
#The Loop runs until either of the players choose to quit 
while True:

         # player choice menu
            print("Turn to choose for", 'current_player')
            print("Enter 1 for x")
            print("Enter 2 for o")
            print("Enter 3 for quit")

  # Try exception for choice input 
#try:
   #  choice = int(input())
# except valuerror:
      #  print("wrong input !!! Try Again\n")
     #   continue

    # condition for player choice 
   # if choice ==1
#player_choice['x']=current_player1:
         #   player_choice['o']=player2
else : 
            player_choice['o']=play1
# elif choice == 2         
#player_choice['o']= current_player
     # if current_player=player1:
player_choice['x='] = player2
#   else:
     #   print("wrongchoice!!! Try  Again\n")            

     # stores the winner in a single game of Tic Tac Toe                 
      #   winner=single_game(options[choice-1])
                                    
        # Edits the scoreboard according to the winner
        # if winner 1 ='D'
          #  player_won=player_choice[winner]
         #    score_board[player_won]=score_board[player_won]

         # print_scoreboard(score_board)
         #switch player who chooses x or o
         # if current_player==player1
            #  current_player=player2
    # else:
           # current_player=player1