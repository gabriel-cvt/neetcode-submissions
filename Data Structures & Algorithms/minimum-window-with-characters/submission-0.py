class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Add frequency of chars
        hashmap = {}
        for c in t:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        # Create the window dinamically from start
        # Go foward with right until the frequency is valid
        # When it's valid, we can shrink L until is no longer valid, tracking the min len

        # When it is valid ?
        # When missing characteres is equal to 0
        l, r = 0, 0
        missing = len(t)
        min_len = float('inf')
        start = 0
        for r in range(len(s)):
            c = s[r]
            hashmap[c] = hashmap.get(c, 0) - 1
            if hashmap[c] >= 0:
                missing -= 1
            
            while missing == 0:
                curr_len = r - l + 1
                if curr_len < min_len:
                    min_len = curr_len
                    start = l

                c = s[l]
                hashmap[c] = 1 + hashmap.get(c, 0)
                if hashmap[c] > 0:
                    missing += 1

                l += 1

        return "" if min_len == float('inf') else s[start: start + min_len]

        
        