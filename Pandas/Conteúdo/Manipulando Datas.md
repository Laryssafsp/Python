# Manipulações de Datas: 



### Código para Ajustar para Hora Cheia
```python
df = pd.DataFrame(data)

# Converter a coluna WindowStartTime para datetime
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])

# Alinhar para a hora cheia
df['WindowStartTime_Hora_Cheia'] = df['WindowStartTime'].dt.floor('H')
print(df)
```
Ajuste para Hora Cheia: O método .dt.floor('H') arredonda os valores de WindowStartTime para baixo (truncar) até a hora mais próxima.

### Código para Ajustar para Minuto Cheia
```python
# Converter 'WindowStartTime' para datetime
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])

# Ajustar os tempos para o mesmo minuto (neste caso: 2025-02-28T09:28:00)
df['WindowStartTime'] = df['WindowStartTime'].dt.floor('T')  # Alinhar ao minuto inicial

# Agrupar os dados pela nova 'WindowStartTime' e somar os valores
df_agrupado = df.groupby('WindowStartTime').sum().reset_index()

print(df_agrupado)
```
Alinhar os tempos: O método .dt.floor('T') ajusta todos os valores para o início do minuto (por exemplo, 2025-02-28T09:28:00).

### Converter Correto dt Para datetime
```python
teste['WindowStartTime'] = pd.to_datetime(teste['WindowStartTime'], errors='coerce')
```


### Código para Ajustar para cada 30 segundos
```python
# Gerar valores de WindowStartTime a cada 30 segundos
inicio = "2025-02-28 09:00:00"  # Data e horário de início
fim = "2025-02-28 12:00:00"     # Data e horário de término

# Criar a sequência de WindowStartTime
window_times = pd.date_range(start=inicio, end=fim, freq='30S')

# Criar um DataFrame com a nova coluna
df = pd.DataFrame({'WindowStartTime': window_times})
print(df)
```


### Código para Ajustar para Intervalos de 30 Minutos
```python
# Converter a coluna para datetime
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])

# Arredondar para cada intervalo de 30 minutos mais próximo (baixo)
df['WindowStartTime_30Min'] = df['WindowStartTime'].dt.floor('30T')

# Arredondar para os 30 minutos seguintes
df['WindowStartTime_30Min'] = df['WindowStartTime'].dt.ceil('30T')
```

### Código para Agrupar por Data e Contar Linhas
```python
# Converter a coluna para datetime
df['WindowStartTime'] = pd.to_datetime(df['WindowStartTime'])

# Agrupar por data e contar o número de linhas
resultado = df.groupby(df['WindowStartTime'].dt.date).size().reset_index(name='Quantidade de Linhas')
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
