Para transformar seu DataFrame no formato que você descreveu, onde você tem uma coluna para cada aprovador e o respectivo email, você pode usar o groupby() para agrupar pelos objectid e depois aplicar uma transformação para redistribuir os nomes e e-mails de forma que cada objectid tenha até três aprovadores.
```python
import pandas as pd

# Criando o DataFrame de exemplo
data = {
    'objectid': [1, 1, 1, 2, 2, 3],
    'workspaces': ['WS1', 'WS1', 'WS1', 'WS2', 'WS2', 'WS3'],
    'name': ['Aprovador1', 'Aprovador2', 'Aprovador3', 'Aprovador1', 'Aprovador2', 'Aprovador1'],
    'email': ['email1@example.com', 'email2@example.com', 'email3@example.com', 'email1@example.com', 'email2@example.com', 'email1@example.com']
}

df = pd.DataFrame(data)

# Criando as colunas desejadas
df_grouped = df.groupby('objectid').agg(
    aprovador1=('name', lambda x: x.iloc[0] if len(x) > 0 else None),
    email1=('email', lambda x: x.iloc[0] if len(x) > 0 else None),
    aprovador2=('name', lambda x: x.iloc[1] if len(x) > 1 else None),
    email2=('email', lambda x: x.iloc[1] if len(x) > 1 else None),
    aprovador3=('name', lambda x: x.iloc[2] if len(x) > 2 else None),
    email3=('email', lambda x: x.iloc[2] if len(x) > 2 else None)
).reset_index()

print(df_grouped)


```

# Passo a passo do código:

## 1. `df.groupby('objectid')`:

O método `groupby()` agrupa as linhas do DataFrame com base em valores iguais na coluna `objectid`. Isso significa que ele vai criar subconjuntos de dados para cada valor único em `objectid`.

- **O que acontece aqui:** O DataFrame será agrupado pela coluna `objectid`, ou seja, todas as linhas que tiverem o mesmo `objectid` serão agrupadas juntas. 
- **Exemplo:** Se tivermos o `objectid` 1, todas as linhas com `objectid` igual a 1 serão agrupadas em um grupo.

## 2. `.agg()`:

O método `agg()` permite aplicar diferentes funções de agregação para cada coluna após o agrupamento.

- **O que acontece aqui:** Estamos utilizando o `agg()` para aplicar funções de agregação nas colunas `name` e `email`, de forma que queremos transformar esses dados na forma desejada. Ou seja, estamos criando novas colunas como `aprovador1`, `email1`, `aprovador2`, etc.

## 3. Dentro do `agg()`:

### 3.1. `aprovador1=('name', lambda x: x.iloc[0] if len(x) > 0 else None)`:

Aqui estamos criando a coluna `aprovador1`. Para cada grupo de `objectid`, selecionamos a primeira linha da coluna `name` com `x.iloc[0]`.

- **Explicação:** A função `lambda x: x.iloc[0] if len(x) > 0 else None` garante que, caso o grupo tenha pelo menos uma linha (isto é, um aprovador), pegamos o primeiro nome (`x.iloc[0]`). Caso contrário, se o grupo estiver vazio (não tem dados para aquele `objectid`), o valor retornado será `None`.

### 3.2. `email1=('email', lambda x: x.iloc[0] if len(x) > 0 else None)`:

De forma similar, estamos criando a coluna `email1` para o primeiro e-mail do grupo. A lógica aqui é a mesma: se o grupo tiver ao menos uma linha, pegamos o primeiro e-mail; caso contrário, retornamos `None`.

### 3.3. `aprovador2=('name', lambda x: x.iloc[1] if len(x) > 1 else None)`:

Aqui criamos a coluna `aprovador2`. Se o grupo de `objectid` tiver mais de 1 aprovador, pegamos o segundo nome (`x.iloc[1]`); caso contrário, colocamos `None`.

### 3.4. `email2=('email', lambda x: x.iloc[1] if len(x) > 1 else None)`:

Similar ao anterior, mas para o segundo e-mail do aprovador 2. Se houver ao menos dois aprovadores, pegamos o segundo e-mail, senão retornamos `None`.

### 3.5. `aprovador3=('name', lambda x: x.iloc[2] if len(x) > 2 else None)`:

Criamos a coluna `aprovador3`. Aqui, se houver pelo menos 3 aprovadores no grupo, pegamos o terceiro nome (`x.iloc[2]`); caso contrário, colocamos `None`.

### 3.6. `email3=('email', lambda x: x.iloc[2] if len(x) > 2 else None)`:

Similar ao anterior, mas para o terceiro e-mail do aprovador 3. Pegamos o terceiro e-mail se houver pelo menos três aprovadores; caso contrário, retornamos `None`.

## 4. `.reset_index()`:

Após aplicar o `groupby()` e o `agg()`, o índice do DataFrame será alterado. O `reset_index()` reinicia o índice do DataFrame.

- **O que acontece aqui:** Isso cria uma nova sequência de números para os índices do DataFrame, o que facilita o uso e visualização. Caso contrário, o índice original poderia ser alterado de forma que tornaria o DataFrame mais difícil de manipular.


