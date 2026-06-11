class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        debt = prices[0] + prices[1]
        return money - debt if debt <= money else money