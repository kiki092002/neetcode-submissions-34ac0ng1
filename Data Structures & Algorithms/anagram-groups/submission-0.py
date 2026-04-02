class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            # use sorted word as a key to group word
            sorted_word = ''.join(sorted(word))
            # if sorted key not in anagrams, create new list
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            
            anagrams[sorted_word].append(word)
            #print(sorted_word,anagrams[sorted_word])
             # Print the entire dictionary to see the current state
            #print(f"After adding '{word}': {anagrams}")

        return list(anagrams.values())