pin=1234
n=0
tent=1
num=int(input("digite a senha: "))
while num!=pin and tent < 3:
    num = int(input("digite novamente: "))
    tent +=1
if num==pin:
        print("acesso liberado")
else:
        print("acesso negado")













