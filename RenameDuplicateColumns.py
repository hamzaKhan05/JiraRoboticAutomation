
def duplicates(In_FileNameArgument):
    import pandas as pd
    df=pd.read_csv(In_FileNameArgument)
    df.to_csv(In_FileNameArgument)
    return



