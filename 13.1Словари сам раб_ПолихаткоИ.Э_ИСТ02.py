# 13.1 Словари сам раб
# 1)
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter: point for letter, point in zip(letters, points)}
# 2)
letter_to_points[""] = 0
# 3)-5)
def score_word(word):
    total_points = 0
    for letter in word.upper():
        total_points += letter_to_points.get(letter, 0)
    return total_points
# 6)
br = score_word("BROWNIE")
print(br)
# 7)
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}
# 8)
player_to_points = {}
# 9)-11)
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points
# 12)
print(player_to_points)

# Доп задания

