import pandas as pd


def pregunta_01():
    """
    Carga de datos.
    -------------------------------------------------------------------------------------
    """
    # Lea el archivo `insurance.csv` y asignelo al DataFrame `df`
    df =pd.read_csv("insurance.csv")

    # Asigne la columna `charges` a la variable `y`.
    variable_y = df['charges']
    return variable_y

print(pregunta_01()
)