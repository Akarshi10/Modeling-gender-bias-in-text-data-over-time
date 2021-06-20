import pandas as pd


df_words= pd.read_csv ("L:/word.csv")
df_words.set_index("WORD", inplace = True)

new_df = df_words.apply (lambda s, n:pd.Series(s.nlargest(n).index), axis = 1, n=3)

new_df.to_excel(r'L:\top3_topics.xlsx', index = True, header = True)