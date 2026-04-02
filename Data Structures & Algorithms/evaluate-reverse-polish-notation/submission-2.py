class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # loop through the list
        # if it's number , we add to stack
        # if it's a operator we pop to add, apply operation
        # push result back to stack
        stack = [] 
        for token in tokens:
            if token not in {'+',"-","*",'/'}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    c = b + a
                    stack.append(c)
                elif token == "-":
                    c = a-b
                    stack.append(c)
                elif token == "*":
                    c = a*b
                    stack.append(c)
                else:
                    c = int(a/b)
                    stack.append(c)

        return stack[-1]