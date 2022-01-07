import pandas as pd
from fastapi import BackgroundTasks


# Saving file to CSV & JSON
def parse_csv(df):
    data = df.to_json("data.json")
    data2 = df.to_csv("data.csv")
    return highest_val(df)


# Finding the Highest Val and save it as Json
# Can use if the columns are the same otherwise change the columns name
def highest_val(df):
    df1 = pd.DataFrame(df)
    max_max = df1[df1['customer_avrage_rating'] == df1['customer_avrage_rating'].max()]
    max_max.to_json("max.json", orient="records")
