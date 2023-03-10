import random

def space():
  for i in range(40):
      print()

def EnterContinue():
  input("'Enter' to continue...")

class Player():

#Class variables to alternate first player for equalness
  current = 0
  seq = [0,1]

#Alternates first player
  def next():
    toReturn = Player.seq[Player.current]
    Player.current = Player.current + 1
    if Player.current == len(Player.seq):
      Player.current = 0
    return toReturn
    # returns 0 or 1

  def __init__(self, name):
    self.name = name
    self.points = 0
    self.hand = []
    #players total bet in the turn
    self.turn_bet = 0
    #indices to specify which cards to switch out
    self.indices = []
    self.move = ""
    self.allin = False
    self.winning = False

  def __str__(self):
    return str(self.name)

  #Deals the player a hand of 5 cards
  def getHand(self, cards):
        for i in range(5):
            self.hand.append(cards.pop(random.randint(0, len(cards) - 1)))

    #shows the player their hand that consists of 5 cards
  def peekHand(self):
    print()
    print("Your hand is...")
    print(self.hand)
    print()


  def play(self, opp):
      #A player can only play if they have more than $0
    if self.points != 0:
      if opp.move == "Check" or opp.move == '':
        print("1. Check")
        print("2. Bet")
        print("3. Fold")
        #Double checks for 'folds' in case of a free check
        doubleCheck = False
        while doubleCheck == False:
          move = int(input("Choose your move: "))
          if move == 1:
            doubleCheck = True
            return "Check"
          if move == 2:
            self.bet(opp)
            doubleCheck = True
            return "Bet"
          if move == 3:
            print()
            print("You have a free check!")
            print("1. Yes")
            print("2. No")
            yesno = int(input("Are you sure you want to fold? 1. Yes 2. No : "))
            if yesno == 1:
              doubleCheck = True
              return "Fold"

      if opp.move == "Bet" and self.move == "":
        print("Your opponent has betted $", opp.turn_bet)
        print()
        print("1. Call")
        print("2. Bet")
        print("3. Fold")
        move = int(input("Choose your move: "))
        if move == 1:
          self.call(opp)
          return "Call"
        if move == 2:
          self.bet(opp)
          return "Bet"
        if move == 3:
          return "Fold"

      if (self.move == "Bet") and (opp.move == "Bet"):
        print("Your opponent has betted $", opp.turn_bet)
        print("Would you like to call?")
        print()
        print("1. Call")
        print("2. Fold")
        move = input("Choose your move: ")
        if move == "1":
          self.call(opp)
          return "Call"
        if move == "2":
          return "Fold"

      if self.move == "Check" and opp.move == "Bet":
        print("Your opponent has betted $", opp.turn_bet)
        print("Would you like to call?")
        print()
        print("1. Call")
        print("2. Fold")
        move = input("Choose your move: ")
        if move == "1":
          self.call(opp)
          return "Call"
        if move == "2":
          return "Fold"

    else:
      print("You have $0")
      print("1. Check")
      move = input("Choose your move: ")

  def turn(self, opp):
    print()
    print(self, ", hit 'Enter' when you are ready.")
    EnterContinue()
    self.peekHand()
    print("You have $", self.points)
    self.move = self.play(opp)
    EnterContinue()
    space()

  def bet(self, opp):
    print()
    print("Your opponent has betted $", opp.turn_bet)
    print("You have $", self.points)

    bet = int(input("How much would you like to bet? "))
    while bet > int(self.points) or bet < 0 or bet <= opp.turn_bet:
      print("Invalid Value!")
      bet = int(input("How much would you like to bet? "))
    if bet == self.points:
      print("You 'All-In'ed!")
      self.allin = True
    self.turn_bet += bet
    self.points -= bet


  def call(self, opp):
    #Player needs to all-in to call
    if opp.turn_bet - (self.turn_bet + self.points) >= 0:
      self.turn_bet = self.turn_bet + self.points
      self.points = 0
      print("You have 'all-in'ed!")
    #Player has enough money to call
    else:
      self.points -= (opp.turn_bet - self.turn_bet)
      self.turn_bet = opp.turn_bet

  #Asks for the indices of the cards to switch
  def askIndex(self):
    self.peekHand()
    indices = []
    done = False
    while not done:
      index = input("Enter the index (0-4) of the cards you would like to get switched one by one (enter an empty string to exit): ")
      if index == '':
        done = True
      else:
        indices.append(int(index))
        print(indices)
    #The array needs to be reversed because popping from the beginning will change the indices of the following cards
    self.indices = reversed(sorted(indices))

  #removes cards with the indices and adds new ones
  #removed cards to not go back to deck
  def swap(self, cards):
    for i in self.indices:
      self.hand.pop(i)
      self.hand.insert(i, cards.pop(random.randint(0, len(cards) - 1)))
    return self.hand

  #Functions involved with switching out cards grouped together
  def changeCards(self, cards):
    print(self, ", hit 'Enter' when you are ready!")
    EnterContinue()
    self.askIndex()
    self.swap(cards)
    self.peekHand()
    EnterContinue()
    space()

  def win(self, opp, pot):
    #adds the total pot amount to winner's points
    print("Congratulations," , self, ", you win this round!")
    print("You win $", pot, ".")
    # if self.allin == True:
    #   self.points = self.???? make another instance variable?
    self.points += pot
    print()
    print(self, ": $", self.points)
    print(opp, ": $", opp.points)
    print()
    self.round_reset()
    opp.round_reset()
    EnterContinue()
    space()

  def turn_reset(self):
    self.turn_bet = 0
    self.move = ''

  def round_reset(self):
    self.hand = []
    self.turn_bet = 0
    self.indices = []
    self.move = ""
    self.winning = False
    self.allin = False
