### Código para Remover Uma Coluna

```python
# Remover a coluna 'Coluna2'
df = df.drop('Coluna2', axis=1)
```
Explicação
1. `drop('Coluna2', axis=1)`:
- O parâmetro 'Coluna2' especifica qual coluna remover.
- O axis=1 indica que estamos trabalhando com colunas (e não linhas).

2. Atribuição ao Mesmo DataFrame (`df = df.drop(...)`):
- Certifique-se de atribuir o resultado ao DataFrame original ou a um novo, pois o método `.drop()` não modifica o DataFrame em lugar (inplace) por padrão.

### Remover Múltiplas Colunas
```python
df = df.drop(['Coluna2', 'Coluna3'], axis=1)
```
Usar inplace (Opcional)
```python
df.drop('Coluna2', axis=1, inplace=True)
```
### 
```python


```

### 
```python


```

### 
```python


```

### 
```python


```
