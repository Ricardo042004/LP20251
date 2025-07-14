import random
from biblioteca import input_int
'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1():
    lista = []
    for _ in range(15):
        lista.append(random.randrange(100))
    print(lista)
    numero = int(input_int('Digite um número a ser buscado: ',0,100))
    try:
        posicao = lista.index(numero)
    except ValueError:
        print(f'{numero} não localizado na lista')
    else:
        print(f'Localizado na posição: {posicao}')
        

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada. (ASCII 65-90)
def q2():
    letras = []
    for _ in range(10):
        letras.append(chr(random.randrange(65,91)))
    cont = 1
    for c in letras:
        print(f'{cont}: {c}')
        cont+=1

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)
def q21():
    qtde = input_int('Qtde de caracteres para a senha: ',8,20)
    senha = ''
    for _ in range(qtde):
        senha+=chr(random.randrange(40,127))
    print(f'Senha sugerida: {senha}')

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
# Lista para armazenar os 15 números
numeros = []

# Entrada dos 15 números
print("Digite 15 números:")

for i in range(15):
    num = int(input(f"{i+1}º número: "))
    numeros.append(num)

# Exibição com numeração e se é par ou ímpar
print("\nListagem:")
for i, num in enumerate(numeros, start=1):
    tipo = "par" if num % 2 == 0 else "ímpar"
    print(f"{i}. {num} - {tipo}")

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
# Lista para armazenar os 8 números
numeros = []

print("Digite 8 números inteiros:")

# Leitura dos números
for i in range(8):
    num = int(input(f"{i+1}º número: "))
    numeros.append(num)

# Imprime todos os números
print("\nNúmeros digitados:")
for i, num in enumerate(numeros, start=1):
    print(f"{i}. {num}")

# Conta múltiplos de 6
multiplos_de_seis = sum(1 for num in numeros if num % 6 == 0)

# Exibe o total
print(f"\nTotal de números múltiplos de 6: {multiplos_de_seis}")
#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q5():
    diario = []
    contchar = 65 # Código ASCII da letra A
    for _ in range(15):
        aluno = dict()
        aluno['nome'] = chr(contchar)
        contchar += 1 # Avançar para a próxima letra para representar o nome do próximo aluno
        aluno['n1'] = random.randrange(0,11)
        aluno['n2'] = random.randrange(0,11)
        aluno['media'] = round((aluno['n1'] + aluno['n2'])/2,1)
        aluno['situacao'] = 'AP' if aluno['media']>=6 else 'RP'
        diario.append(aluno)
    
    resultado = 'NOME\tN1\tN2\tMEDIA\tSITUACAO\n'
    for a in diario:
        resultado += f'{a["nome"]}\t{a["n1"]}\t{a["n2"]}\t{a["media"]}\t{a["situacao"]}\n'
    print(resultado)



#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
# Listas para armazenar os salários antigos e os reajustados
salarios_originais = []
salarios_reajustados = []

print("Digite o salário de 20 pessoas:")

# Leitura e cálculo
for i in range(20):
    salario = float(input(f"{i+1}º salário: R$ "))
    salarios_originais.append(salario)
    novo_salario = salario * 1.08  # reajuste de 8%
    salarios_reajustados.append(novo_salario)

# Exibição da listagem numerada
print("\nListagem de salários com reajuste de 8%:")
print("Nº\tSalário Original\tNovo Salário")
for i in range(20):
    print(f"{i+1}\tR$ {salarios_originais[i]:.2f}\t\tR$ {salarios_reajustados[i]:.2f}")

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
precos_compra = []
precos_venda = []

print("Digite o preço de compra e venda de 100 mercadorias:")

for i in range(100):
    compra = float(input(f"{i+1}º preço de compra: R$ "))
    venda = float(input(f"{i+1}º preço de venda: R$ "))
    precos_compra.append(compra)
    precos_venda.append(venda)

# Contadores para as faixas de lucro
lucro_menor_10 = 0
lucro_entre_10_e_20 = 0
lucro_maior_20 = 0

for compra, venda in zip(precos_compra, precos_venda):
    if compra == 0:
        # Evitar divisão por zero
        continue
    lucro_percentual = ((venda - compra) / compra) * 100

    if lucro_percentual < 10:

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.
produtos = {}

print("Cadastro de 30 produtos:\n")
for i in range(30):
    codigo = input(f"{i+1}º produto - Código: ").strip()
    while codigo in produtos:
        print("Código já existe. Digite um código único.")
        codigo = input("Código: ").strip()

    quantidade = int(input("Quantidade: "))
    valor_compra = float(input("Valor de compra: R$ "))
    valor_venda = float(input("Valor de venda: R$ "))

    produtos[codigo] = {
        "quantidade": quantidade,
        "compra": valor_compra,
        "venda": valor_venda
    }

# Escolha de listagem
print("\nConsulta de produtos:")
opcao = input("Digite 'T' para listar todos os produtos ou digite o código de um produto específico: ").strip()

