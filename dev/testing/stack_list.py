

class stack:
    '''
    ''' 
    def __init__(self):
        self.stack = []


    def push(self, item):
        self.stack.append(item)

    def pop(self, item):
        self.stack.pop(item)

    def is_empty(self):
        return len(self.stack)
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None