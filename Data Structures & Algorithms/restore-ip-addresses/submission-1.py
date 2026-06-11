class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        
        res = []
        def backtrack(index, parts):
            if len(parts) == 4:
                if index == len(s):
                    res.append(".".join(parts))
                return
            
            for i in range(index, min(index + 3, len(s))):
                seg = s[index:i+1]

                if len(seg) > 1 and seg[0] == "0":
                    continue
                
                if int(seg) <= 255:
                    parts.append(seg)
                    backtrack(i + 1, parts)
                    parts.pop()
        
        backtrack(0, [])
        return res
