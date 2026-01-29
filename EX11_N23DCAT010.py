from collections import deque


class Node:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

    
    def fmt(self):
        p = self.parent.state if self.parent else "none"
        m = self.move if self.move is not None else "none"
        return f"({self.state},{p},{m},{self.cost})"

def bfs(start, goal, graph):
    openL = deque()
    openL.append(Node(start))

    closeL = []          
    visited = set([start])

    step = 1
    print("step state      openL      closeL")

    while openL:
        current = openL.popleft()
        s = current.state

        closeL.append(current)

        # nếu gặp đích thì in step rồi dừng
        if s == goal:
            open_str = ",".join(n.fmt() for n in openL) or "none"
            close_str = ",".join(n.fmt() for n in closeL) or "none"
            print(step, current.fmt(), open_str, close_str)
            return current

        
        for neighbor in graph.get(s, []):
            if neighbor not in visited:
                visited.add(neighbor)
                child = Node(
                    state=neighbor,
                    parent=current,
                    move=None,
                    cost=current.cost + 1
                )
                openL.append(child)

        
        open_str = ",".join(n.fmt() for n in openL) or "none"
        close_str = ",".join(n.fmt() for n in closeL) or "none"
        print(step, current.fmt(), open_str, close_str)
        step += 1

    return None

# Ví dụ graph (danh sách kề)
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


result = bfs("A", "G", graph)
if result:
    print("Tim thay:", result.state, "cost =", result.cost)
    print_path(result)
else:
    print("Khong tim thay")
