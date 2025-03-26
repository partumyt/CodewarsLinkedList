def linked_list_from_string(s):
    s = s.split(" -> ")
    if s[-1] == "None": s.pop()
    if not s:
        return None
    head = Node(int(s[0]))
    cur = head
    for i in s[1:]:
        cur.next = Node(int(i))
        cur = cur.next
    return head
