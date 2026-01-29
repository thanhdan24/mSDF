import heapq

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def fmt(self):
        p = self.parent.state if self.parent else "none"
        return f"({self.state},{p},{self.cost})"


def ucs(start, goal, graph):
    openL = []
    closeL = []
    visited = set()

    t = 0  
    heapq.heappush(openL, (0, t, Node(start, cost=0)))

    step = 1
    print("step state      openL      closeL")

    while openL:
        cost, _, current = heapq.heappop(openL)

        if current.state in visited:
            continue
        visited.add(current.state)
        closeL.append(current)

        if current.state == goal:
            open_str = ",".join(item[2].fmt() for item in sorted(openL)) or "none"
            close_str = ",".join(n.fmt() for n in closeL) or "none"
            print(step, current.fmt(), open_str, close_str)
            return current

        for neighbor, w in graph.get(current.state, []):
            if neighbor not in visited:
                child = Node(neighbor, parent=current, cost=current.cost + w)
                t += 1
                heapq.heappush(openL, (child.cost, t, child))

        open_str = ",".join(item[2].fmt() for item in sorted(openL)) or "none"
        close_str = ",".join(n.fmt() for n in closeL) or "none"
        print(step, current.fmt(), open_str, close_str)
        step += 1

    return None


graph = {
    "A": [("B", 2), ("C", 1)],
    "B": [("D", 3), ("E", 1)],
    "C": [("F", 4)],
    "D": [],
    "E": [("G", 2)],
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

result = ucs("A", "G", graph)
if result:
    print("Tim thay:", result.state, "cost =", result.cost)
    print_path(result)
else:
    print("Khong tim thay")


