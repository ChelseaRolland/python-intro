letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Building Point Dictionary
letter_to_points = {key:value for key, value in zip(letters, points)}
#print("Letters to Points: ", letter_to_points)

#Adding the blank tile
letter_to_points[" "] = 0
print("Letters to Points: ", letter_to_points)

#Score a Word
def score_word(word):
    point_total = 0
    word = word.upper()
    for letter in word:
        if letter in letter_to_points.keys():
            point_total += letter_to_points[letter]
        else:
            point_total += 0
    return point_total

print("Test 1.1: ", score_word("yay"))      #9 points
print("Test 1.1: ", score_word("cool"))     #6 points

print(score_word("BROWNIE"))                #15 points
