import pandas as pd
import numpy as np


def gerar_dataframe(array):
    # criar um dataframe a partir do array
    df = pd.DataFrame(array, columns=["A", "B", "C"])
    print("Dataframe gerado com sucesso!")
    print(df)
    return df


def calcular_media(df):
    media = df.mean()
    print("Média calculada com sucesso!")
    print(media)


lista = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

df_final = gerar_dataframe(lista)
media_final = calcular_media(df_final)
