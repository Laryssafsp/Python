# Arquivo de Configurações e Utilidades para DataFrames Pandas

Este documento `.md` reúne um conjunto completo de **configurações
globais**, **ajustes diretos no DataFrame**, e **funções úteis** para
inspeção, análise e manipulação de DataFrames em Python com Pandas.\
O objetivo é servir como um **guia único e completo** para consulta
rápida.

------------------------------------------------------------------------

# 📌 1. Importação e Configurações Globais do Pandas

``` python
import pandas as pd
```

## 🔧 Ajustes de exibição (pd.set_option)

### ✔ Mostrar todas as linhas

``` python
pd.set_option('display.max_rows', None)
```

### ✔ Mostrar todas as colunas

``` python
pd.set_option('display.max_columns', None)
```

### ✔ Não cortar textos longos

``` python
pd.set_option('display.max_colwidth', None)
```

### ✔ Ajustar largura total da impressão

``` python
pd.set_option('display.width', None)
```

### ✔ Aumentar precisão decimal

``` python
pd.set_option('display.precision', 5)
```

### ✔ Evitar notação científica

``` python
pd.set_option('display.float_format', lambda x: f"{x:.4f}")
```

------------------------------------------------------------------------

# 📌 2. Configurações úteis aplicadas diretamente no DataFrame

## ✔ Visualizar informações gerais

``` python
df.info()
```

## ✔ Resumo estatístico

``` python
df.describe()
```

## ✔ Resumo estatístico apenas numéricos

``` python
df.describe(include=['float', 'int'])
```

## ✔ Resumo estatístico de todas as colunas (incluindo texto)

``` python
df.describe(include='all')
```

## ✔ Ver primeiros registros

``` python
df.head()
```

## ✔ Ver últimos registros

``` python
df.tail()
```

## ✔ Mostrar tipos das colunas

``` python
df.dtypes
```

## ✔ Contar valores únicos

``` python
df.nunique()
```

## ✔ Ver distribuição de um campo

``` python
df['coluna'].value_counts()
```

## ✔ Ver distribuição normalizada (percentual)

``` python
df['coluna'].value_counts(normalize=True)
```

## ✔ Renomear colunas

``` python
df.rename(columns={'AntigoNome': 'NovoNome'}, inplace=True)
```

------------------------------------------------------------------------

# 📌 3. Operações comuns no DataFrame

## ✔ Seleção de colunas

``` python
df['coluna']
df[['coluna1', 'coluna2']]
```

## ✔ Filtrar linhas (exemplos rápidos)

``` python
df[df['coluna'] == 'valor']
df[df['coluna'].str.contains('texto', na=False)]
df[df['valor'] > 10]
df[df['coluna'].between(10, 20)]
```

## ✔ Resetar índice

``` python
df.reset_index(drop=True, inplace=True)
```

## ✔ Ordenar

``` python
df.sort_values(by='coluna', ascending=True)
```

## ✔ Identificar valores nulos

``` python
df.isna().sum()
```

## ✔ Remover linhas duplicadas

``` python
df.drop_duplicates(inplace=True)
```

------------------------------------------------------------------------

# 📌 4. Conversão de Tipos

## ✔ Converter coluna para número

``` python
df['coluna'] = pd.to_numeric(df['coluna'], errors='coerce')
```

## ✔ Converter coluna para texto

``` python
df['coluna'] = df['coluna'].astype(str)
```

## ✔ Converter coluna para datetime

``` python
df['coluna'] = pd.to_datetime(df['coluna'], errors='coerce')
```

------------------------------------------------------------------------

# 📌 5. Manipulação Avançada

## ✔ Aplicar função em toda a coluna

``` python
df['nova'] = df['coluna'].apply(lambda x: x * 2)
```

## ✔ Aplicar função linha a linha

``` python
df['nova'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
```

## ✔ Criar coluna condicional

``` python
df['Status'] = df['valor'].apply(lambda x: 'Alto' if x > 10 else 'Baixo')
```

------------------------------------------------------------------------

# 📌 6. Agrupamento e Agregações

## ✔ Agrupar e somar

``` python
df.groupby('coluna').sum()
```

## ✔ Agrupar e contar

``` python
df.groupby('coluna').count()
```

## ✔ Agregações múltiplas

``` python
df.groupby('categoria').agg({
    'vendas': ['sum', 'mean', 'max'],
    'qtd': 'count'
})
```

------------------------------------------------------------------------

# 📌 7. Exportação de Dados

## ✔ Para CSV

``` python
df.to_csv('arquivo.csv', index=False)
```

## ✔ Para Excel

``` python
df.to_excel('arquivo.xlsx', index=False)
```

------------------------------------------------------------------------

# 📌 8. Outras Configurações Úteis

## ✔ Ver memória usada pelo DataFrame

``` python
df.memory_usage(deep=True)
```

## ✔ Ver número de linhas e colunas

``` python
df.shape
```

## ✔ Copiar DataFrame

``` python
df2 = df.copy()
```

------------------------------------------------------------------------

# 📌 9. Opções estéticas para melhorar inspeção

## ✔ Exibir todas as opções disponíveis

``` python
pd.describe_option()
```

## ✔ Restaurar opções padrão

``` python
pd.reset_option("all")
```

------------------------------------------------------------------------

# ✔ Final

Este arquivo reúne as **configurações mais completas** e os principais
comandos úteis do pandas.\
Ideal para ser usado como referência no dia a dia.
