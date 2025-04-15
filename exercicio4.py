alunos= int(input("quantos alunos tem na turma: "))
n=0
soma=0
while n < alunos:
    nota=int(input("digite a nota:" ))
    soma += nota
    n += 1
media= soma/alunos
print(f"a media da turma é: {media}")


