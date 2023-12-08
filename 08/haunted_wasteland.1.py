from __future__ import annotations

class Node:
    left: Node
    right: Node
    value: str

    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None
    
    def add_left(self, node: Node):
        self.left = node
    
    def add_right(self, node: Node):
        self.right = node
    
    def go_left(self):
        if self.left is None:
            raise ValueError("No left node")
        return self.left

    def go_right(self):
        if self.right is None:
            raise ValueError("No right node")
        return self.right
    

with open("test_input.txt", "r") as network_description:
    path = [*network_description.readline().strip()]
    _ = network_description.readline()
    nodes = {}
    paths = {}
    for line in network_description:
        value, left_right = line.split("=")
        value = value.strip()
        left_right = left_right.strip().split(",")
        left = left_right[0].strip()[1:]
        right = left_right[1].strip()[:-1]
        nodes[value] = Node(value)
        paths[value] = (left, right)
    for node in nodes:
        left, right = paths[node]
        if left in nodes:
            nodes[node].add_left(nodes[left])
        if right in nodes:
            nodes[node].add_right(nodes[right])
    
    steps = 0
    number_of_steps = len(path)
    current_node = nodes["AAA"]
    while current_node.value != "ZZZ":
        direction = path[steps % number_of_steps]
        if direction == "L":
            current_node = current_node.go_left()
        else:
            current_node = current_node.go_right()
        steps += 1
    print(steps)