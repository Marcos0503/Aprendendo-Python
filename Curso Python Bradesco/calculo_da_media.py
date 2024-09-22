def lernotas():
    n = float(input('Digite uma nota para o aluno(a): '))
    return n

def media(n1,n2,n3):
    resultado = (n1+n2+n3)/3
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Nota 3: ", n3)
    print("Media: %.1f"% resultado)
    if resultado >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
c = lernotas()
media(a,b,c)
