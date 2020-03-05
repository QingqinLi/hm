class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.stack:
            self.stack.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        if self.stack:
            return self.stack[len(self.stack)-1]
        else:
            return


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.stack) == 0 else False

    def str(self):
        return self.stack



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
param_2 = obj.pop()
print(obj.str())
param_3 = obj.top()
param_4 = obj.empty()
print(obj.str())