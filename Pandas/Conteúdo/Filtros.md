# Guia Completo de Filtros em Pandas

A seguir estão todos os modos de filtragem em pandas (incluindo os seus
e os que acrescentei), organizados por categorias e sem remover nada ---
apenas eliminadas duplicatas e estruturado de forma clara.

------------------------------------------------------------------------

# 1. Filtrar por igualdade / valores exatos

## ✔ Filtrar por um valor específico

``` python
df_filtered = df[df['Coluna'] == 'Valor']
```

## ✔ Filtrar por múltiplos valores (isin)

``` python
df_filtered = df[df['Coluna'].isin(['Valor1', 'Valor2'])]
```

## ✔ Excluir valores específicos (negação)

``` python
df_filtered = df[~df['Coluna'].isin(['Indesejado1', 'Indesejado2'])]
```

------------------------------------------------------------------------

# 2. Filtrar por condições numéricas

## ✔ Condição simples

``` python
df_filtered = df[df['Coluna'] > 10]
```

## ✔ Intervalo entre valores (between)

``` python
df_filtered = df[df['Coluna'].between(10, 20)]
```

------------------------------------------------------------------------

# 3. Filtrar com múltiplas condições

## ✔ AND

``` python
df_filtered = df[(df['Coluna1'] > 10) & (df['Coluna2'] == 'Valor')]
```

## ✔ OR

``` python
df_filtered = df[(df['Coluna1'] > 10) | (df['Coluna2'] == 'Valor')]
```

------------------------------------------------------------------------

# 4. Filtrar por strings (`str.contains`, etc.)

## ✔ Contém texto

``` python
df_filtered = df[df['Coluna'].str.contains('palavra', case=False, na=False)]
```

------------------------------------------------------------------------

# 5. Filtrar valores ausentes

## ✔ Somente valores NaN

``` python
df_filtered = df[df['Coluna'].isna()]
```

## ✔ Somente valores NÃO nulos

``` python
df_filtered = df[df['Coluna'].notna()]
```

------------------------------------------------------------------------

# 6. Filtrar por índices

``` python
df_filtered = df.loc[[0, 1, 2]]
```

------------------------------------------------------------------------

# 7. Selecionar colunas específicas

``` python
df_filtered = df[['Coluna1', 'Coluna2']]
```

------------------------------------------------------------------------

# 8. Filtrar datas

## ✔ Converter para datetime

``` python
df['Data'] = pd.to_datetime(df['Data'])
df_filtered = df[df['Data'] == '2025-03-06']
```

## ✔ Filtrar múltiplas datas (ignorando horário)

``` python
dates_of_interest = [
    pd.to_datetime('2025-03-06').date(),
    pd.to_datetime('2025-03-07').date()
]

filtered_df = df[df['WindowStartTime'].dt.date.isin(dates_of_interest)]
```

------------------------------------------------------------------------

# 9. Filtrar horários (intervalo de horas)

``` python
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])
filtered_df = df[df['WindowStartTime'].dt.hour.between(9, 14)]
```

------------------------------------------------------------------------

# 10. Identificar valores inválidos antes de converter datas

## ✔ Encontrar datas inválidas

``` python
invalid_values = df[~pd.to_datetime(df['WindowStartTime'], errors='coerce').notna()]
print(invalid_values)
```

## ✔ Remover datas inválidas

``` python
df = df[pd.to_datetime(df['WindowStartTime'], errors='coerce').notna()]
```

------------------------------------------------------------------------

# 11. Filtrar por data específica ignorando hora

``` python
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])
filtered_df = df[df['WindowStartTime'].dt.date == pd.to_datetime('2025-03-06').date()]
```

------------------------------------------------------------------------

# 12. Converter coluna em lista (extra)

``` python
lista = df['Coluna'].tolist()
```

# 13. Exibir coluna inteira sem truncar (extra)

``` python
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
print(df['Coluna'])
```
