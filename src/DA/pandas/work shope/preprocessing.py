import pandas as pd

def read_file(file_path:str)->pd.DataFrame:
    return pd.read_csv(file_path)

def drop_cols(df:pd.DataFrame, cols:list[str])->pd.DataFrame:
    
    return df.drop(columns=cols)