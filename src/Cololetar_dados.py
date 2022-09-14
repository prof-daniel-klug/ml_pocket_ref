import pandas as pd

def coletar_dados():
    
    url = "https://hbiostat.org/data/repo/titanic3.xls"
    df = pd.read_excel(url).clean_names()
    
    return df