if opcao.upper() == 'T':
    print("\nListagem completa dos produtos:")
    for cod, info in produtos.items():
        print(f"Código: {cod} | Quantidade: {info['quantidade']} | Compra: R$ {info['compra']:.2f} | Venda: R$ {info['venda']:.2f}")
elif opcao in produtos:
    info = produtos[opcao]
    print(f"\nProduto encontrado:\nCódigo: {opcao} | Quantidade: {info['quantidade']} | Compra: R$ {info['compra']:.2f} | Venda: R$ {info['venda']:.2f}")
else:
    print("Produto não encontrado.")
#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
import math

# Lista para armazenar os 10 números e seus fatoriais
numeros = []
fatoriais = []

print("Digite 10 números inteiros:")

# Leitura dos números e cálculo dos fatoriais
for i in range(10):
    num = int(input(f"{i+1}º número: "))
    numeros.append(num)
    fatoriais.append(math.factorial(num))

# Cálculo do maior, menor, média e percentual de pares
maior = max(fatoriais)
menor = min(fatoriais)
media = sum(fatoriais) / len(fatoriais)
quant_pares = sum(1 for f in fatoriais if f % 2 == 0)
percentual_pares = (quant_pares / len(fatoriais)) * 100

# Exibição dos resultados
print("\nLista original:", numeros)
print("Lista de fatoriais:", fatoriais)
print(f"Maior fatorial: {maior}")
print(f"Menor fatorial: {menor}")
print(f"Percentual de pares: {percentual_pares:.2f}%")
print(f"Média dos fatoriais: {media:.2f}")

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
import math

# Listas
numeros = []
fatoriais = []

# Entrada de 10 números
print("Digite 10 números inteiros:")

for i in range(10):
    num = int(input(f"{i+1}º número: "))
    numeros.append(num)
    fatoriais.append(math.factorial(num))

# Cálculo do maior e menor (sem ordenar)
maior = fatoriais[0]
menor = fatoriais[0]
soma = 0
pares = 0

for f in fatoriais:
    if f > maior:
        maior = f
    if f < menor:
        menor = f
    if f % 2 == 0:
        pares += 1
    soma += f

# Resultados
media = soma / len(fatoriais)
percentual_pares = (pares / len(fatoriais)) * 100

# Saída
print("\nLista de fatoriais:", fatoriais)
print(f"Maior fatorial: {maior}")
print(f"Menor fatorial: {menor}")
print(f"Percentual de números pares: {percentual_pares:.2f}%")
print(f"Média dos fatoriais: {media:.2f}")

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.
# Inicialização das mesas: 30 mesas com 5 lugares cada
mesas = [5] * 30  # índice 0 representa a mesa 1

total_lugares_ocupados = 0
total_lugares = 150

print("Sistema de reservas - Casa de Espetáculo (30 mesas, 5 lugares cada)")

while total_lugares_ocupados < total_lugares:
    try:
        codigo_mesa = int(input("\nDigite o código da mesa (1 a 30) ou 0 para sair: "))
        
        if codigo_mesa == 0:
            print("\nEncerrando o sistema de reservas.")
            break

        if not 1 <= codigo_mesa <= 30:
            print("Código inválido. Digite um valor entre 1 e 30.")
            continue

        lugares_desejados = int(input("Digite a quantidade de lugares desejados: "))

        index_mesa = codigo_mesa - 1  # ajustar para índice da lista

        if lugares_desejados <= 0:
            print("Quantidade de lugares deve ser maior que zero.")
            continue

        if lugares_desejados > mesas[index_mesa]:
            print(f"Não é possível reservar {lugares_desejados} lugar(es) na mesa {codigo_mesa}.")
            print(f"Restam apenas {mesas[index_mesa]} lugar(es) disponíveis.")
        else:
            mesas[index_mesa] -= lugares_desejados
            total_lugares_ocupados += lugares_desejados
            print(f"Reserva confirmada: {lugares_desejados} lugar(es) na mesa {codigo_mesa}.")
            print(f"Lugares restantes nessa mesa: {mesas[index_mesa]}")
            print(f"Lugares totais ocupados: {total_lugares_ocupados}/150")

    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

# Verifica se todos os lugares foram ocupados
if total_lugares_ocupados == total_lugares:
    print("\nTodas as mesas estão completamente reservadas. Encerrando o sistema.")
#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.
# Dicionário para armazenar os voos {número_do_voo: vagas_disponiveis}
voos = {}

# Cadastro dos 10 voos
print("Cadastro de 10 voos:")

for i in range(10):
    numero_voo = input(f"\n{i+1}º voo - Número do voo: ").strip()
    while numero_voo in voos:
        print("Número de voo já cadastrado. Digite outro.")
        numero_voo = input("Número do voo: ").strip()

    lugares = int(input("Quantidade de lugares disponíveis: "))
    voos[numero_voo] = lugares

