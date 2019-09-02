def isWinner(score):
    scores = score.split("-")
    return int(scores[0]) > int(scores[1])

with open("ex6.csv") as f:
    lines = f.readlines()

games = [line.strip().split(",") for line in lines]

dic = {}

def addPlayers(players):
    for player in players:
        if dic.get(player, False) == False:
            dic[player] = []

for game in games:
    player1 = game[0]
    player2 = game[1]

    addPlayers([player1, player2])

    wins = 0
    matches = len(game[2:])

    for score in game[2:]:
        if isWinner(score):
            wins += 1

    if wins > matches - wins:
        winner = player1
        loser = player2
    else:
        winner = player2
        loser = player1

    dic[winner].append(loser)

print(dic)
