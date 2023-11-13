import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bonus=[]
    for i in range(len(employees['salary'])):
        employees['bonus']=2*employees['salary']
    return employees