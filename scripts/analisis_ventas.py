import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("../datos/ventas.csv")

# Ventas totales
ventas_totales = df["monto"].sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Convertir fecha
df["fecha"] = pd.to_datetime(df["fecha"])

# Obtener mes
df["mes"] = df["fecha"].dt.month

# Ventas por mes
ventas_mes = df.groupby("mes")["monto"].sum()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Crear gráfico
ventas_mes.plot(kind="bar")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto vendido")

# Guardar gráfico
plt.savefig("../resultados/grafico_ventas.png")

print("Gráfico guardado correctamente")
