from collections import defaultdict
class Node:
    def __init__(self, index, value):
        self.parent = None
        self.index = index
        self.value = value
        self.xp = 0

    def visit(self):
        if self.parent:
            self.xp = self.value + self.parent.xp
        else:
            self.xp = self.value


class Graph:
    def __init__(self, root):
        self.most_xp = 0
        self.graph = defaultdict(list)
        self.nodes = {0: root}
        self.visited = [False]

    def addDaun(self, parent_index, child_index, value):
        node = Node(child_index, value)
        self.graph[parent_index].append(node)
        self.nodes.update({child_index: node})
        node.parent = self.nodes[parent_index]
        self.visited.append(False)

    def shukai(self):
        stack = [self.nodes[0]]
        while len(stack) > 0:
            current_node = stack.pop()
            if not self.visited[current_node.index]:
                node_index = current_node.index
                self.visited[node_index] = True
                self.nodes[node_index].visit()

                exp = self.nodes[node_index].xp
                if exp > self.most_xp:
                    self.most_xp = exp

                for child in self.graph[node_index]:
                    if not self.visited[child.index]:
                        stack.append(child)