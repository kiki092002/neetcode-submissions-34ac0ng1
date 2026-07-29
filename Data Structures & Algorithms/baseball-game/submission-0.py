class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = [] 
        for i in range(len(operations)):
            if operations[i] not in ['C','D','+']:
                records.append(int(operations[i]))
            elif operations[i] == '+':
               
                records.append(records[-1]+records[-2])
            elif operations[i] == 'D':
                
                records.append(records[-1]*2)
            else:
                
                inval = records.pop()
        return sum(records)
                
        
