import sys

from common import input_parser



class Node:
    child_nodes = []
    metadata = []

    def __init__(self, child_nodes, metadata):
        self.child_nodes = child_nodes
        self.metadata = metadata

    def sum(self):
        return sum(self.metadata)

def parse(numbers):
    number_of_child_nodes = numbers[0]
    size_of_metadata = numbers[1]

   # print("number_of_child_nodes:", number_of_child_nodes)
   # print("size_of_metadata:", size_of_metadata)

    children = []
    if number_of_child_nodes == 0:
       # print("create node", numbers[2:2 + size_of_metadata])
        node = Node([], numbers[2:2 + size_of_metadata])
        return node, size_of_metadata + 2
    else:
        total_size = 0
        childnodes_part = numbers[2:-size_of_metadata]

        while len(childnodes_part) != 0:
            node, size = parse(childnodes_part)
            children.append(node)
            del childnodes_part[0:size]
            total_size += size

        return Node(children, numbers[-size_of_metadata:]), total_size + 2 + size_of_metadata


def sum_metadata(node):
    if node.child_nodes != []:
        sum_child_nodes = 0
        for child_node in node.child_nodes:
            sum_child_nodes += sum_metadata(child_node)

        return sum_child_nodes + node.sum()
    else:
        return node.sum()

if __name__ == '__main__':
    licence_file = []
    with open("input.txt", "r") as f:
        line = f.read()
        items = line.split()
        licence_file = list(map(int, items))

    #print(licence_file)

    sys.setrecursionlimit(3200)  #maybe rewrite to iterative?
    main_node = parse(licence_file)

    print(main_node)
    print(sum_metadata(main_node[0]))




