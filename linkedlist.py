class Node:
    start, itr  = None, None
    def __init__(self) -> None:
        self.data = None
        self.next = None

    def append(self, data):
        n = Node()
        n.data = data
        if self.start is None:
            self.start = n
            self.itr = n
        else:
            self.itr.next = n
        self.itr = n

    def print(self):
        p = self.start
        while p:
            print(p.data)
            p = p.next
    
    def pop(self):
        p = self.start
        prev = None
        while p.next:
            prev = p
            p = p.next
        prev.next = None
        return p.data

    def size(self):
        cnt = 0
        p = self.start
        while p:
            cnt += 1
            p = p.next
        return cnt

    def reverse(self):
        p, q = self.start, self.start
        stack = []
        while p:
            stack.append(p)
            prev = p
            p = p.next
        
        print(stack)

        #m = Node()
        x = stack.pop()
        curr = x

        while len(stack) > 0:
            n = stack.pop()
            curr.next = n
            curr = n
        curr.next = None
        self.start = x
        

if __name__ == '__main__':
    m = Node()
    m.append(4)
    m.append(5)
    m.append(6)
    m.append(7)

    m.print()

    print(m.pop())

    m.print()

    print(m.size())

    m.reverse()
    m.print()