from typing import Set, Tuple, List

#set() - превращает объект во множество. При длобавлении элемента проверяет, есть ли такой элемент в нем
my_list = [1,2]
my_set = set(my_list)
my_set.add(3) #добавление
my_set.remove(1) #удаление элемента (не по номеру, а по значению)
a_set = {1,2}
b_set = {1,3}
a_set.union(b_set) #объединение. Просто возвращает новое множество, старые не заменяет
a_set.intersection(b_set) #пересечение. Общие элементы
a_set.difference(b_set) #разница
elements = [i for i in a_set] #множества поддерживают итерацию

#дуги
edge = (1,2)
edge_set = set([(1,2), (1,3)])

class Graph:
    def __init__(self):
        self.edges: Set[Tuple[str, str]] = set()  # дуги
        self.nodes: Set[str] = set() #вершины

    def add_node(self, node: str) -> None:
        self.nodes.add(node)

    def add_edge(self, edge: Tuple[str]) -> None:
        self.edges.add(edge)

    def get_neighbours(self, node: str) -> Set[str]:
        neighbours = set()
        for edge in self.edges:
            if edge[0] == node:
                neighbours.add(edge[1])
            elif edge[1] == node:
                neighbours.add(edge[0])
        return neighbours

    # Обход графа в ширину. Принимаем за вход стратовую вершину и обходим всех ее соседей. Затем берем соседа и обходим всех его соседей и тд
    def breadth_first_walk(self, start_node: str) -> List[str]:
        visited_nodes = set()
        queue_to_visit = set(start_node)
        visited_nodes_list = []

        while queue_to_visit:
            visiting = queue_to_visit.pop()
            # if visiting == finish_node: Сделать поиск кратчайшего пути
            #     finish_node_neighbours = set(self.get_neighbours(finish_node))
            #     for node_in_way in visited_nodes_list:
            #         if
            neighbours = self.get_neighbours(visiting)
            visited_nodes.add(visiting)
            visited_nodes_list.append(visiting)
            for node in neighbours:
                if node not in visited_nodes:
                    queue_to_visit.add(node)

        return visited_nodes_list

    # Обход графа в глубину
    def depth_first_walk(self, start_node: str, visited=set()) -> Set[str]:
        visited.add(start_node)
        for neighbour in self.get_neighbours(start_node):
            if neighbour not in visited:
                self.depth_first_walk(neighbour, visited)
        return visited

#NetworkX - библиотека для работы с графами


graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_edge(('A','B'))
graph.add_edge(('B','C'))
graph.add_edge(('C','D'))

print(graph.nodes)
print(graph.edges)
print(graph.get_neighbours('B'))
print(graph.breadth_first_walk('B'))
print(graph.depth_first_walk('B'))



