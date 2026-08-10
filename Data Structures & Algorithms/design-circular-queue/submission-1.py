class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.num = 0
        self.k = k
        self.front = Node()
        self.rear = self.front
        

    def enQueue(self, value: int) -> bool:
        if self.num == 0:
            self.front.val = value
        else:
            if self.num < self.k:
                node = Node(value)
                self.rear.next = node
                self.rear = self.rear.next
            else:
                return False
        self.num +=1
        print(self.front.val, self.rear.val)
        return True


    def deQueue(self) -> bool:
        if self.num == 0:
            return False
        if self.front == self.rear:
            self.num -=1
            return True
        self.front = self.front.next
        self.num -=1
        return True

    def Front(self) -> int:
        if self.num == 0:
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.num == 0:
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        if self.num == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.num == self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()