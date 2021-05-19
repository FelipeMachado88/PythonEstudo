peso = float(input("Qual é o seu peso em Kg? "))
altura = float(input("Qual é a sua altura em cm? "))

IMC = peso/(altura/100)**2

int(print("O seu IMC é:",IMC))

if IMC<18.5:
    print("Você precisa se alimentar mais, está com índice de MAGREZA!")
elif IMC>=18.5 and IMC < 24.9 :
    print("Você está muito bem, parabéns! IMC NORMAL.")
elif IMC>=25 and IMC < 29.9 :
    print("Você precisa de atenção na sua alimentação, está com SOBREPESO. Classificado como obesidade grau I.")
elif IMC>=30 and IMC < 39.9 :
    print("Muito cuidado, você está com OBESIDADE grau II. Melhore seus hábitos alimentares e pratique exercícios.")
else :
    print("PODE PARAR DE COMER JÁ E CUIDE-SE, você está com OBESIDADE GRAVE grau III!")


