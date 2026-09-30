"""
Aqeel Hussain
Sep 28, 2026 - Monday
lab 7: APIs and data collection
"""
import pandas as pd

# -------------------------
# 1. Example DataFrame
# -------------------------

dict_ = {'a': [11,21,31], 'b': [12,22,32]}

df = pd.DataFrame(dict_)

print(df.head())
print(df.mean())

# -------------------------
# 2. Get NBA teams
# -------------------------

from static import get_teams
nba_teams = get_teams()

print(f"First 2 teams: {nba_teams[:2]}")

# convert list of dictionary into a DataFrame
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

# filter the row that contains the 'Warriors' nickname
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print(df_warriors)

# access and save the id, which is the first row first column, of warriors
id_warriors = df_warriors[['id']].values[0][0]
print(f"Id of Warriors = {id_warriors}")

# -------------------------
# 3. Working with external API
# -------------------------
# a. download the pickle file
import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# save the download file as Golden_state.pkl
file_name = "Golden_State.pkl"

print("\nDownloading external data...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete")
else:
    print("Download failed")

# b. Load DataFrame from pickle
games = pd.read_pickle(file_name)
print("\nGames data from pickle file: ")
print(games.head())

# c. Filter GSW vs Raptors
warrior_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
gsw_home_vs_raptors = warrior_vs_raptors[warrior_vs_raptors['MATCHUP'].str.contains('vs. ')]
gsw_away_vs_raptors = warrior_vs_raptors[warrior_vs_raptors['MATCHUP'].str.contains('@ ')]

# d. calculate averages
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"Warriors home average {home_avg_plus}")
print(f"Warriors away average {away_avg_plus}")
print(f"Warriors home points average {home_avg_pts}")
print(f"Warriors away points average {away_avg_pts}")

print('\n------------------------- LAB EXERCISE -------------------------')
# pick two teams to work on step a through e.
# teams selected: Arsenal and Chelsea
# a. download the EPL CSV file
url = "https://datahub.io/football/english-premier-league/r/season-2324.csv"
file_name = "epl_matches.csv"

print("\nDownloading EPL data...")
response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete")
else:
    print("Download failed")

# b. load DataFrame from CSV
epl = pd.read_csv(file_name)

print("\nEPL data from CSV file:")
print(epl.head())

# c. filter Arsenal and Chelsea matches

# Arsenal matches
arsenal_matches = epl[
    (epl['HomeTeam'] == 'Arsenal') |
    (epl['AwayTeam'] == 'Arsenal')
]

# Chelsea matches
chelsea_matches = epl[
    (epl['HomeTeam'] == 'Chelsea') |
    (epl['AwayTeam'] == 'Chelsea')
]

print("\nArsenal matches:")
print(arsenal_matches.head())

print("\nChelsea matches:")
print(chelsea_matches.head())

# d. calculate averages

# Arsenal goals scored
arsenal_goals = (
    arsenal_matches['FTHG'].where(
        arsenal_matches['HomeTeam'] == 'Arsenal',
        arsenal_matches['FTAG']
    )
)

# Chelsea goals scored
chelsea_goals = (
    chelsea_matches['FTHG'].where(
        chelsea_matches['HomeTeam'] == 'Chelsea',
        chelsea_matches['FTAG']
    )
)

# Arsenal goals conceded
arsenal_goals_conceded = (
    arsenal_matches['FTAG'].where(
        arsenal_matches['HomeTeam'] == 'Arsenal',
        arsenal_matches['FTHG']
    )
)

# Chelsea goals conceded
chelsea_goals_conceded = (
    chelsea_matches['FTAG'].where(
        chelsea_matches['HomeTeam'] == 'Chelsea',
        chelsea_matches['FTHG']
    )
)

arsenal_avg_goals = arsenal_goals.mean()
chelsea_avg_goals = chelsea_goals.mean()

arsenal_avg_conceded = arsenal_goals_conceded.mean()
chelsea_avg_conceded = chelsea_goals_conceded.mean()

print(f"\nArsenal average goals scored: {arsenal_avg_goals:.2f}")
print(f"Chelsea average goals scored: {chelsea_avg_goals:.2f}")

print(f"Arsenal average goals conceded: {arsenal_avg_conceded:.2f}")
print(f"Chelsea average goals conceded: {chelsea_avg_conceded:.2f}")

# e. visualize

import matplotlib.pyplot as plt

metrics = ['Goals Scored', 'Goals Conceded']

arsenal_values = [
    arsenal_avg_goals,
    arsenal_avg_conceded
]

chelsea_values = [
    chelsea_avg_goals,
    chelsea_avg_conceded
]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))

plt.bar(
    [i - bar_width / 2 for i in x],
    arsenal_values,
    width=bar_width,
    label='Arsenal',
    color='red'
)

plt.bar(
    [i + bar_width / 2 for i in x],
    chelsea_values,
    width=bar_width,
    label='Chelsea',
    color='blue'
)

plt.xticks(x, metrics)

plt.title('Arsenal vs Chelsea — Average Goals Comparison')
plt.ylabel('Average Goals')
plt.legend()

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show(block=True)

input("Press Enter to close...")