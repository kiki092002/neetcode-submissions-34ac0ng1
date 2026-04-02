class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result =[]
        candidates.sort()
        def back_tracking(start,current,target):

             # Base case: when the target is reduced to 0, add the combination to the result
            if target == 0:
                result.append(current[:])
                return
            
            for i in range(start, len(candidates)):
                # If the current number is greater than the target, we break early (pruning)
                if candidates[i] > target:
                    break
                
                # Skip duplicates: if the current number is the same as the previous, skip it
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Add the current number to the combination and recurse
                current.append(candidates[i])
                back_tracking(i + 1, current, target - candidates[i])  # Move to the next index
                current.pop()  # Backtrack and remove the last number
        back_tracking(0,[],target)
        return result