import players

Cards = ["SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK","CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK","HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK","DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK"]

def playout(p1, p2):
  p1.turn(p2)
  
  if p1.move == "Fold":
    p2.winning = True
    
  else: 
    p2.turn(p1)
    
    if p2.move == "Fold":
      p1.winnning = True 
      return 
    
    if p2.move == "Bet":
      
      p1.turn(p2)
      
      if p1.move == "Fold":
        p2.winning = True 
        return
        
def main():
  print("Welcome!")
  player1 = players.Player(input("Enter player 1 name: "))
  player2 = players.Player(input("Enter player 2 name: "))

  all_players = [player1, player2]

  done = False 
  while not done: 
    startPoint = int(input("Starting amount: $"))
    if startPoint > 0:
      done = True
  
  player1.points = startPoint
  player2.points = startPoint

  rounds = 0

  while player1.points > 0 and player2.points > 0: 
    rounds += 1

    print()
    print("Starting Round", rounds, "!")
    
    total_pot = 0

    #makes a new deck of cards with all 52 cards
    cards = Cards
    player1.getHand(cards)
    player2.getHand(cards)

    firstPlayer = all_players[players.Player.next()]

    if firstPlayer == player1:
      secondPlayer = player2
    else:
      secondPlayer = player1
    
    playout(firstPlayer, secondPlayer)
    
    total_pot = int(player1.turn_bet) + int(player2.turn_bet)

    if player1.winning == True:
      player1.win(player2, total_pot)

    if player2.winning == True:
      player2.win(player1, total_pot) 

    else:
      print("Total in the pot: $", total_pot)
      print()
      player1.turn_reset()
      player2.turn_reset()

      firstPlayer.changeCards(cards)
      secondPlayer.changeCards(cards)
      
      #Round 2
      playout(firstPlayer, secondPlayer)

      total_pot += player1.turn_bet + player2.turn_bet

      if player1.winning == True:
        player1.win(player2, total_pot)

      if player2.winning == True:
        player2.win(player1, total_pot) 

      else: 
        print("Total in the pot: $", total_pot)
        print()
        print("It's time for showdown!")
        print(player1, "has", player1.hand)
        print(player2, "has", player2.hand)
        print()
        print("1.", player1)
        print("2.", player2)
        round_winner = input("Who won? ")

        if round_winner == '1' or round_winner == player1.name:
          player1.win(player2, total_pot)
        if round_winner == '2' or round_winner == player2.name: 
          player2.win(player1, total_pot)
      
  else:
    if player1.points == 0:
      print("Congratulations,", player2 , "you win!")
    if player2.points == 0:
      print("Congratulations,", player1, "you win!")
  
    
if __name__ == '__main__':
  main()

