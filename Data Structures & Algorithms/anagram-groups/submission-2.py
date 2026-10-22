class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            sortedWord = str(sorted(i))
            d[sortedWord].append(i)
        
        return list(d.values())