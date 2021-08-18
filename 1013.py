#leia 3 valores inteiros A,B,C
#apresente o maior com a mensagem (he o maior)
#fromula(a+b+abs+(a-b))/2
valor=input().split()
a=int(valor[0])
b=int(valor[1])
c=int(valor[2])
#maiorAB=int(a+b+abs(a-b))/2
#maiorABC=int(maiorAB+c+abs(maiorAB-c))/2
#print('{:.0f} he o maior'.format(maiorABC))

if(a>b and c):
    print('{} he o maior'.format(a))
    if(b>a and c):
       print('{} he o maior'.format(b))
elif(c>a and b):
           print('{} he o maior'.format(c))



        



