import pandas as pd

df = pd.read_csv('Titanic.csv')

from config import COL5_DROP
from preprocessing import drop_cols
drop_cols(df, COL5_DROP)

