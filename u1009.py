vendedor=(input())
fixo=float(input())
vendas=float(input())
comissao=float(vendas*15/100)
total=(fixo)+(comissao)
print('TOTAL = R$ {:.2f}'.format(total))

