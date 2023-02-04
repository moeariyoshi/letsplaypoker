# README | Final Project

This project was my final assignment for the Introduction to Computer Science class for the Fall 2022 semester.
We were given approximately 2 weeks.
We began brainstorming about what we wanted to create in the beginning of December
and submitted our final project on December 18.

My project is a 2-player poker game.

RULES:

For each turn, pass around the computer to see and play your hands.
After each player gets a hand, a player can play (check, bet/call or fold).
Each player gets one chance to switch out as many or no cards from their hand.
Then each player gets one more round of betting.
Finally, showdown to see who the winner is!
The game ends when a player has no points.

Hands
0: "high card",
1: "one pair",
2: "two pairs",
3: "three of a kind",
4: "straight",
5: "flush",
6: "full house",
7: "four of a kind",
8: "straight flush",
9: "royal flush"


As part of your submission, complete the responses below. Be sure to include your declaration of the Honor Code at the end of this file.

1. Names of anyone with whom you discussed the final project with:

William (Lab Helper)
Josh Dawson
Unknown Lab Helper Thursday 12/17  7-9pm

2. What did you learn during the process of creating your final project?

Even though it may seem that self.bet() (method) and self.bet (instance variable) are different,
the computer gets confused if we use the same name for a method and an instance variable.
As a solution, I used self.turn_bet for the instance variable.

During the process of creating this project,
I was able to solidify my understanding of the difference between the following two functions:
reverse(list) - returns a new different list with reverse content
list.reverse() - modifies the original list and does not have any returned objects

The same can be said with sort() and .sorted() .


3. What is one thing you wish you could have done differently?

I wish I had the time to have more players taking turns.
The difficulty of this was programming the bet method while pertaining to the rules of poker.

Another functionality I would have liked my project to have is the ability for the computer to recognize the hands
so that the computer can automatically declare the winner.
This could be implemented by constructing the cards by combining the suit and numbers from different arrays so we can keep track of the suits in the players' hand.

4. Honor Code Declaration:
I have adhered to the Honor Code in this assignment

# Grading

- Proposal: 9/10 points
-- No intermediate goals were listed
- Checkin: 2.5/5 points
-- Only some of the questions were answered
- Docs: 10/10 points
- Variables and Assignment: 2.5/2.5 points
- Conditionals: 5/5 points
- Nested Loops: 10/10 points
- Functions: 10/10 points
- Strings: 2.5/2.5 points
- Module: 5/5 points
- Data Structures: 10/10 points
-- Nice uses of classes!
- Style: 10/10 points
- Complexity: 5/5 points
- Correctness: 10/10 points
- README: 5/5 points

Total: 96.5/100 points

Great project!
