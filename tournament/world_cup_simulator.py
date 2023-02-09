# Simulate a sports tournament

import csv
import random

# Number of simluations to run
N = int(input("Number of simulations to run: "))


def main():

    # Creating an empty list.
    teams = []
    # Reading teams into memory from file.
    filename = "fifa_2022.csv"
    # Opening filename as a readable file.
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        # Picking every key-value pair inside file (team and rating) and then casting ratings as an int.
        for team in reader:
            team["rating"] = int(team["rating"])
            # Adding every key value pairs into the empty list.
            teams.append(team)

    # Creating an empty dictionary.
    counts = {}
    # Simulating N tournaments.
    for iteration in range(N):
        # Declaring variable to keep track of win counts.
        winner = simulate_tournament(teams)
        # Adding into the winner count each team's results from tournament simulation.
        if winner in counts:
            counts[winner] += 1
        else:
            counts[winner] = 1

    # Printing each team's chances of winning, according to simulation.
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulating games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # Creating a loop that will check if length of teams higher than 1.
    while len(teams) > 1:
        # Keep simulating and eliminating teams from competition.
        teams = simulate_round(teams)
    # Returning the remaining team at index 0.
    return teams[0]["team"]


if __name__ == "__main__":
    main()
