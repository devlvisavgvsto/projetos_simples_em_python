primeiro_termo = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
quantos_termos_user = int(input('Quantos termos da PA: '))

quantos_termos = primeiro_termo + (razao * quantos_termos_user)

for termo in range(primeiro_termo, quantos_termos, razao):
    print(f'{termo}', end='->')
print(' Terminou!')
