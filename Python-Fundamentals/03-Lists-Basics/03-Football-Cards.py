# 03. Football Cards

team_A = [i for i in range(1, 12)]
team_B = [i for i in range(1, 12)]

players_count_A = 11
players_count_B = 11

input_cards = input().split()

for element in range(len(input_cards)):
    if not input_cards:
        break
    card = input_cards[element].split('-')
    team = card[0]
    value = int(card[1])

    if team == 'A':
        if value in team_A:
            team_A.remove(value)
            players_count_A -= 1
    elif team == 'B':
        if value in team_B:
            team_B.remove(value)
            players_count_B -= 1
    if (players_count_A or players_count_B) < 7:
        break

print(f'Team A - {players_count_A}; Team B - {players_count_B}')
if players_count_A < 7 or players_count_B < 7:
    print('Game was terminated')

