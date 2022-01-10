
"""Scrabble
In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!
https://en.wikipedia.org/wiki/Scrabble"""


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
print(list(zip(letters,points)),"\n________________________")
letter_to_points={item[0]:item[1] for item in zip(letters,points)}
print(letter_to_points,"\n________________________")
letter_to_points[" "]=0
print(letter_to_points,"\n________________________")
def score_word(word):
  word=word.upper()
  point_total = 0
  for letter in word:
    point_total += letter_to_points[letter]
  # print(point_total,"\n________________________")
  return point_total
score_word("BROWNIE")
player_to_words = {"player1":["BLUE","TENNIS","EXIT"], 	"wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}
player_to_points={}
for player in list(player_to_words):
  words = player_to_words[player]
  player_points=0
  for word in words:
    player_points += score_word(word)
  player_to_points[player]=player_points
print(player_to_points)

"""Lets make a play function"""
def play_word(player_to_words):
  player_to_points={}
  for player in list(player_to_words):
    words = player_to_words[player]
    player_points=0
    for word in words:
      player_points += score_word(word)
    player_to_points[player]=player_points
  return player_to_points
"""Lets make a function to determine the winner"""
def winner(dic):
  highscore=0
  for player in dic.keys():
    score=dic[player]
    if score> highscore:
      highscore=score
      winner=player
  return winner,highscore
  
"Lets test the game with inputs, determining the winner"
dic={"Reza":["hosna","mahvash","hi"],"Ferdowsi":["Top score","nothing"," "]}
scores=play_word(dic)
print(scores)
print(f"The winner and the highest score are {winner(scores)}")

"""The outcome of the code:
[('A', 1), ('B', 3), ('C', 3), ('D', 2), ('E', 1), ('F', 4), ('G', 2), ('H', 4), ('I', 1), ('J', 8), ('K', 5), ('L', 1), ('M', 3), ('N', 4), ('O', 1), ('P', 3), ('Q', 10), ('R', 1), ('S', 1), ('T', 1), ('U', 1), ('V', 4), ('W', 4), ('X', 8), ('Y', 4), ('Z', 10)] 
________________________
{'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10} 
________________________
{'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0} 
________________________
{'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}
{'Reza': 34, 'Ferdowsi': 29}
The winner and the highest score are ('Reza', 34)"""
