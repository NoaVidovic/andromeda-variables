def where(cond, df):
    return df.loc[cond]

def where_eq(column, eq, df):
    return where(df[column] == eq, df=df)