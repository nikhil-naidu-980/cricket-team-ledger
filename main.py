import os
import pandas as pd 
from team_functions import total_played, dates_played

team_file = "./team.csv"
data_folder = "./data"

team = pd.read_csv(team_file)
fname="Player First Name"
team[fname] = team[fname].str.upper().replace("\s", "", regex=True)
team_df = team[['Player First Name', ]].set_index(fname)

league_gp_df = team_df.copy()
league_dp_df = team_df.copy()

for x in os.listdir(data_folder):
    if ".csv" in x:
        print(x)
        ledger = pd.read_csv("./data/"+x)

        league_gp_df = league_gp_df.join(total_played(team_df, ledger, x.replace(".csv", "")))
        league_dp_df = league_dp_df.join(dates_played(team_df, ledger, x.replace(".csv", "")))

league_gp_df.to_csv("./games_played.csv")
league_dp_df.to_csv("./dates_played.csv")

