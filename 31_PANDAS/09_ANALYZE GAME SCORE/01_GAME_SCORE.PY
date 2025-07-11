import pandas as pd

# Sample game data
data = {
    'Player': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'Game': ['Chess', 'Chess', 'Chess', 'TicTacToe', 'TicTacToe'],
    'Score': [85, 92, 78, 90, 88]
}

df = pd.DataFrame(data)

# Total score per player
total_score = df.groupby('Player')['Score'].sum().reset_index()

print("Total Score per Player:")
print(total_score)

# Average score per game
avg_score = df.groupby('Game')['Score'].mean().reset_index()

print("\nAverage Score per Game:")
print(avg_score)
