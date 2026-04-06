import heapq

from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

'''#Ex. 1

fila = ['cliente1', 'cliente2', 'cliente3', 'cliente4', 'cliente5']
print(fila)


cliente = fila.pop(0)
print(cliente)


#Ex. 2

fila = []
fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
fila.append('cliente4')
fila.append('cliente5')

print(fila)

cliente = fila.pop(0)
print(cliente)


#Ex. 3

fila = ['cliente1', 'cliente2', 'cliente3', 'cliente4', 'cliente5']
while fila:
    cliente = fila.pop(0)
    print(f"Atendendo {cliente}")
    
    

#Ex. 4
fila = ['cliente1', 'cliente2', 'cliente3', 'cliente4', 'cliente5']

i = 0

for i in range(len(fila)):
    cliente = fila.pop(0)
    print(f"Atendendo {cliente}")    
    
    
    '''
    
#Exercicio PDF
'''
fila_nome = []
nome = input("Qual seu nome: ")
fila_nome.append(nome)

for i in range(len(fila_nome)):
    cliente = fila_nome.pop(0)
    print(f"Atendendo {cliente}")
    while True:
        nome2 = input("algum cliente esta sendo atendido?")
        if nome2 == ("n" or "N"):
            print("Todos foram atendidos")
            break
        
        '''

#Estrutura baseada em pilha (last in first out)
'''
fila = ['A', 'B', 'C', 'D', 'E']
atendimento = fila.pop(0)
print(atendimento)

while fila:
    cliente = fila.pop(0)
    print(cliente)
'''

'''
fila = ['A', 'B', 'C', 'D', 'E']
atendimento = fila.pop()
print(atendimento)

pilha = []
pilha.append('cliente 1')
pilha.append('cliente 2')
pilha.append('cliente 3')
pilha.append('cliente 4')
pilha.append('cliente 5')

print(pilha)

pilha.pop()
'''

'''
def busca_largura(grafo, inicio, alvo):
    fila = [inicio]
    visitados = [inicio]

    while len(fila) > 0:
        atual = fila.pop()
        if atual == alvo:
            return f"Achei o {alvo}!"
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.append(vizinho)
    return "Nao encontrado"
'''

#Exercicio 1 : Crie uma estrutura para solicitar  peças, apos isso, cire uma estrutura para retirar as pecas por ordem LIFO,
#Utilize estrutura om while e for

'''pecas = []
for i in range(3):
    nomes = input("Digite o nome de uma peça: ")
    pecas.append(nomes)
    print(pecas)

while pecas:
    retirando = pecas.pop()
    print(f"Retirando peça {retirando}")
'''


#Exercicio 2 : Um escritorio recebe documentos que precisam ser processados. O utimo documento adicionado deve ser o primeiro a ser processsado.
# - Peça o nome dos documentos e os adicione a pilha.
# - Processe os documentos na ordem inversa a que foram adicionados (LIFO)
# - Apos processar todos documentos, exiba todos os documento q foram processados
'''
escritorio = []
while True:
    documentos = input("Digite o nome do documento: ")
    if documentos == 'fim':
        break
    escritorio.append(documentos)
    print(documentos)

for i in range(len(escritorio)):
    processar = escritorio.pop()
    print(f"Documentos processados {processar}")
'''

#Exercicio 3 : Um restaurante recebe pedidos de clientes  os coloca em uma fila para a cozinha. Cada pedido tem um nome
#e um tempo estimado de preparo.
# - Crie um programa que adicione pedidos a fila e exiba a ordem de preparr.
# - Ao servir um pedido, remova-o da fila e exiba quem sera servido em seguida.

'''restaurante = []
for i in range(3):
    nome = input("Diga seu pedido: ")
    tempo = int(input("Digite o tempo de preparo do pedido: "))
    pedido = (nome, tempo)
    restaurante.append(pedido)
print(restaurante)

restaurante.sort(key=lambda a: a[1])
print(restaurante)

for pedido in restaurante:
    print(f"Pedido: {pedido[0]} / Tempo: {pedido[1]}")
'''



#Exercicio 4 : Um hospital recebe pacientes e os coloca em uma fila de atendimento.
#Cada paciente tem um nivel de urgencia que varia de 1 (menos urgente) a 5 (mais urgente)
# - Crie um programa que adicioe pacientes a fila e atenda primeiro aqueles com maior nivel de urgencia
# - Se houver empate, siga a ordem de chegada.
'''
hospital = []
for  i in range(6):
    nome = input("Diga seu nome: ")
    urgencia = int(input("Qual o nivel da sua urgencia: (1-5)"))
    consulta = (urgencia, nome)
    hospital.append(consulta)
print(hospital)

hospital.sort(reverse=True)
print(hospital)

for consulta in hospital:
    print(f"Urgencia: {consulta[0]} / Paciente: {consulta[1]}")'''


#Exercicio 5 : Desenvolva um algoritmo para adicionar e remover clientes em ma lista.
#O algoritmo deve conter as seguintes escolhas para resolver o problema de filas FIFO:
#Opcao 1 = adicionar Cliente, em seguida, insira um valor.
#Opcao 2 = Atender Cliente
#Opcao 3 = Mostrar fila
#Opcao 4 = Sair

'''
fila_clientes = []

while True:
    print("\n--- MENU DE ATENDIMENTO ---")
    print("1 - Adicionar Cliente")
    print("2 - Atender Cliente")
    print("3 - Mostrar Fila")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == '1':
        nome = input("Qual seu nome: ")
        fila_clientes.append(nome)
    elif opcao == '2':
        if fila_clientes:
            atendido = fila_clientes.pop(0)
            print(f"Atendendo o cliente: {atendido}")
        else:
            print("Nao ha ninguem na fila para atender")
    elif opcao == '3':
        print(f"fila atual: {fila_clientes}")
    elif opcao == '4':
        print("Saindo......")
        break
    else:
        print("Opcao invalida!")


'''




#HEAP in python
'''fila = []

heapq.heappush(fila, (1, "Emergencia"))
heapq.heappush(fila, (3, "Consulta"))
heapq.heappush(fila, (2, "Exame"))
print(fila)

while fila:
    print(heapq.heappop(fila))
'''
'''fila = []

#Ex2
heapq.heappush(fila, ("Emergencia", 2))
heapq.heappush(fila, ("Consulta", 1))
heapq.heappush(fila, ("Exame", 3))
print(fila)

#converter para heap correto
fila_corrigida = [(prioridade, nome) for nome, prioridade in fila]
print(fila_corrigida)
'''

#CLASS em python
'''class Pilha:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        return self.itens.pop()


p = Pilha()
p.push(10)
print(itens)'''

class Pilha:
    def __init__(self):
        self.itens = []
    def push(self, item):
        self.itens.append(item)
    def is_empty(self):
        return
    def pop(self):
        if not self.is_empty:
            return self.itens.pop()
        return "Pilha Vazia"
    def peek(self):
        return len(self.itens) == 0

    def mostrar(self):
        return self.itens

p = Pilha()
p.push(10)
p.pop()
p.peek()
print(p.itens)



