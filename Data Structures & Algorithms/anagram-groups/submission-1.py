class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            sort = str(sorted(i))
            result[sort].append(i)
        
        return list(result.values())