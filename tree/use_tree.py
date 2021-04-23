import random
from tree import Node, NodeMgmt

head = Node(100)
node = NodeMgmt(head)
rand_list = []

for i in range(20):
    rand_list.append(random.randint(0, 999))

for i in rand_list:
    node.insert(i)

for i in rand_list:
    print(node.remove(i))
