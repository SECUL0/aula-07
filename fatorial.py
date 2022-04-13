def fatorial(n):
    fat = 1
    for i in range(2,n+1):
        fat = fat * i
    return fat

numero_inteiro = int(input("Digite o número que deseja saber o fatorial: "))
print("seu fatorial é:", fatorial(numero_inteiro))


# n = int(input("Digite o número que deseja saber o fatorial: "))
# fat = 1
# for i in range(2, n+1):
#     fat = fat * i
# print("seu fatorial é:", fat)