class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        array = []

        for element in strs:
            if ''.join(sorted(element)) not in group:
                group["".join(sorted(element))] = [element]
            else:
                group["".join(sorted(element))].append(element)
        
        for key in group:
            array.append(group.get(key))
        
        return array