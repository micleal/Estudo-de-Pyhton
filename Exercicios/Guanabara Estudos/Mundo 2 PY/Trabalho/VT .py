dia = int(input('Digite quantos dias de trabalho no mês: '))
bu = float(input('Digite o valor da passagem do Bilhete Unico: '))
bom = float(input('Digite o valor da passagem do Bilhete Bom: '))
inte = float(input('Digite o valor da integração do Bilhete unico entre onibus e trem: '))
bumes = dia*((bu+inte)*2)
bommes = dia*(bom*2)
print('O valor de VT do Bilhete Unico R$ {:.2f} e o valor de VT do Bilhete Bom R$ {:.2f}'.format(bumes,bommes))