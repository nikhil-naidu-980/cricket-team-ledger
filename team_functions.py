import pandas as pd

def total_played(team, ledger, result_column_name="Games_Played"):
    full_schedule_df = team.copy()
    for x in ledger.columns.tolist():
        today_df = ledger[[x]]
        today_df[x] = today_df[x].str.upper()
        
        today_df = today_df.set_index(x)
        today_df.index = today_df.index.rename('player')
        today_df[x+"_flag"]=1
        today_df = today_df[[x+"_flag"]]
        full_schedule_df = full_schedule_df.join(today_df)
    full_schedule_df = full_schedule_df.fillna(0)
    
    return(pd.DataFrame(full_schedule_df[[i for i in full_schedule_df.columns.tolist() if "_flag" in i]].sum(axis=1), columns=[result_column_name]))

def dates_played(team, ledger, result_column_name="Dates_Played"):
    full_schedule_df = team.copy()

    for x in ledger.columns.tolist():
        today_df = ledger[[x]]
        today_df[x] = today_df[x].str.upper().replace("\s", "", regex=True)
        today_df = today_df.set_index(x)
        today_df.index = today_df.index.rename('player') 
        today_df[x+"_flag"]=str(x)
        today_df = today_df[[x+"_flag"]]
        full_schedule_df = full_schedule_df.join(today_df)
        
    full_schedule_df = full_schedule_df[[i for i in full_schedule_df.columns.tolist() if "_flag" in i]]
    full_schedule_df = full_schedule_df.agg(lambda x: "".join(x.dropna()), axis=1)
    return(pd.DataFrame(full_schedule_df, columns=[result_column_name]))
