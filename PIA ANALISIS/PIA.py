# Demuestra la aplicación de objetos de pandas.
import pandas as pd

df_datos = pd.read_csv('datos.csv')

# print(df_datos.head())


# Filtrado de datos en un DataFrame de pandas
#mexico_df = df_datos[df_datos['PAÍS'] == 'MEXICO']
#print(mexico_df[["FECHA", "CONTAGIOS", "MUERTES", "PAÍS"]].head(10))

# Filtrado por valores nulos
#nulo_df = df_datos[df_datos["FECHA"].isnull()]
#print(nulo_df)

# Agrupar por México y mes, y obtener la suma de contagios y muertes
agrupado = df_datos.groupby('MES')[['CONTAGIOS', 'MUERTES']].sum().reset_index()
print(agrupado.head())

contagios_por_pais = df.groupby('PAIS')['CONTAGIOS'].sum().sort_values(ascending=False)
print(contagios_por_pais.head())

print(df_datos.columns)
df_datos.set_index('CONTAGIOS', inplace=True)
filtrado_loc = df_datos.loc[[10, 20]]
print("Filtrado con loc (por etiquetas):")
print(filtrado_loc)


contagios_por_anio = df.groupby('AÑO')['CONTAGIOS'].sum().sort_index()
print(contagios_por_anio)

media = df['CONTAGIOS'].mean()
mediana = df['CONTAGIOS'].median()
moda = df['CONTAGIOS'].mode()
rango = df['CONTAGIOS'].max() - df['CONTAGIOS'].min()


#Agrupar y sumar contagios por año
contagios_por_anio = df_datos.groupby('AÑO')['CONTAGIOS'].sum()
#Ordenarlos
contagios_por_anio = contagios_por_anio.sort_index()
#Graficar resultados
contagios_por_anio.plot(kind='bar', title='Contagios por año', figsize=(10,6), color='seagreen')