# Processamento de reservas
print("\n--- Início das reservas ---")
while True:
    identidade = input("\nNúmero da identidade do cliente: ").strip()
    voo_desejado = input("Número do voo desejado (ou 0 para encerrar): ").strip()

    if voo_desejado == "0":
        print("\nEncerrando sistema de reservas.")
        break

    if voo_desejado in voos:
        if voos[voo_desejado] > 0:
            voos[voo_desejado] -= 1
            print(f"Reserva confirmada! Cliente {identidade} - Voo {voo_desejado}")
        else:
            print("Desculpe, não há mais lugares disponíveis nesse voo.")
    else:
        print("Voo não encontrado. Verifique o número e tente novamente.")
#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.
# Lista para armazenar os 50 números inteiros
lista_original = []
lista_quadrados = []

print("Digite 50 números inteiros:")

# Leitura e cálculo
for i in range(50):
    num = int(input(f"{i+1}º número: "))
    lista_original.append(num)
    lista_quadrados.append(num ** 2)

# Exibição
print("\nNúmero original\tQuadrado")
for original, quadrado in zip(lista_original, lista_quadrados):
    print(f"{original}\t\t{quadrado}")

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.
numeros = []

print("Digite até 100 números inteiros (digite 0 para parar):")

while len(numeros) < 100:
    num = int(input(f"{len(numeros)+1}º número: "))
    numeros.append(num)
    if num == 0:
        break

# Verificar se houve ao menos um número antes do 0
if len(numeros) > 1:
    ultimo_numero_valido = numeros[-2]  # penúltimo elemento (antes do 0)
    # Contar quantas vezes o último número válido aparece na lista (sem contar o 0)
    contagem = numeros[:-1].count(ultimo_numero_valido)
    print(f"\nO número {ultimo_numero_valido} foi lido {contagem} vez(es).")
else:
    print("\nNenhum número válido foi digitado antes do 0.")

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média
# Lista para armazenar os 100 números reais
numeros = []

# Entrada dos 100 números
print("Digite 100 números reais:")

for i in range(100):
    num = float(input(f"{i+1}º número: "))
    numeros.append(num)

# Contar quantos são iguais a 30
iguais_a_30 = sum(1 for n in numeros if n == 30)

# Calcular a média
media = sum(numeros) / len(numeros)

# Contar quantos são maiores que a média
maiores_que_media = sum(1 for n in numeros if n > media)

# Contar quantos são iguais à média
iguais_a_media = sum(1 for n in numeros if n == media)

# Exibir os resultados
print("\nResultados:")
print(f"Números iguais a 30: {iguais_a_30}")
print(f"Números maiores que a média ({media:.2f}): {maiores_que_media}")
print(f"Números iguais à média: {iguais_a_media}")

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.
# Lista para armazenar os 30 números inteiros
valores = []

# Leitura dos 30 valores
print("Digite 30 números inteiros:")

for i in range(30):
    num = int(input(f"{i+1}º número: "))
    valores.append(num)

# Impressão na ordem inversa
print("\nNúmeros na ordem inversa:")
for i, num in enumerate(reversed(valores), start=1):
    print(f"{i}. {num}")
#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.
# Lista para armazenar os 20 números
valores = []

print("Digite 20 números (podem ter repetidos):")

# Leitura dos 20 valores
for i in range(20):
    num = float(input(f"{i+1}º número: "))
    valores.append(num)

# Remover duplicatas usando set e ordenar o resultado
valores_unicos_ordenados = sorted(set(valores))

# Exibir a lista ordenada sem repetição
print("\nLista ordenada sem repetição:")
for i, num in enumerate(valores_unicos_ordenados, start=1):
    print(f"{i}. {num}")

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.
registros = {}

print("Cadastro de 30 códigos e telefones:")
for i in range(30):
    codigo = input(f"{i+1}º código: ").strip()
    telefone = input(f"{i+1}º telefone: ").strip()
    registros[codigo] = telefone

# Busca por código
print("\nBuscar telefone por código:")
codigo_busca = input("Digite o código a ser buscado: ").strip()

# Verifica e imprime o telefone correspondente
if codigo_busca in registros:
    print(f"Telefone correspondente: {registros[codigo_busca]}")
else:
    print("Código não encontrado.")
#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.
# Lista para armazenar os dados dos alunos

alunos = []

print("Digite a matrícula e a média de 100 alunos:")

# Leitura dos dados
for i in range(100):
    print(f"\nAluno {i+1}:")
    matricula = input("Matrícula: ").strip()
    media = float(input("Média: "))
    alunos.append((matricula, media))

# Ordenar da maior para a menor média
alunos.sort(key=lambda x: x[1], reverse=True)

# Imprimir a relação ordenada
print("\nRelação de alunos (ordenados por média decrescente):")
print("Matrícula\tMédia")
for matricula, media in alunos:
    print(f"{matricula}\t{media:.2f}")
questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')