'''
Exercício #3
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
'''

metros = float(input("Informe o tamanho em metros da area a ser pintada: "))
litros = float(metros / 3)

litros_lata = 18
preco_lata = 80

quantidade_latas = litros / litros_lata
total = quantidade_latas * preco_lata

print(f'Você usará {quantidade_latas} latas e  pagará {total} reais')


