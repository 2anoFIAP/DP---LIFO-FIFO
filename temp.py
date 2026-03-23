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
        
        
        
def busca_largura(grafo, inicio, alvo):
    fila = [inicio]
    visitados = [inicio]

    while len(fila) > 0:
        atual = fila.pop(0)
        if atual == alvo:
            return f"Achei o {alvo}!"
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                fila.append(vizinho)
                visitados.append(vizinho)
    return "Nao encontrado"





    