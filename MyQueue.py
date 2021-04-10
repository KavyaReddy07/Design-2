class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_ = []
        self.out = []
    

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.out:
            while self.in_:
                self.out.append(self.in_.pop(-1))
        # print('out', self.out[-1])
                
        el = self.out[-1]
        del self.out[-1]
        return el
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.out:
            while self.in_:
                self.out.append(self.in_.pop(-1))
                
        if self.out: 
            return self.out[-1]
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.out or self.in_:
            return False
        else:
            return True
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()