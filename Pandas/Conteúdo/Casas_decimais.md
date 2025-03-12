1. Usando round()
A função round() arredonda o número para o número especificado de casas decimais.

```python
numero = 3.14159
numero_arredondado = round(numero, 2)
print(numero_arredondado)  # Saída: 3.14
```

2. Usando format()
Você pode usar o método de string format para controlar a exibição.

```python
numero = 3.14159
numero_formatado = "{:.2f}".format(numero)
print(numero_formatado)  # Saída: 3.14
```

3. Usando F-strings (Python 3.6 ou superior)
As f-strings são uma forma moderna e eficiente de formatar strings.

```python
numero = 3.14159
numero_formatado = f"{numero:.2f}"
print(numero_formatado)  # Saída: 3.14
```

4. Atualizando um DataFrame no pandas
Se você está trabalhando com um DataFrame no pandas e quer deixar os números de uma coluna com 2 casas decimais:
```python
python
import pandas as pd

# Exemplo de DataFrame
data = {'Coluna': [3.14159, 2.71828, 1.61803]}
df = pd.DataFrame(data)

# Arredondar os valores na coluna
df['Coluna'] = df['Coluna'].round(2)

print(df)
```

5. Para deixar todas as colunas numéricas de um DataFrame pandas com apenas duas casas decimais.
Você pode usar o método .round() do pandas, que arredonda os valores das colunas especificadas. Aqui está como fazer isso:

 ```python
import pandas as pd

# Exemplo de DataFrame
data = {
    'Coluna1': [1.12345, 2.67891, 3.98765],
    'Coluna2': ['texto1', 'texto2', 'texto3'],
    'Coluna3': [4.55555, 5.66666, 6.77777]
}
df = pd.DataFrame(data)

# Arredondar apenas as colunas numéricas para 2 casas decimais
df[df.select_dtypes(include=['number']).columns] = df.select_dtypes(include=['number']).round(2)

print(df)

```
