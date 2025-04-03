def get_nth(node, index):
    if node is None or index < 0:
        raise IndexError
    curr = node
    for i in range(index):
        if curr.next is None and i != index:
            raise IndexError
        curr = curr.next
    return curr