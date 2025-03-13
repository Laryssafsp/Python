# Ao ler o arquivo, garantir que "WindowStartTime" seja tratada corretamente

```python
df = pd.read_excel('arquivo.xlsx', parse_dates=['WindowStartTime'])
```

# Configurar o Pandas para mostrar todas as colunas
```python
pd.set_option('display.max_columns', None)
```


# `df.Copy` ou `df1=df2` - Quando Usar Cada Um?

- `df_teste = df`:

Útil se você quiser trabalhar com a mesma instância de dados e espera que as alterações afetem o DataFrame original.

Cuidado ao usar, pois alterações em um afetarão o outro.

- `df_teste = df.copy()`:

Use sempre que precisar de uma cópia independente do DataFrame.

Ideal para evitar modificações acidentais no DataFrame original.

