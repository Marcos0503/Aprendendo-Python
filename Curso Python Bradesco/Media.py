notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informe a segunda nota: "))

#Calcular media
mediafinal = (notaA + notaB) / 2

#Verificação
if mediafinal >= 7.0:
    print("A Média: %.1f - Aprovado "% mediafinal)
else:
    print("A Média: %.1f - Reprovado" % mediafinal)