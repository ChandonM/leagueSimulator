import random

A_wins = 0
A_draws = 0
A_losses = 0

for i in range(1000000):
    A_total = 53
    C_total = 47

    for j in range(14):
        rand_1 = random.random()
        rand_2 = random.random()

        if rand_1 < 0.6604:
            A_total += 3
        elif rand_1 < 0.87:
            A_total += 1

        if rand_2 < 0.6244:
            C_total += 3
        elif rand_2 < 0.831:
            C_total += 1

    if A_total > C_total:
        A_wins += 1
    elif A_total == C_total:
        A_draws += 1
    else:
        A_losses += 1

print("Arsenal wins: " + str(A_wins))
print("Arsenal draws: " + str(A_draws))
print("Arsenal losses: " + str(A_losses))
