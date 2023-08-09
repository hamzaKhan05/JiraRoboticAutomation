def configure(FileName):
    import pandas as pd
    df=pd.read_csv(f"{FileName}.csv")
    return df.to_json(orient="records")
def filter():
    import pandas as pd
    df_jira=pd.read_csv("JiraToPythonDt.csv")
    configure=pd.read_excel("Configuration.xlsx",sheet_name='Sheet1')
    status=[]
    row=[]
    columns=[]
    for i in configure['Columns']:
        if isinstance(i,str):
            columns.append(i)
    for i in configure['Status']:
        if isinstance(i,str):
            status.append(i)
    for i in status:
        temp=df_jira[df_jira['Status']==f'{i}']
        for j in temp.index:
            row.append(df_jira.iloc[j])
    df_new=pd.DataFrame(row)
    df_filtered=df_new[columns] 
    return df_filtered.to_json(orient="records")