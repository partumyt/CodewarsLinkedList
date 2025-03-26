def stringify(node):
    res = ""
    cur = node
    while cur is not None:
        res += str(cur.data) + " -> "
        cur = cur.next
    return res + "None"
