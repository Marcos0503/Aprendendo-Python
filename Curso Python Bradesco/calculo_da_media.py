def lernotas():
    n = float(input('Digite uma nota para o aluno(a): '))
    return n

def media(n1,n2):
    resultado = (n1+n2)/2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Media: ", resultado)
    if resultado >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
media(a,b)
