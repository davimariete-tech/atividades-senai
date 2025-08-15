# atividade
import os 
os.system("cls")
print ("ola usuario , me indique dois numeros para serem operados")
print()


nu1= float(input("digite o primeiro numero: (operador)"))
nu2= float(input("digite o segundo numero: (operador)"))

soma= nu1 + nu2
sub= nu1 - nu2
mult= nu1 * nu2

divide= nu1 / nu2

print(f"soma : {soma:.2f}")
print(f"subtração : {sub:.2f}")
print(f"MULTIPICAÇÃO : {mult:.2f}")
print(f"divisão: {divide:.2f}")

