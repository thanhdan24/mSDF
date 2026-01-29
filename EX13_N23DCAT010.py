class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def fmt(self):
        p = self.parent.state if self.parent else "none"
        return f"({self.state},{p},{self.cost})"


def dfs_stack(start, goal, graph):
    stack = []                 
    stack.append(Node(start))  

    visited = set()
    step = 1
    print("step state")

    while stack:
        current = stack.pop()  
        s = current.state

        if s in visited:
            continue
        visited.add(s)

        print(step, current.fmt())
        step += 1

        if s == goal:
            return current

        for neighbor in reversed(graph.get(s, [])):
            if neighbor not in visited:
                stack.append(Node(neighbor, parent=current, cost=current.cost + 1))

    return None


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def print_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print("Duong di:", " -> ".join(path))

result = dfs_stack("A", "G", graph)
if result:
    print("Tim thay:", result.state, "cost =", result.cost)
    print_path(result)
else:
    print("Khong tim thay")
