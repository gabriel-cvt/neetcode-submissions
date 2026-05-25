from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        for k in sorted(freq):
            while freq[k] > 0:
                aux = k
                for _ in range(groupSize):
                    if aux not in freq or freq[aux] <= 0:
                        return False
                    freq[aux] -= 1
                    aux += 1
        return True 