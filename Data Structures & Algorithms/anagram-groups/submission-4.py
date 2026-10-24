class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            word = str(sorted(i))
            res[word].append(i)
        
        return list(res.values())