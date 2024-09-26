print("************* CALCULADORA ****************")
print("Ingrese dos numeros por teclado")
# HAY QUE CONVERTIR EL TIPO DE DATO QUE VA A SER (en este caso int())
num_one = int(input("Ingrese el primer numero: ")) 
num_two = int(input("Ingrese el primer numero: "))

print("\n************** RESULTADOS *************"
     f"\nSuma: {num_one + num_two}",
     f"\nResta: {num_one - num_two}",
     f"\nMultiplicación: {num_one * num_two}",
     f"\nDivisión: {float(num_one / num_two)}",
     f"\nResto: {num_one % num_two}") 