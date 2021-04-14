import pandas as pd
import numpy as np

# Creo una serie con Pandas
s = pd.Series([1,2,3,4,5,6, np.nan, 8,9,10])
print(s)

# Creo una serie di Date con "date_range", 10 in totale
d = pd.date_range('20200301', periods=10)
print(d)

#Creo una tabella multidimensionale con index = Data_Range e colonne le 4 lettere
df = pd.DataFrame(np.random.randn(10,4), index=d, columns=[
    'A','B','C','D'
])
print(df)

print("*******************")
# Creo un nuovo dataframe (tabella bi-dimensionale) - Colonna : campi della colonna
df2 = pd.DataFrame({'A':[1,2,3,4],
                    'B':pd.Timestamp('20200301'),
                    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D':np.array([5]*4, dtype='int32'),
                    'E':pd.Categorical(['true', 'false', 'true', 'false']),
                    'F': 'Edureka'
})
print(df2)
print("*******************")
print(df2.dtypes)
print("*******************")

# Ritorno a df
print("Ritorno alla prima tabella (df)")
print("\ndf - stampa tutto il dataframe")
print(df)
print("\ndf.head - stampa la meta superiore del dataframe")
print(df.head())
print("\ndf.tail - stampa la meta inferiore del dataframe")
print(df.tail())
print("\ndf.index - stampa l'index (la colonna 0 -> tutte le righe)")
print(df.index)
print("\ndf.colums - stampa tutte le colonne")
print(df.columns)
print("***** df.to_numpy -> converte il Dataframe in un array NumPy *****")
print(df.to_numpy())
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html?highlight=describe#pandas.DataFrame.describe
print("***** df.describe() -> racchiude una serie di statistiche descrittive *****")
print(df.describe())
print("\n***sort_index() -> ordina l'oggetto lungo gli assi: axis=0 o axis=1 ***")
print(df.sort_index(axis=1, ascending=False))
# Sono riordinate in ordine crescente rispetto la colonna C
print("\n***sort_value***")
print(df.sort_values(by='C'))
print("***********************")
print("***********************")
print("***********************")
print("Caso in cui voglio ritornare una intera colonna.")
print(df['C']) # Ritorna tutta e solo la colonna C in base all'indice
print("df[0:3")
print(df[0:3]) # Ritorna le righe dalla 0 alla 3 esclusa con tutte le colonne.

# loc = permette di accedere a una riga, una colonna, un campo a seconda di cosa viene dato in input
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html?highlight=loc#pandas.DataFrame.loc
print("Ritorna tutta la riga all'indice 0 in input:")
print(df.loc[d[0]])
print("***************")
# Ritorna tutte le righe ma solo le colonne A e C
print(df.loc[:,['A','C']])

# Ritorna una tabella (dataframe) dalla riga index 20200301 alla riga index 20200306 incluse, con le colonne C e D
print(df.loc['20200301':'20200306', ['D','C']])
print("***************")
print(df.loc['20200306', ['D','C']])
print("***************")
print("***** at *****")
# Mi stampa l'esatto valore completo della riga 0 colonna 'C'
print(df.at[d[0], 'C'])
print("***************")
print(df.iloc[3]) # Stampa le righe con indice 3 di colonna (iloc = index loc)
print("***************")
print("*** Stampa con iloc[3:5, 0:2] -> le righe da indice 3 a 5 e le righe da indice 0 a 2:")
print(df.iloc[3:5, 0:2])
print("\ndf[df['A'] > 0] = stampa il dataframe completo di solo righe con A>0")
print(df[df['A'] > 0])

print("*****************************")
print("*** Handling Missing Data ***")
print("*****************************")
# Stampo l'originale df2
# utilizzo reindex per sostiture il Dataframe db2 con df, avendo solo su df2 rige da 0 a 4 e nelle colonne ho tutti gli elementi di df + ultima colonna nuova creata settata tutta a NaN
print("DF2 Dataframe before:\n", df2)
df2 = df.reindex(index=d[0:4], columns=list(df.columns)+['E'])
print("DF2 Dataframe after:\n", df2)
# Potrei utilizzare df2.loc per settare i valori della colonna E

# Check se sono presenti campi vuoti
print(df2.isnull())

print("*** Prendi solo RxC che non hanno nessun campo vuoto:")
print(df2.dropna())

print("*** Riempi i campi NaN con value=2 ***")
print(df2.fillna(value=2))

# Stampa true / false a seconda che i campi siano Nan
print(pd.isna(df2))

# Different Pandas Operations
print("****************")
print("Different Pandas Operations")
# mean = Restituisce la media per asse richiesto! https://www.geeksforgeeks.org/python-pandas-dataframe-mean/#:~:text=mean()%20function%20return%20the,values%20for%20the%20requested%20axis.&text=If%20the%20method%20is%20applied%20on%20a%20pandas%20dataframe%20object,values%20over%20the%20specified%20axis.
print(df.mean())
print("** Posso fare la media per riga **")
print(df.mean(1))
print("** Posso fare la media per colonna **")
print(df.mean(0))

print("*****************")
s = pd.Series([1,2,3,np.nan,4,5,6,7,8,9], index=d).shift(2)
print(s)
# Posso sostituire tutte le righe null del Dataframe "s" nel Dataframe "df"
print(df.sub(s, axis='index'))

print("*** DF ***")
print(df)
print("\ncumsum:\n")
print(df.apply(np.cumsum))
print("*** lambda ***")
print(df.apply(lambda x:x.max()-x.min()))
print("*******")
### Histogrammy: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html
# Restituisce una serie contenente conteggi di righe univoche nel Dataframe
print(s.value_counts())
s = pd.Series(['Edureka', 'python', 'jupyter', np.nan, 'football', 'world']).str.upper()
print(s)

df = pd.DataFrame(np.random.randn(10,4))
print(df)

df2 = [df[:3], df[3:7], df[7:]]
print(df2)
print("*******")
print(pd.concat(df2))

left = pd.DataFrame({'A':[1,2], 'B':[3,4]})
right = pd.DataFrame({'A':[3,2], 'D': [4,5]})
print("left\n", left)
print("right\n", right)

#Effettuo il merge dei due dataframe secondo colonna A
m = pd.merge(left, right, on='A')
print(m)

print("*********")
print(df)

print(df.groupby([2,3]).sum())

### Merge, Group e Reshape
print("***********************")
print("****** RESHAPING ******")
print("***********************")
# Reshaping = rimodellare il Dataframe e le serie. Esistono diverse specifiche per rimodellare.
my_tuple = list(zip(*[[1,2,3,4,5,17,18,19],[11,1,2,6,7,8,9,10]]))
index = pd.MultiIndex.from_tuples(my_tuple, names=['First', 'Second'])
df = pd.DataFrame(np.random.randn(8,2), index=index, columns=['A','B'])
print(df)
a = df.stack()
print(a) # Altra visione
print(a.unstack())

print("***************")

df = pd.DataFrame({'A':['a','b','c','d']*3,
                    'B':['A','B','C']*4,
                    'C':['P','P','P','Q','Q','Q']*2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)
print("***************")

print(pd.pivot_table(df,values='D', index=['A','B'], columns=['C']))

print("**************************************")
print("**** TIME SERIES AND CATEGORICALS ****")
print("**************************************")

dates = pd.date_range('3/3/2020', periods=100, freq='S')
print(dates)
ts = pd.Series(np.random.randint(0,500, len(dates)), dates)
ts = ts.resample('5min').sum()
print(ts)

