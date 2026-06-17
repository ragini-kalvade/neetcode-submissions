class MinStack:

    def __init__(self):
        self.minstack = list()
        
    def push(self, val: int) -> None:
        self.minstack.append(val)

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        minval = float('inf')
        for x in self.minstack:
            if x < minval:
                minval = x
        return minval

        
