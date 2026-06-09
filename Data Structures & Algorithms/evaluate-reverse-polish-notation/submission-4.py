class Solution:
    def apply_operator(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b

    def evalRPN(self, tokens: List[str]) -> int:
        operator_set = {'+', '-', '/', '*'}
        stack = []
        for i in tokens:
            if i in operator_set:
                new_int = self.apply_operator(int(stack[-2]), int(stack[-1]), i)
                stack.pop()
                stack.pop()
                stack.append(new_int)
            else: 
                stack.append(i)
        return int(stack[0])
        
