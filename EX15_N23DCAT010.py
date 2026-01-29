class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

    def fmt(self):
        p = self.parent.state if self.parent else "none"
        return f"({self.state},{p},depth={self.depth})"


def dls(start, goal, graph, limit):
    stack = [Node(start, depth=0)]

    while stack:
        current = stack.pop()

        if current.state == goal:
            return current

        if current.depth == limit:
            continue

        for neighbor in reversed(graph.get(current.state, [])):
            stack.append(Node(neighbor, parent=current, depth=current.depth + 1))

    return None


def ids(start, goal, graph, max_depth):
    for limit in range(max_depth + 1):
        print("\n=== LIMIT =", limit, "===")
        result = dls(start, goal, graph, limit)
        if result:
            return result
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

result = ids("A", "G", graph, max_depth=5)
if result:
    print("\nTim thay:", result.state, "tai depth =", result.depth)
else:
    print("\nKhong tim thay")

path = []
cur = result
while cur:
    path.append(cur.state)
    cur = cur.parent
print("Duong di:", " -> ".join(reversed(path)))
