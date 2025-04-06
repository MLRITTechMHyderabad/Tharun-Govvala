import numpy as np
points = np.array([
    [10, 25, 30, 22, 12, 18, 26, 32, 24, 29],
    [20, 15, 12, 28, 24, 26, 30, 18, 22, 25],
    [35, 30, 32, 40, 28, 34, 29, 31, 26, 37],
    [12, 18, 20, 15, 22, 14, 19, 21, 23, 17],
    [28, 26, 27, 25, 30, 29, 35, 32, 31, 38]
])

avg_points=np.mean(points,axis=1)
print("Average points per game:\n",avg_points )

total=np.sum(points,axis=1)

best_max = np.max(total)
best_player = np.argmax(total)
print("Best-performing player: Player",best_player," (Total: ",best_max ,"points)")

worst = np.min(total)
worst_player = np.argmin(total)
print("Worst-performing player: Player",worst_player," (Total: ",worst ,"points)")

sorted_players = np.argsort(total)[::-1] + 1  
print("Players sorted by total points:")
for player in sorted_players:
    print(f"Player {player} - {total[player-1]} points")