Dados do exemplo
nome = "Ar-condicionado"
potencia = 9  # em watts (W)
horas_dia = 2  # horas por dia

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Resultado
print("--- Resultado ---")
print(f"Aparelho: {nome}")
print(f"Potência: {potencia} W")
print(f"Horas por dia: {horas_dia}h")
print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
