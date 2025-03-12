## 1. Usando Seleção por Lista de Colunas
Se você sabe os nomes das colunas que deseja selecionar, use o seguinte formato:

```python
# Selecionar colunas específicas
colunas_desejadas = ['coluna1', 'coluna2', 'coluna3']
df_selecionado = df[colunas_desejadas]

print(df_selecionado)
```

## 2. Selecionar Apenas uma Coluna
Caso precise apenas de uma coluna específica, você pode usar:

```python
# Selecionar uma única coluna
coluna1 = df['coluna1']

print(coluna1)
```

## 3. Usando .loc para Selecionar Colunas Específicas
A função .loc permite selecionar linhas e colunas de maneira mais flexível:

```python
# Selecionar todas as linhas, mas apenas as colunas desejadas
df_selecionado = df.loc[:, ['coluna1', 'coluna2']]
print(df_selecionado)
```

## 4. Selecionando Colunas por Índice
Se você não conhece os nomes das colunas mas sabe a posição delas, use .iloc:

```python
# Selecionar por índices de colunas (exemplo: 0 e 2)
df_selecionado = df.iloc[:, [0, 2]]

print(df_selecionado)
```

## 5. Selecionar Todas Menos Algumas Colunas
Se você deseja excluir colunas específicas, pode usar o método drop:

```python
# Excluir uma ou mais colunas
df_selecionado = df.drop(['coluna_a_excluir'], axis=1)

print(df_selecionado)
```

