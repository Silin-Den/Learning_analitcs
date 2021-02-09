import sqlite3
import pandas as pd

db = sqlite3.connect('/Users/silinanata/hubway.db')


def run_query(query):
    return pd.read_sql_query(query, db)

query = '''
  SELECT *
  FROM trips 
  WHERE (duration) > 9990 AND (sub_type = "Registered")
  ORDER BY duration DESC
  LIMIT 15 
  ;
'''

df_hubway = run_query(query)
print(df_hubway)
