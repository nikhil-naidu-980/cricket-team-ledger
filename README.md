# Cricket Team Ledger

This repo contains custom python files to show a Cricket Team Ledger. I created this repo to address 2 issues my team was facing:

1. Keeping a track of how many players are taking part in the games actively each week?
2. To keep track of which player was part of the team on which day?

## General Pain Points:

Managing a cricket team can be hectic, cause it needs managing 20-30 players at a given point of time. On top of that, we also need to keep track of when was a player given an opportunity, what dates etc., Although MS Excel can be
used to solve these issues, it could be quite time taking and confusion.

The python scripts are created to help with these issues.

## Setup

1. Clone with repo with `git clone`
2. Latest version of Python

## Usage

1. Clone the repo and `cd cricket-team-ledger`
2. Make sure `team.csv` is updated with all the players who registered with the team (Include player names even if they played only one game) - `team.csv` is added as an example.
3. Create a `.csv` for each tournament, add each match day as a column followed by the team on that specific day - `whitby_league.csv` and `gtcc_league.csv` are added as a examples.
4. Run `python main.py` - this will create two new `.csv` files - `games_played.csv` and `dates_played.csv`

