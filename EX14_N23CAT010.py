class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth   

    def fmt(self):
        p = self.parent.state if self.parent else "none"
        return f"({self.state},{p},depth={self.depth})"


def depth_limited_search(start, goal, graph, limit):
    stack = []
    stack.append(Node(start, depth=0))

    step = 1
    print("step state")

    while stack:
        current = stack.pop()
        print(step, current.fmt())
        step += 1

        if current.state == goal:
            return current

        
        if current.depth == limit:
            continue

        
        for neighbor in reversed(graph.get(current.state, [])):
            stack.append(Node(neighbor, parent=current, depth=current.depth + 1))

    return None


# Ví dụ graph
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


limit = 3
result = depth_limited_search("A", "G", graph, limit)
if result:
    print("Tim thay:", result.state)
    print_path(result)
else:
    print("Khong tim thay (do gioi han do sau =", limit, ")")
