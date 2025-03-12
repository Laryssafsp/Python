## Tipos de Merge
O parâmetro how no pd.merge() define o tipo de junção:

- how='inner': Inclui apenas as datas que existem em ambos os DataFrames.
- how='left': Inclui todas as datas de df1 e preenche valores ausentes para as datas que não existem em df2.
- how='right': Inclui todas as datas de df2 e preenche valores ausentes para as datas que não existem em df1.
- how='outer': Inclui todas as datas de ambos os DataFrames, preenchendo os valores ausentes onde necessário.

###  Se as colunas têm nomes iguais
```python
###  Converter a coluna 'Date' para datetime em ambos os DataFrames
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

###  Realizar o merge com base na coluna 'Date'
merged_df = pd.merge(df1, df2, on='Date', how='inner')  # Tipos de join: 'inner', 'left', 'right', 'outer'
```

---
### Se as colunas de data têm nomes diferentes nos DataFrames, use os parâmetros left_on e right_on:

python

```python
merged_df = pd.merge(df1, df2, left_on='Data1', right_on='Data2', how='inner'
```
