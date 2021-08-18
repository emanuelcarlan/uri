#leia os qautro valorer de dois pontos p1(x1,y1) e p2(x2,y2)
#calcule a distancia entre eles com 4 casa decimais apos a vigula
#entrada dua linhas de valors de ponto flutuante
import math
p1=input().split()
x1=float(p1[0])
y1=float(p1[1])

p2=input().split()
x2=float(p2[0])
y2=float(p2[1])

distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)

print("{:.4f}".format(distancia))




