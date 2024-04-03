
""" CONTROLAR A ADIÇÃO DE OBSTÁCULOS
    AJEITAR A PARTE DO OBSTÁCULO NO PONTO INICIAL
"""


import heapq
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x # ---> Coordenada x e y
        self.y = coord_y
        self.cost = float('inf')   #----> o custo e a heuristica inicia com inf pq ainda não tem um valor associado e ele
        self.heuristic = float('inf')
        self.prev = None
    
    """ Esse método aqui compara dois nós e verifica se o custo + heuristica é maior ou menor, como a solução
    usa o algoritmo A* para encontrar a melhor solução, essa comparação é feita e o menor é seguido"""
    # def compare(self, other):
    #     return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

""" Essa função aqui calcula a heuristica entre o ponto atual e o ponto que se deseja chegar (distância de manhatam)"""
def calculate_heuristic(atual, objetivo):  
    return abs(atual.x - objetivo.x) + abs(atual.y - objetivo.y)

"""" Essa função encontra os vizinhos de um nó.
Ela recebe como parametro o nó atual e uma lista com a coordenada dos obstáculos,
a lista moves (movimentos) armazena todos os possiveis movimentos que o algoritmo pode fazer,
o loop for itera sobre os movimentos possiveis e atualiza a posição atual do no, em seguida verifica se 
essa nova coordenada está dentroda lista de obstáculos, se não estiver, ele é adicionado à lista neighbors (vizinhos).
"""
def neighbors(node, obstacles):
    neighbors = []
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]  # Movimentos ortogonais básicos

    # Adicionando movimentos ortogonais ao longo das laterais dos obstáculos
    moves += [(dx, dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)] for x, y in [(node.x + dx, node.y + dy)] if (x, y) in obstacles]

    for dx, dy in moves:
        new_x, new_y = node.x + dx, node.y + dy
        if 0 <= new_x <= 10 and 0 <= new_y <= 10:  # Verifica se as coordenadas estão dentro dos limites
            if (new_x, new_y) not in obstacles or (node.x + dx, node.y) in obstacles or (node.x, node.y + dy) in obstacles:
                neighbors.append(Node(new_x, new_y))
    return neighbors




def a_star(start, goal, obstacles):
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)
    start.cost = 0
    start.heuristic = calculate_heuristic(start, goal)

    while open_list:
        current = heapq.heappop(open_list)

        if (current.x, current.y) == (goal.x, goal.y):
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.prev
            return path[::-1]

        closed_set.add((current.x, current.y))
        
        if not neighbors:  # Se não houver vizinhos disponíveis
            continue
        
        for neighbor in neighbors(current, obstacles):
            if (neighbor.x, neighbor.y) in closed_set:
                continue

            tentative_g = current.cost + 1
            if tentative_g < neighbor.cost:
                neighbor.prev = current
                neighbor.cost = tentative_g
                neighbor.heuristic = calculate_heuristic(neighbor, goal)
                heapq.heappush(open_list, neighbor)

    return None


def plot_grid(obstacles, path):
    fig, ax = plt.subplots()

    for obstacle in obstacles:
        ax.add_patch(plt.Rectangle((obstacle[0], obstacle[1]), 1, 1, color='gray'))

    if path:
        # Ajustar o trajeto para começar nos cantos das células do grid
        adjusted_path = [(x, y) for x, y in path]
        x_values, y_values = zip(*adjusted_path)
        ax.plot(x_values, y_values, color='blue')

    ax.set_xticks(range(12))  # Define os ticks do eixo x em incrementos de 1
    ax.set_yticks(range(12))  # Define os ticks do eixo y em incrementos de 1
    
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()


def generate_obstacles(start, grid_size, num_obstacles):
    obstacles = set()
    
    # Adiciona o ponto inicial à lista de obstáculos temporariamente
    obstacles.add((start.x, start.y))
    
    while len(obstacles) < num_obstacles + 1:  # Adiciona 1 para compensar o ponto inicial
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        if not any(abs(x - obs_x) <= 1 and abs(y - obs_y) <= 1 for obs_x, obs_y in obstacles):
            obstacles.add((x, y))
    
    # Remove o ponto inicial da lista de obstáculos
    obstacles.remove((start.x, start.y))
    
    return obstacles


def main():
    start = Node(0, 0)
    goal = Node(10,10)
    #obstacles = {(2, 3), (3, 3), (6, 4), (5, 5),(1,1)}  
    obstacles = generate_obstacles(start, 12, 30)
    
    path = a_star(start, goal, obstacles)
    
    print(obstacles)
    
    if path:
        print("Caminho encontrado:")
        print(path)
        plot_grid(obstacles, path)
    else:
        print("Não foi possível encontrar um caminho.")

if __name__ == "__main__":
    main()



