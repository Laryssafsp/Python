md
# Tipos de Filtros em Pandas

## 1. Filtrar por valores em uma coluna
Filtra as linhas que correspondem a um valor específico.

```python
df_filtered = df[df['Coluna'] == 'Valor']
```
2. Filtrar por múltiplos valores (isin)
Seleciona linhas onde a coluna contém qualquer um dos valores especificados.

```python
df_filtered = df[df['Coluna'].isin(['Valor1', 'Valor2'])]
```
3. Filtrar por uma condição numérica
Filtra as linhas com base em uma operação lógica.

```python
df_filtered = df[df['Coluna'] > 10]  # Exemplo: valores maiores que 10
```
4. Filtrar por múltiplas condições (AND)
Filtra as linhas que atendem a múltiplas condições utilizando &.

```python
df_filtered = df[(df['Coluna1'] > 10) & (df['Coluna2'] == 'Valor')]
```
5. Filtrar por múltiplas condições (OR)
Filtra as linhas que atendem a pelo menos uma das condições utilizando |.

```python
df_filtered = df[(df['Coluna1'] > 10) | (df['Coluna2'] == 'Valor')]
```
6. Filtrar colunas específicas
Filtra apenas as colunas desejadas.

```python
df_filtered = df[['Coluna1', 'Coluna2']]
```
7. Filtrar por Data
Converte as datas e realiza o filtro.

```python
df['Data'] = pd.to_datetime(df['Data'])
df_filtered = df[df['Data'] == '2025-03-06']
filter_times = pd.to_datetime(['2025-03-06T10:21:30','2025-03-06T10:24:00', '2025-02-26T09:20:00'])

```
8. Filtrar com str.contains
Filtra as linhas com base em strings.

```python
df_filtered = df[df['Coluna'].str.contains('palavra', case=False, na=False)]
```
9. Filtrar linhas com valores ausentes (isna ou notna)
Inclui ou exclui linhas com valores NaN.

```python
# Filtrar linhas com NaN
df_filtered = df[df['Coluna'].isna()]

# Filtrar linhas sem NaN
df_filtered = df[df['Coluna'].notna()]
```
10. Filtrar por índice
Filtra as linhas com base nos índices.

```python
df_filtered = df.loc[[0, 1, 2]]  # Seleciona os índices 0, 1 e 2
```
11. Filtrar linhas por intervalos (entre)
Filtra as linhas que estão em um intervalo específico.

```python
df_filtered = df[df['Coluna'].between(10, 20)]
```

### Antes de tentar converter, é útil inspecionar os valores para identificar quais não são datas.
```python
# Identificar valores não convertíveis em datetime
invalid_values = df[~pd.to_datetime(df['WindowStartTime'], errors='coerce').notna()]
print(invalid_values)
```

###Filtrar Valores Inválidos Antes da Conversão
```python
# Remover valores inválidos antes da conversão
df = df[pd.to_datetime(df['WindowStartTime'], errors='coerce').notna()]
```

# Filtrando datas: 

### Filtrar por data específica (ignorar o horário)
```python
# Exemplo de DataFrame
data = {
    'WindowStartTime': ['2025-03-06T10:21:30', '2025-03-06T15:45:00', '2025-03-07T12:00:00'],
    'Interactive': [100, 200, 300],
    'Background': [50, 75, 125]
}
df = pd.DataFrame(data)

# Converter a coluna WindowStartTime para datetime
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])

# Filtrar por data específica (ignorar o horário)
filtered_df = df[df['WindowStartTime'].dt.date == pd.to_datetime('2025-03-06').date()]
```


### Filtrar por mais de uma data(ignorar o horário)
```python
# Lista de datas de interesse
dates_of_interest = [pd.to_datetime('2025-03-06').date(), pd.to_datetime('2025-03-07').date()]

# Filtrar o DataFrame
filtered_df = df[df['WindowStartTime'].dt.date.isin(dates_of_interest)]

print(filtered_df)
```

### Para filtrar os dados de um DataFrame pandas com base em um intervalo de horário (por exemplo, de 9h às 14h)
```python
# Exemplo de DataFrame
data = {
    'WindowStartTime': ['2025-03-06T08:30:00', '2025-03-06T10:21:30', '2025-03-06T14:15:00', '2025-03-06T09:45:00'],
    'Value': [100, 200, 300, 400]
}
df = pd.DataFrame(data)

# Converter a coluna WindowStartTime para datetime
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])

# Filtrar as linhas com horário entre 9h e 14h
filtered_df = df[df['WindowStartTime'].dt.hour.between(9, 14)]

print(filtered_df)
```

### Filtrar por mais de uma data(ignorar o horário)
```python

```



# Converter para datetime
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])
```

