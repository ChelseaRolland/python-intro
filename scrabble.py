letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Building Point Dictionary
letter_to_points = {key:value for key, value in zip(letters, points)}
#print("Letters to Points: ", letter_to_points)

#Adding the blank tile
letter_to_points[" "] = 0
#print("Letters to Points: ", letter_to_points)

#Score a Word
def score_word(word):
    point_total = 0
    #make sure word is in proper uppercase
    word = word.upper()
    #look thru each letter to compare it to the keys in dictionary
    for letter in word:
        if letter in letter_to_points.keys():
            #letter in letter dictionary, then add the value to the point total
            point_total += letter_to_points[letter]
        else:
            point_total += 0
    return point_total

#print("Test 1.1: ", score_word("yay"))      #9 points
#print("Test 1.1: ", score_word("cool"))     #6 points

brownie_points = score_word("BROWNIE")      #15 points
print(brownie_points)                       #15 points

#Score a Game

#setting up the players
players = ["player1", "wordNerd", "Lexi Con", "Prof Reader"]
words = [["BLUE", "TENNIS", "EXIT"], ["EARTH", "EYES", "MACHINE"], ["ERASER", "BELLY", "HUSKY"], ["ZAP", "COMA", "PERIOD"]]
player_to_words = {key:value for key, value in zip(players, words)}
print("Players to Words: ", player_to_words)

players_to_points = {}
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    players_to_points[player] = player_points
print(players_to_points)

def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word.upper())
    else:
        print("Not a player part of the game. Please enter a valid player name")

play_word("player1", "bacon")

def update_point_totals(player_to_words, players_to_points):
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        players_to_points[player] = player_points
    return players_to_points

print(update_point_totals(player_to_words, players_to_points))
