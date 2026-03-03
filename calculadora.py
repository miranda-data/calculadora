while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Digite apenas números.")

while True:
    try:
        num2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Digite apenas números.")

operacao= input("Digite a operação que deseja realizar: ")
if operacao== "+":
    print("O resultado da operação é: ", num1+num2)
elif operacao== "-":
    print("O resultado da operação é: ", num1-num2)
elif operacao== "*":
    print("O resultado da operação é: ", num1*num2)
elif operacao== "/":
  if num2== 0:
    print("Não é possível dividir por zero")
  else:
    print("O resultado da operação é: ", num1/num2)
elif operacao== "%":
    print("O resultado da operação é: ", num1%num2)
else:
    print("Operação inválida. Operadores permitidos apenas: +, -, *, /, ou %.")
