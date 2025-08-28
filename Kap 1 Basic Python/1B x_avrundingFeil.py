# OBS! Pass på flyttall! Svaret blir ikke nøyaktig det du tror!!
# (Hvorfor?)

result = 0.1 + 0.2
print(result)  # 0.30000000000000004
print(result == 0.3)  # False!




import math

# Må bruke "isclose" fra math når man sjekker float!
result = 0.1 + 0.2
print("med isclose:", math.isclose(result, 0.3))  # True





# Eller manuelt med abs og en toleranse
tolerance = 1e-6 # 10^-6 = 0.000001
print("med tolerance:", abs(result - 0.3) < tolerance)  # True

# NB! Dette er grunnen til at man aldri bør bruke == for 
# å sammenligne floating-point tall - bruk alltid math.isclose() 
# eller sjekk om forskjellen er mindre enn en liten toleranse!
