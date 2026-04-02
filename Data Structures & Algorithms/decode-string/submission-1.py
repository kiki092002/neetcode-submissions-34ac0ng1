class Solution:
    def decodeString(self, s: str) -> str:
        

        num_stack = []  
        str_stack = [] 
        curr="" 
        k = 0 

        for c in s:
            if c.isdigit():
                k = k*10+int(c)
            elif c=='[':
                str_stack.append(curr)
                num_stack.append(k)
                curr=""
                k=0
            elif c ==']':
                temp = curr
                curr = str_stack.pop()
                num = num_stack.pop()
                curr += temp*num
            else:
                curr+=c
        return curr

        