from __future__ import annotations
from math import lcm

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
    

with open("input.txt", "r") as network_description:
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

    starting_nodes = [node for node in nodes if node[2] == "A"]
    current_nodes = [nodes[node] for node in starting_nodes]
    steps_per_node = [0 for _ in range(len(current_nodes))]
    cycle_lengths = [0 for _ in range(len(current_nodes))]
    for index in range(len(current_nodes)):
        current_node = current_nodes[index]
        current_node_steps = steps_per_node[index]
        starting_node = current_nodes[index]

        end_node = None
        end_node_after_steps = 0
        while True:
            if current_node.value[2] == "Z":
                if end_node is None:
                    end_node = current_node
                    end_node_after_steps = current_node_steps
                else:
                    if end_node.value == current_node.value:
                        cycle_lengths[index] = current_node_steps - end_node_after_steps
                        break
            direction = path[current_node_steps % number_of_steps]
            if direction == "L":
                current_node = current_node.go_left()
            else:
                current_node = current_node.go_right()
            current_node_steps += 1
        steps_per_node[index] = current_node_steps
        steps += 1

    min_steps = lcm(*cycle_lengths)

    print(min_steps)