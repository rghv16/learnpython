class Stack:
    '''
    https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/balanced-brackets-3-4fc590c6/
    '''
    
    def __init__(self):
        '''
        '''
        self.l = []
    
    def top(self):
        '''
        '''
        return self.l[-1]
    
    def push(self, ele):
        '''
        '''
        self.l.append(ele)
        
    def pop(self):
        '''
        '''
        return self.l.pop()
        
    
for _ in range(int(input())):
    
    stack = Stack()
    stack.push('$')
    inp = input()
    
    for ele in inp:
        if stack.top() == ele:
            stack.pop()
        elif ele == '(':
            stack.push(')')
        elif ele == '{':
            stack.push('}')
        elif ele == '[':
            stack.push(']')
        
    if stack.top() == '$':
        print('YES')
    else:
        print('NO')
    

