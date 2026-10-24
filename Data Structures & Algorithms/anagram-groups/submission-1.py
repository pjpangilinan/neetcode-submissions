class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for i, a in enumerate(strs):
            l = tuple(sorted(a))
            if l in anag:
                anag[l].append(i)
            else:
                anag[l] = [i]
        
        lis = []
        for ana in anag.keys():
            li = []
            for i in anag[ana]:
                li.append(strs[i])
            lis.append(li)

        return lis