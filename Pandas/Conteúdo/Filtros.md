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
df_filtered = df[df['Coluna'].between(
```


