# Parâmetros do `DataFrame.merge()` no pandas

Este documento descreve os parâmetros usados no exemplo:

``` python
df = df.merge(
    df_table_id,
    how="left",
    left_on="tgt_table_id",
    right_on="tableid",
    suffixes=("_base", "_src"),
)
```

## Parâmetros

### **`how`**

Define o tipo de junção: - `"left"`: mantém todas as linhas do DataFrame
da esquerda (`df`) e combina com o da direita.

### **`left_on`**

Coluna do DataFrame da esquerda usada como chave de junção.\
Neste caso: `tgt_table_id`.

### **`right_on`**

Coluna do DataFrame da direita usada como chave.\
Neste caso: `tableid`.

### **`suffixes`**

Define os sufixos adicionados a colunas com nomes duplicados após o
merge.\
Neste caso: - `"_base"` para colunas do DataFrame da esquerda. -
`"_src"` para colunas do DataFrame da direita\`.
