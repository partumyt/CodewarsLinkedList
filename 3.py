def push(head, data):
    nn = Node(data)
    nn.next = head
    return nn

def build_one_two_three():
    n1, n2, n3 = Node(1), Node(2), Node(3)
    n2.next = n3
    n1.next = n2
    return n1