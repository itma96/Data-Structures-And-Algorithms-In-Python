from LinkedList import LinkedList, printList

def reverse_list(n):
    if n._next == None:
        l = LinkedList()
        l.add_last(n._element)
        return l
    
    l = reverse_list(n._next)
    l.add_last(n._element)
    return l

if __name__ == "__main__":
    l = LinkedList()
    for i in range(10):
        l.add_last(i)
    l_rev = reverse_list(l.first())
    printList(l_rev)