class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        idx = 0
        while curr:
            if idx == index:
                return curr.val
            curr = curr.next
            idx += 1
        return -1

        
    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        # [1]->[2]->[3]->[4]
        # remove 0 -> self.head = self.head.next
        # remove 1 -> prev.next = curr.next
        curr = self.head
        i = 0
        while curr.next and i < index:
            curr = curr.next
            i += 1
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
