idade = int(input("Digite sua idade: "))
contr = int(input("Digite quantos anos vc tem de contribuição: "))
sexo = input("Digite seu sexo, f ou m : ")

if sexo == 'm':
    idadeAposentadoria = 65
    anosContr = 15
    if idade >= idadeAposentadoria & contr >= anosContr:
        print("Aposentadoria por idade liberada!!")
    else:
        if idade >= 62 & contr >= 35:
            print("Aposentadoria por contribuição liberada")
        else: 
            print("Aposentadoria não liberada")
    
elif sexo == 'f':
    idadeAposentadoria = 62
    anosContr = 15
    if idade >= idadeAposentadoria & contr >= anosContr:
        print("Aposentadoria por idade liberada!!")
    else:
        if idade >= 57 & contr >= 30:
            print("Aposentadoria por contribuição liberada")
        else: 
            print("Aposentadoria não liberada")

else:
    print("O sexo foi digitado de forma errada, precisa ser f ou m")
