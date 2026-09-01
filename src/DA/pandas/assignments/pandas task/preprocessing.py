import pandas as pd

def Read_data_file(file_path)-> pd.DataFrame:
    """
    Reads a CSV file and returns a pandas DataFrame.

    Parameters:
    file_path : The path to the CSV file
    
    Returns:
    pd.DataFrame : A DataFrame containing the data from the CSV file
    """
    try:
        df=  pd.read_csv(file_path)
        return df
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found")
        
    except Exception:
        print(f"An error occurred while reading the file at {file_path}")
        
        
        
def Drop_unnecessary_features(df: pd.DataFrame, cols_to_drop: list)-> pd.DataFrame:
    """
    Drops unnecessary features from the DataFrame.

    Parameters:
    df : The input DataFrame
    cols_to_drop : A list of column names to drop
    
    Returns:
    pd.DataFrame : A DataFrame with the specified columns dropped
    """
    df = df.drop(columns=cols_to_drop) 
    
    return df


def Check_data_type(df: pd.DataFrame)-> pd.DataFrame:
    """
    Checks the data types and unique values of each column.

    Parameters:
    df : The input DataFrame

    Returns:
    pd.DataFrame : A transpose DataFrame containing column names,
                   data types, and number of unique values
    """
    data_info = {
        
        "Columns Name" : df.columns,
        "Data Type" : df.dtypes,
        "Number of Unique Values" : df.nunique()
          
    }
    return pd.DataFrame(data_info).T


    

    
    
   
