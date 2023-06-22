clima = "sol"
dinheiro = 400
lugar = ""

if clima == "sol" and (dinheiro in range(300,501)):
    lugar = "clube"
else:
    lugar = "cinema"

print ("Vou ao", lugar)