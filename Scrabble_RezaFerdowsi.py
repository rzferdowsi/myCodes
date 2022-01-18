
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
# defining a function to calculat the score of a given word by adding the value of the letters.
def score_word(word):
  word=word.upper()
  # define a variable to update by adding each value to retun at the end.
  point_total = 0
  for letter in word:
    #point_total += letter_to_points[letter]
    #.get(key, the value retuned if the key dosen't exist) 
    point_total += letter_to_points.get(letter, 0)
  # print(point_total,"\n________________________")
  return point_total
print("BROWNIE:",score_word("BROWNIE"),"\n________________________")
player_to_words = {"player1":["BLUE","TENNIS","EXIT"], 	"wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}
player_to_points={}
#for all the keys in the list of keys that dic. has
for player in list(player_to_words):
  words = player_to_words[player]
  player_points=0
  # going to player list to calculat player's score.
  for word in words:
    player_points += score_word(word)
  #adding each player as key to dic. with the value of total points for thrir words.
  player_to_points[player]=player_points
print(player_to_points,"\n________________________")
#defining new function that gets a dic. with keys of players & the values are list of their chosen words to retun a new dic with keys of players and values are the points they got for their words.
def play_word(player_to_words):
  player_to_points={}
  for player in list(player_to_words):
    words = player_to_words[player]
    player_points=0
    for word in words:
      player_points += score_word(word)
    #adding each player as key to dic. with the value of total points for thrir words.
    player_to_points[player]=player_points
  #for line 35 is finished so all players with their points are added to dic.  
  return player_to_points
#defingin new function for camparing values of each players to see find winner.
def winner(dic):
  highscore=0
  #for key in all keys 
  for player in dic.keys():
    score = dic[player]
    if score > highscore:
      highscore = score
      winner = player
  return winner,highscore
dic={"Fri":["hosna","mahvash","h"],"Ferdowsi":["Top score","nothing"," "],"Reza":["hosna","mahvash","hi"],"Fe":["hosna","mahvash","hello"]}
scores=play_word(dic)
print(scores,"\n________________________")
print(f"The winner and the highest score are {winner(scores)}","\n________________________*")
"""The outcomes:
[('A', 1), ('B', 3), ('C', 3), ('D', 2), ('E', 1), ('F', 4), ('G', 2), ('H', 4), ('I', 1), ('J', 8), ('K', 5), ('L', 1), ('M', 3), ('N', 4), ('O', 1), ('P', 3), ('Q', 10), ('R', 1), ('S', 1), ('T', 1), ('U', 1), ('V', 4), ('W', 4), ('X', 8), ('Y', 4), ('Z', 10)] 
________________________
{'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10} 
________________________
{'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10, ' ': 0} 
________________________
BROWNIE: 15 
________________________
{'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31} 
________________________
{'Fri': 33, 'Ferdowsi': 29, 'Reza': 34, 'Fe': 37} 
________________________
The winner and the highest score are ('Fe', 37) 
________________________RF*"""
